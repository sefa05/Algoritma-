#!/usr/bin/env python3
"""Ölçtüm deney çalıştırıcısı.

Bir sınıflandırma veri setini birden fazla modele gönderir, ham cevapları kaydeder
ve doğruluk / maliyet / süre raporu üretir.

Kullanım:
    python deneyler/calistir.py deneyler/olctum-01                # deneyi çalıştır
    python deneyler/calistir.py deneyler/olctum-01 --deneme       # API çağırmadan uçtan uca test
    python deneyler/calistir.py deneyler/olctum-01 --sadece-rapor # kayıtlı cevaplardan raporu yeniden üret

Deney klasöründe beklenen dosyalar:
    veri-seti-modele-giden.csv   id, metin
    veri-seti-etiketli.csv       id, onerilen_etiket, sefa_etiketi, zor, ...
    sistem-istemi.md             ilk ``` kod bloğu sistem istemidir
    modeller.json                model listesi (bkz. olctum-01/modeller.json)

Çıktılar (aynı klasöre):
    ham-sonuclar.jsonl   her (model, e-posta) çağrısı; yarıda kalırsa kaldığı yerden devam eder
    sonuc-sablonu.csv    doğru etiket + her modelin cevabı + süre
    rapor.md             özet tablo, kategori bazında doğruluk, karışıklıklar, zor örnekler
    (--deneme çıktıları -deneme ekiyle ayrı dosyalara yazılır)
"""

import argparse
import csv
import json
import random
import re
import statistics
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ETIKETLER = ["SIPARIS_DURUMU", "IADE_DEGISIM", "FATURA_ODEME", "TEKNIK_SORUN", "SIKAYET_DIGER"]


# ---------------------------------------------------------------- veri

