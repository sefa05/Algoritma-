# İşleyiş — KorgaAI İçerik Operasyonu

> ✍️ **Şu an sadece metin modu (4 Ekim 2026'dan).** Aşağıdaki çekim, montaj, Reels ve deney adımları beklemede. Geçerli döngü:
> - **Pazar:** Ajan paketi üretir.
> - **Pazartesi:** Sefa onaylar (15 dk).
> - **Her gün:** Paylaşım (5 dk) + yanıtlar (15 dk).
>
> Yayın günleri ve saatleri için `takvim/ana-takvim.md`. X kuralları için bölüm 5.1b.

Bu dosya sistemin nasıl döndüğünü anlatır: kim ne yapar, ne zaman yapar, içerik nereden nereye gider.

---

## 1. Roller

| | **Sefa** | **Ajan (Claude)** |
|---|---|---|
| **Karar** | Konu onayı, fikir ve görüş cümlelerini kendi sesine uydurma | Konu önerisi, önceliklendirme |
| **Üretim** | Deneyi çalıştırma, çekim, ses kaydı, montaj | Senaryo, ekran yazıları, açıklamalar, carousel metinleri, X gönderileri, deney protokolü |
| **Yayın** | Paylaşma ya da zamanlama (Meta Business Suite, YouTube Studio, X) | Yayın takvimi: gün, saat, platform |
| **Etkileşim** | Yanıtlar, yorumlar, DM'ler (günde 20 dk) | Hedef hesap kategorileri, yanıt kalıpları |
| **Ölçüm** | Pazar günü istatistik ekran görüntülerini gönderme | Analiz, `olcum/metrik-kaydi.md` güncellemesi, gelecek haftanın ayarı |

> **Ajanın değişmez kuralı:** Rakam uydurmaz. Deney sonuçları, müşteri yorumları ve "şunu yaşadım" türü deneyimler Sefa'dan gelir. Paket içinde bunlar `[YER TUTUCU]` olarak işaretlenir.

---

## 2. Haftalık döngü

| Gün | Sefa | Ajan |
|---|---|---|
| **Pazar akşamı** | Instagram, YouTube ve X istatistik ekran görüntülerini gönderir (5 dk) | Geçen haftayı analiz eder. **Gelecek haftanın paketini** üretir: `icerik/2026-hNN.md` |
| **Pazartesi** | Paketi okur, onaylar veya düzeltir (15 dk). Deneyleri çalıştırır. | Düzeltmeleri işler |
| **Salı–Çarşamba** | Çekim ve kayıt. Tek oturumda o haftanın bütün Reels ve Shorts'ları. | Deney sonuçları gelince yer tutucuları doldurur, son metinleri hazırlar |
| **Çarşamba** | Montaj. Yayınları platformların kendi araçlarıyla zamanlar. | — |
| **Her gün** | Etkileşim rutini (aşağıda) | — |
| **Uzun video haftası** | Hafta sonu kayıt, hafta içi montaj | Senaryo ve bölüm planı bir hafta önceden hazır olur |

---

## 3. Standart yayın matrisi

Saatler İstanbul saatine göre ve **başlangıç hipotezi**. 4 hafta sonunda istatistiklere göre güncellenecek.

| Gün | Instagram | YouTube | X |
|---|---|---|---|
| **Pzt** | Reels, B veya D sütunu (20:30) | Aynı içerik Shorts olarak (20:30) | Tek gönderi (09:00) |
| **Sal** | Hikâye: perde arkası | — | Tek gönderi (21:00) |
| **Çar** | **Carousel**, C sütunu (12:30) | — | Carousel'in dizi hali (21:00) |
| **Per** | Hikâye: uzun videonun tanıtımı | **Uzun video** (19:00, iki haftada bir) | Uzun videodan kesit, link ilk yanıtta (19:30) |
| **Cum** | **Reels: Ölçtüm #N** (20:30) | Ölçtüm Shorts'u (seri) (20:30) | Ölçüm sonucu, tablo ve video (21:00) |
| **Cmt** | Hikâye: anket veya soru-cevap | — | Hafif gönderi veya perde arkası |
| **Paz** | — | — | — (haftalık değerlendirme) |

**Hafta toplamı:** Instagram 3 akış gönderisi ve 3–4 gün hikâye. YouTube 2–3 Shorts ve iki haftada bir uzun video. X 5–6 tek gönderi ve 1 dizi.

### Günlük etkileşim rutini (20 dk)
1. **X:** `Hedef` listesinden 10 anlamlı yanıt yaz. Kendi gönderine gelen her yanıta ilk 2 saatte cevap ver.
2. **Instagram:** Hedef sektör hesaplarına 5 anlamlı yorum yaz. Gelen yorum ve DM'lere cevap ver.
3. **YouTube:** Gelen her yoruma cevap ver. İlk hafta en iyi yorumu sabitle.

---

## 4. Tek içerikten dört platforma

```
DENEY veya KURULUM (Sefa)
      │
      ├─► Uzun video (YouTube) ──► 3–5 kesit ──► Shorts + Reels + X video
      ├─► Ölçtüm kısa videosu ─────────────► Reels + Shorts (seri) + X
      ├─► Sonuç tablosu ────────────────────► Carousel + X dizisi
      └─► Vaka özeti ───────────────────────► Portfolyo + Öne çıkan hikâyeler
```

**Dağıtım kuralları:**
- Her platforma **ayrı ve doğrudan** yükle. Başka platformun filigranı olmasın, CapCut ve TikTok logosu da olmasın.
- Açıklama metni platforma göre değişir. Instagram: kısa ve eyleme çağıran. YouTube: aranabilir. X: sohbet başlatan.
- Link: X'te ilk yanıtta, Instagram'da profilde, YouTube'da açıklamada ve sabit yorumda.

---

## 5. Üretim şablonları

### 5.1 Reels / Shorts (30–60 sn)
```
BAŞLIK (iç kullanım):
SÜTUN: A Ölçtüm | B Demo | D Görsel demo
0–2 sn   EKRAN YAZISI: [sonuç veya rakam]    SES: [tek cümle]
2–10 sn  Problem:
10–40 sn Nasıl (ekran kaydı): [kurulum adımları, hata anı, düzeltme]
40–55 sn Sonuç (rakam) + 1 ders:
KAPANIŞ: [bağlama uygun eylem çağrısı]
KAPAK: [3 kelime + rakam]
AÇIKLAMA (IG):
BAŞLIK (YT Shorts):
HASHTAG (en fazla 5):
X METNİ:
```

### 5.1b X gönderisi
```
Her gönderi ≤ 280 karakter (emoji 2 sayılır). Link ilk yanıtta.
Boş gün veya ek gönderi için: icerik/x-gonderi-bankasi.md
```

### 5.2 Carousel (8–12 slayt)
```
1 Kapak: sonuç vaat eden başlık (en fazla 8 kelime)
2–N Her slayt tek fikir, en fazla 25 kelime
Son-1 Özet
Son Eylem çağrısı + imza (Sefa Balaban | KorgaAI)
```

### 5.3 Uzun video (12–20 dk)
```
Açılış 0:00–0:30 · Problem · Kurulum · Başarısızlık anı · Ölçüm tablosu · Ders + eylem çağrısı
Başlık (aranabilir + rakam) · Küçük resim (yüz + rakam + en fazla 3 kelime) · Bölümler · Açıklama · Sabit yorum
Kesit planı: hangi dakikadan hangi Shorts çıkacak
```

### 5.4 Deney protokolü (her Ölçtüm için)
```
Görev · Veri seti (kaynak, adet, gerçek mi sentetik mi, anonimleştirme) · Doğru cevaplar (kim etiketledi)
Karşılaştırılanlar (model veya yaklaşım) · Sabitler (aynı istem; sıcaklık 0 yalnızca destekleyen modellerde)
Metrikler: doğruluk %, 100 iş başına maliyet (TL), ortalama süre (sn), hata türleri
Kayıt: ekran kaydı, sonuç tablosu (CSV), 3 ilginç hata örneği
Şeffaflık notu (içerikte söylenecek): veri seti sentetik mi, kaç örnek, sınırlamalar
```

---

## 6. Kalite kontrol (yayından önce 30 sn)

- [ ] İlk 2 saniyede sonuç veya rakam var mı?
- [ ] Anlatıda **ben** var mı? ("Model yaptı" değil, "ben kurdum, ölçtüm")
- [ ] Konu açıkça söyleniyor mu? (işletme, otomasyon, RAG, ajan)
- [ ] Rakamlar gerçek deneyden mi geliyor? Veri seti sentetikse söylendi mi?
- [ ] Filigran yok, en fazla 5 hashtag, link doğru yerde mi?
- [ ] Başlıkta vaat edilen şey içerikte var mı?
