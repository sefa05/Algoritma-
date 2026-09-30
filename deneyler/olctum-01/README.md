# Ölçtüm #1 — 100 Türkçe müşteri e-postası, 3 model

> ⚠️ **Veri seti sentetiktir.** E-postaları Claude, kurgusal bir genel e-ticaret mağazası ("Örnekmarket") için yazdı. Gerçek müşteri verisi yok. İçerikte bu açıkça söylenecek:
> "Veri seti: 100 sentetik e-posta, gerçek müşteri kalıplarından esinlenildi."

## Dosyalar

| Dosya | Ne işe yarar |
|---|---|
| `veri-seti-etiketli.csv` | 100 e-posta + **önerilen etiket** + zorluk bilgisi + not. `sefa_etiketi` sütunu senin kontrolün için boş. |
| `veri-seti-modele-giden.csv` | Yalnızca `id` ve `metin`. Modellere **bu dosya** verilir, etiketler sızmaz. |
| `sistem-istemi.md` | Üç modele aynen verilecek istem. |
| `sonuc-sablonu.csv` | Doğru etiket + 3 modelin cevabı + süreler. |

## Dağılım
- **Kategoriler:** 5 kategori × 20 e-posta.
- **Zor örnekler:** 17 tane.

| Zorluk türü | Adet |
|---|---|
| Yanıltıcı anahtar kelime | 6 |
| Çok kısa | 2 |
| Yazım hatası / Türkçe karakter yok | 2 |
| İroni | 2 |
| İade ile ödeme sınırı | 1 |
| Sipariş ile ödeme sınırı | 1 |
| Teknik ile iade sınırı | 1 |
| Karışık dil | 1 |
| Spam | 1 |
| Anlamsız mesaj | 1 |

## Etiketleme rehberi

| Etiket | Kapsam |
|---|---|
| `SIPARIS_DURUMU` | Kargo, teslimat, gecikme, adres değişikliği, **kargolanmamış** siparişin iptali, eksik gönderim |
| `IADE_DEGISIM` | İade veya değişim talebi ve süreci, iade kodu, **iadeye bağlı** para iadesi, müşterinin açıkça değişim istediği arızalar |
| `FATURA_ODEME` | Fatura, taksit, ödeme adımı hataları, mükerrer veya yanlış çekim, bloke tutar, kupon ve puan ile ücret farkı |
| `TEKNIK_SORUN` | Ürün arızası, kurulum, kullanım, ödeme adımı **dışındaki** site ve uygulama hataları |
| `SIKAYET_DIGER` | Hizmet şikâyeti, teşekkür, iş başvurusu, iş birliği, KVKK, bülten, spam, sınıflandırılamayan mesajlar |

**Sınır kuralları:**
1. **Müşterinin şirketten ne yapmasını istediğine** bak, geçen kelimelere değil.
2. **Arıza:** Açıkça iade veya değişim istiyorsa `IADE_DEGISIM`. Yardım veya tamir istiyorsa `TEKNIK_SORUN`. Talep yoksa, yalnızca arıza bildiriyorsa `TEKNIK_SORUN`.
3. **Para:** İade sürecine bağlıysa `IADE_DEGISIM`. Çekim hatası, bloke tutar veya sipariş oluşmadan düşen para ise `FATURA_ODEME`.
4. **Bilgi yoksa:** Hiçbir kategoriye girmiyorsa `SIKAYET_DIGER`.

## Yapılacaklar (Cuma 2 Ekim, ~30 dk)
1. **Etiketleri kontrol et.** `veri-seti-etiketli.csv` dosyasını aç, önerilen etiketleri gözden geçir. Katılmadığın satırda `sefa_etiketi` sütununu doldur. **Nihai doğru cevap senin etiketin.**
2. **Modelleri seç.**
   - Model A: büyük / pahalı
   - Model B: küçük / ucuz
   - Model C: farklı sağlayıcı ya da açık kaynak