def veri_oku(klasor: Path):
    with open(klasor / "veri-seti-modele-giden.csv", encoding="utf-8") as f:
        epostalar = [(r["id"], r["metin"]) for r in csv.DictReader(f)]
    dogru, zor = {}, {}
    with open(klasor / "veri-seti-etiketli.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            # Sefa'nın etiketi varsa nihai doğru cevap odur.
            dogru[r["id"]] = (r.get("sefa_etiketi") or "").strip() or r["onerilen_etiket"]
            zor[r["id"]] = r.get("zor") == "evet"
    istem_md = (klasor / "sistem-istemi.md").read_text(encoding="utf-8")
    eslesme = re.search(r"```\n(.*?)```", istem_md, re.S)
    if not eslesme:
        sys.exit("sistem-istemi.md içinde ``` kod bloğu bulunamadı.")
    modeller = json.loads((klasor / "modeller.json").read_text(encoding="utf-8"))
    return epostalar, dogru, zor, eslesme.group(1).strip(), modeller


def etiket_ayikla(metin: str):
    """Cevabı normalize eder. Geçerli bir etiket değilse None döner (format hatası)."""
    temiz = metin.strip().strip(".`'\" \n").upper()
    return temiz if temiz in ETIKETLER else None


# ---------------------------------------------------------------- sağlayıcılar

class AnthropicCagirici:
    def __init__(self, cfg):
        import anthropic  # pip install anthropic

        self.anthropic = anthropic
        self.client = anthropic.Anthropic(max_retries=4)
        self.cfg = cfg

    def cagir(self, sistem: str, metin: str) -> dict:
        # Not: Claude Opus 5.5 / Sonnet 5.5 sıcaklık (temperature) kabul etmez ve Opus 5.5'te
        # düşünme kapatılamaz; bu yüzden parametreler model bazında modeller.json'dan gelir.
        # Refusal fallback bilinçli olarak KAPALI: açık olsaydı reddedilen istek başka bir
        # modelde çalışır ve ölçüm kirlenirdi. Reddetme ayrı bir sonuç olarak kaydedilir.
        yanit = self.client.messages.create(
            model=self.cfg["model"],
            system=sistem,
            messages=[{"role": "user", "content": metin}],
            **self.cfg.get("parametreler", {}),
        )
        cikti = "".join(b.text for b in yanit.content if b.type == "text")
        return {
            "cevap": cikti,
            "durma_nedeni": yanit.stop_reason,
            "girdi_token": yanit.usage.input_tokens,
            "cikti_token": yanit.usage.output_tokens,  # düşünme token'ları dahil
        }


class OpenAIUyumluCagirici:
    """Claude dışındaki sağlayıcılar için (OpenAI, OpenRouter, yerel vLLM/Ollama vb.)."""

    def __init__(self, cfg):
        import os

        from openai import OpenAI  # pip install openai

        anahtar_env = cfg.get("api_anahtari_env", "OPENAI_API_KEY")
        self.client = OpenAI(base_url=cfg.get("base_url"), api_key=os.environ.get(anahtar_env), max_retries=4)
        self.cfg = cfg

    def cagir(self, sistem: str, metin: str) -> dict:
        yanit = self.client.chat.completions.create(
            model=self.cfg["model"],
            messages=[{"role": "system", "content": sistem}, {"role": "user", "content": metin}],
            **self.cfg.get("parametreler", {}),
        )
        secim = yanit.choices[0]
        return {
            "cevap": secim.message.content or "",
            "durma_nedeni": secim.finish_reason,
            "girdi_token": yanit.usage.prompt_tokens if yanit.usage else 0,
            "cikti_token": yanit.usage.completion_tokens if yanit.usage else 0,
        }


class DenemeCagirici:
    """--deneme: ağ çağrısı yapmadan boru hattını test eder. Sonuçlar anlamsızdır."""

    def __init__(self, cfg):
        self.rng = random.Random(cfg["ad"])

    def cagir(self, sistem: str, metin: str) -> dict:
        time.sleep(0.001)
        cevap = self.rng.choice(ETIKETLER + ["Bu bir iade talebidir."])
        return {"cevap": cevap, "durma_nedeni": "deneme", "girdi_token": 300, "cikti_token": 5}


SAGLAYICILAR = {"anthropic": AnthropicCagirici, "openai_uyumlu": OpenAIUyumluCagirici}


# ---------------------------------------------------------------- çalıştırma

def kayitli_oku(yol: Path):
    kayitlar = []
    if yol.exists():
        with open(yol, encoding="utf-8") as f:
            kayitlar = [json.loads(s) for s in f if s.strip()]
    return kayitlar


def calistir(klasor: Path, deneme: bool, paralel: int):
    epostalar, _, _, sistem, modeller = veri_oku(klasor)
    ham_yol = klasor / ("ham-sonuclar-deneme.jsonl" if deneme else "ham-sonuclar.jsonl")
    yapilan = {(k["model_ad"], k["id"]) for k in kayitli_oku(ham_yol) if "hata" not in k}
    kilit = threading.Lock()

    for cfg in modeller:
        if "[" in cfg["model"]:
            print(f"⏭  {cfg['ad']} atlandı: model kimliği doldurulmamış ({cfg['model']})")
            continue
        cagirici = DenemeCagirici(cfg) if deneme else SAGLAYICILAR[cfg["saglayici"]](cfg)
        kalan = [(i, m) for i, m in epostalar if (cfg["ad"], i) not in yapilan]
        print(f"▶  {cfg['ad']} · {cfg['etiket']}: {len(kalan)} e-posta")

        def tek(i, m):
            bas = time.perf_counter()
            try:
                sonuc = cagirici.cagir(sistem, m)
            except Exception as e:  # kaydet, sonraki çalıştırmada tekrar denenir
                return {"model_ad": cfg["ad"], "id": i, "hata": f"{type(e).__name__}: {e}"}
            sonuc.update(model_ad=cfg["ad"], id=i, sure_sn=round(time.perf_counter() - bas, 3))
            return sonuc

        with ThreadPoolExecutor(max_workers=paralel) as havuz, open(ham_yol, "a", encoding="utf-8") as f:
            isler = [havuz.submit(tek, i, m) for i, m in kalan]
            for n, is_ in enumerate(as_completed(isler), 1):
                kayit = is_.result()
                with kilit:
                    f.write(json.dumps(kayit, ensure_ascii=False) + "\n")
                    f.flush()
                if "hata" in kayit:
                    print(f"   ⚠ {kayit['id']}: {kayit['hata'][:120]}")
                if n % 20 == 0:
                    print(f"   {n}/{len(kalan)}")
    return ham_yol


# ---------------------------------------------------------------- rapor

def rapor_uret(klasor: Path, ham_yol: Path):
    epostalar, dogru, zor, _, modeller = veri_oku(klasor)
    kayitlar = [k for k in kayitli_oku(ham_yol) if "hata" not in k]
    son = {(k["model_ad"], k["id"]): k for k in kayitlar}  # tekrar varsa en sonuncusu
    usd_try = next((m["usd_try"] for m in modeller if (m.get("usd_try") or {}).get("kur")), None)
    ids = [i for i, _ in epostalar]
    ek = "-deneme" if "deneme" in ham_yol.name else ""  # deneme çıktıları gerçek dosyaları ezmez
    aktif = [m for m in modeller if any((m["ad"], i) in son for i in ids)]

    satirlar, detay = [], {}
    for m in aktif:
        k = [son[(m["ad"], i)] for i in ids if (m["ad"], i) in son]
        tahmin = {x["id"]: etiket_ayikla(x["cevap"]) for x in k}
        dogru_say = sum(tahmin[x["id"]] == dogru[x["id"]] for x in k)
        zor_ids = [x["id"] for x in k if zor[x["id"]]]
        fiyat = m.get("fiyat_usd_1m") or {}
        gt, ct = sum(x["girdi_token"] for x in k), sum(x["cikti_token"] for x in k)
        usd = None
        if fiyat.get("girdi") is not None and fiyat.get("cikti") is not None:
            usd = (gt * fiyat["girdi"] + ct * fiyat["cikti"]) / 1e6 * (100 / len(k))
        sureler = [x["sure_sn"] for x in k]
        satirlar.append({
            "ad": m["ad"], "etiket": m["etiket"], "n": len(k),
            "dogruluk": dogru_say / len(k),
            "zor_dogruluk": (sum(tahmin[i] == dogru[i] for i in zor_ids) / len(zor_ids)) if zor_ids else None,
            "format_hatasi": sum(v is None for v in tahmin.values()),
            "reddetme": sum(x["durma_nedeni"] == "refusal" for x in k),
            "usd_100": usd, "tl_100": usd * usd_try["kur"] if usd is not None and usd_try else None,
            "ort_sure": statistics.mean(sureler), "medyan_sure": statistics.median(sureler),
            "girdi_token": gt, "cikti_token": ct,
        })
        kategori = defaultdict(lambda: [0, 0])
        karisik = Counter()
        for i, t in tahmin.items():
            kategori[dogru[i]][1] += 1
            if t == dogru[i]:
                kategori[dogru[i]][0] += 1
            else:
                karisik[(dogru[i], t or "FORMAT_HATASI")] += 1
        detay[m["ad"]] = (kategori, karisik, tahmin)

    # sonuc-sablonu.csv
    with open(klasor / f"sonuc-sablonu{ek}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "dogru_etiket"] + [f"model_{m['ad'].lower()}" for m in aktif]
                   + [f"model_{m['ad'].lower()}_sure_sn" for m in aktif])
        for i in ids:
            w.writerow([i, dogru[i]]
                       + [(son.get((m["ad"], i)) or {}).get("cevap", "").strip() for m in aktif]
                       + [(son.get((m["ad"], i)) or {}).get("sure_sn", "") for m in aktif])

    # rapor.md
    yuzde = lambda x: "—" if x is None else f"%{x * 100:.0f}"
    para = lambda x, s: "—" if x is None else f"{x:.4f} {s}"
    r = [f"# {klasor.name} — Sonuç Raporu", "",
         f"Kaynak: `{ham_yol.name}` · E-posta: {len(ids)} · Zor örnek: {sum(zor.values())}", ""]
    if "deneme" in ham_yol.name:
        r += ["> ⚠️ **DENEME ÇALIŞTIRMASI — rakamlar rastgeledir, içerikte KULLANILMAZ.**", ""]
    r += ["| Model | Doğruluk | Zor örneklerde | Format hatası | Reddetme | 100 e-posta maliyeti | Ort. süre (sn) |",
          "|---|---|---|---|---|---|---|"]
    for s in satirlar:
        maliyet = para(s["tl_100"], "TL") if s["tl_100"] is not None else para(s["usd_100"], "USD")
        r.append(f"| {s['ad']} · {s['etiket']} | {yuzde(s['dogruluk'])} | {yuzde(s['zor_dogruluk'])} | "
                 f"{s['format_hatasi']} | {s['reddetme']} | {maliyet} | {s['ort_sure']:.2f} |")
    if usd_try:
        r += ["", f"Kur: 1 USD = {usd_try['kur']} TL ({usd_try.get('tarih', 'tarih yok')})"]
    r += ["", "Maliyet = gerçek token kullanımı × `modeller.json`'daki liste fiyatı. Çıktı token'ına düşünme token'ları dahildir.", ""]
    for m in aktif:
        kategori, karisik, tahmin = detay[m["ad"]]
        r += [f"## {m['ad']} · {m['etiket']}", "", "| Kategori | Doğru / Toplam |", "|---|---|"]
        r += [f"| {e} | {kategori[e][0]} / {kategori[e][1]} |" for e in ETIKETLER]
        r += ["", "**En çok karıştırılanlar:** " + (", ".join(
            f"{a} → {b} ({n})" for (a, b), n in karisik.most_common(3)) or "yok")]
        zor_yanlis = [i for i in ids if zor[i] and tahmin.get(i) != dogru[i] and i in tahmin]
        r += ["", f"**Yanlış bilinen zor örnekler:** {', '.join(zor_yanlis) or 'yok'}", ""]
    (klasor / f"rapor{ek}.md").write_text("\n".join(r) + "\n", encoding="utf-8")
    print("\n".join(r[:8 + len(satirlar)]))
    print(f"\n✓ Rapor: {klasor / f'rapor{ek}.md'}")


def main():
    p = argparse.ArgumentParser(description="Ölçtüm deney çalıştırıcısı")
    p.add_argument("klasor", type=Path)
    p.add_argument("--deneme", action="store_true", help="API çağırmadan uçtan uca test")
    p.add_argument("--sadece-rapor", action="store_true", help="kayıtlı cevaplardan raporu yeniden üret")
    p.add_argument("--paralel", type=int, default=4, help="model başına eşzamanlı istek (varsayılan 4)")
    a = p.parse_args()
    ham = a.klasor / ("ham-sonuclar-deneme.jsonl" if a.deneme else "ham-sonuclar.jsonl")
    if not a.sadece_rapor:
        ham = calistir(a.klasor, a.deneme, a.paralel)
    rapor_uret(a.klasor, ham)


if __name__ == "__main__":
    main()