3. **Veri setini değiştirmek istersen** e-posta ekleyip çıkarabilirsin. Sonra bana haber ver, dağılım tablosunu güncellerim.

## Deneyi çalıştırma (Pzt–Sal)

### 1. Kurulum (bir kez)
```bash
pip install anthropic openai
export ANTHROPIC_API_KEY=...      # ya da: ant auth login
export OPENAI_API_KEY=...         # yalnızca Model C OpenAI uyumlu bir sağlayıcıysa
```

### 2. `modeller.json` dosyasını doldur
| Model | Varsayılan | Değiştirebilirsin |
|---|---|---|
| **A** (büyük) | Claude Opus 5.5, effort `low` | Claude Sonnet 5.5 (`claude-sonnet-5-5`, $2 / $10) |
| **B** (küçük / ucuz) | Claude Haiku 4.5, sıcaklık 0 | — |
| **C** (farklı sağlayıcı) | **Boş.** `model`, `etiket`, fiyatlar ve gerekiyorsa `base_url` alanlarını doldur. OpenAI, OpenRouter ve yerel vLLM/Ollama ile çalışır. | — |

- `usd_try.kur` ve `tarih` alanlarına deney günkü kuru yaz. Rapor maliyeti TL olarak verir.
- **Model C'nin fiyatı:** Sağlayıcının güncel fiyat sayfasından al. Claude fiyatları 25 Eylül 2026 liste fiyatlarıdır.

> ⚠️ **Protokol notu:** Yeni Claude modellerinde (Opus 5.5, Sonnet 5.5) **sıcaklık ayarı yok**, gönderilirse istek hata verir. Opus 5.5'te **düşünme kapatılamaz**, yalnızca `effort` ile azaltılır. Bu yüzden "sıcaklık 0" kuralı yalnızca destekleyen modellere uygulanır. İçerikte tek cümleyle söyle: *"Her modeli sağlayıcının izin verdiği en tutarlı ayarla çalıştırdım."* Bu fark, videoda ilginç bir detay da olabilir.

### 3. Önce deneme, sonra gerçek çalıştırma
```bash
python deneyler/calistir.py deneyler/olctum-01 --deneme   # API çağırmaz, sahte cevaplarla boru hattını test eder
python deneyler/calistir.py deneyler/olctum-01            # gerçek deney: 3 × 100 istek
```
- **Yarıda kalırsa** aynı komutu tekrar çalıştır. Biten istekleri atlar, kaldığı yerden devam eder.
- **Ekran kaydı** için gerçek çalıştırmayı terminalde canlı göster. İlerleme satırları videoda sayaç görevi görür.

### 4. Çıktılar
| Dosya | İçerik |
|---|---|
| `rapor.md` | Doğruluk · zor örneklerde doğruluk · format hatası · reddetme · 100 e-posta maliyeti (TL) · ortalama süre · kategori bazında tablo · en çok karıştırılan çiftler |
| `sonuc-sablonu.csv` | Her e-posta için 3 modelin cevabı |
| `ham-sonuclar.jsonl` | Ham kayıt: cevap, token, süre, durma nedeni |

**Teslim:** `rapor.md` dosyasını bu sohbete gönder ya da depoya ekle. H1 paketindeki yer tutucuları ben doldururum.

**Ölçüm kuralları:**
- **Geçersiz cevap:** Etiket dışında bir şey döndüren cevap **yanlış** sayılır ve ayrıca "format hatası" olarak raporlanır.
- **Reddetme:** Model bir e-postayı reddederse (refusal) bu da ayrı raporlanır. Reddedilen isteği otomatik olarak başka bir modele yönlendirme özelliği (fallback) **bilinçli olarak kapalı**; açık olsaydı ölçüm başka bir modelle karışırdı.
- **Maliyet:** Düşünme token'ları çıktı token'ına dahil olduğu için Opus 5.5'in gerçek maliyeti ölçülür.
