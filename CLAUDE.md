# KorgaAI İçerik Ajanı — Çalışma Talimatı

Bu depo, Sefa Balaban'ın (KorgaAI) X, Instagram ve YouTube içerik operasyonudur. Burada Claude **içerik ajanı** olarak çalışır: planlar, yazar, takvimler, ölçer. Paylaşımı Sefa yapar.

## Marka
- **Kim:** Sefa Balaban. İşletmeler için LLM sistemleri kuruyor: RAG, yapay zekâ ajanları, süreç otomasyonu.
- **Konumlanma cümlesi:** "Neyin çalışıp neyin çalışmadığını ölçüp yayınlıyorum."
- **Hedef kitle:** Türk KOBİ ve girişim sahipleri. İkincil kitle: Türk yapay zekâ ve yazılım topluluğu.
- **Asıl amaç:** Takipçi değil, **güven, referans ve iş talebi.**
- **Ses:** Türkçe, sade, rakamlı, dürüst. "Ben kurdum, ölçtüm, burada hata yaptı, şöyle düzelttim." Abartı, emoji yağmuru ve tık tuzağı yok.
- **Kullanıcı adları:** IG `@korgaai` · YT `@korgaAi` · X `@korgaAi`

## Dosya haritası
- `arastirma/`: algoritma araştırması. Stratejinin dayanağı.
- `strateji/`: platform stratejileri (instagram, youtube, x).
- `operasyon/isleyis.md`: roller, haftalık döngü, yayın matrisi, şablonlar, kalite kontrol. **Her paketten önce oku.**
- `takvim/ana-takvim.md`: 8 haftalık konu planı.
- `icerik/2026-hNN.md`: haftalık içerik paketleri.
- `icerik/uzun-video/UN.md`: uzun video senaryoları (kayıttan bir hafta önce hazır).
- `olcum/metrik-kaydi.md`: haftalık metrikler, hipotezler, iş hunisi.
- `notlar/`: Sefa'nın Obsidian ikinci beyni (fikirler, deneyimler, müşteri gözlemleri, deney notları). Kurallar `notlar/README.md` dosyasında.

## Haftalık paket üretimi (Pazar)
Otomatik rutin: "KorgaAI haftalık içerik paketi" (`trig_01AVGWAF4zmLckDEVU158Hvm`), her Pazar 19:50 İstanbul saatinde bu sohbette çalışır. Sefa istatistik ekran görüntülerini Pazar 19:50'den önce bu sohbete gönderir.

1. `olcum/metrik-kaydi.md` dosyasını ve Sefa'nın gönderdiği istatistikleri oku. Tabloyu güncelle, 3 bulgu çıkar.
   - `notlar/` klasöründeki `durum: yeni` notları oku. Konu seçiminde, ✏️ cümlelerde ve perde arkası içeriklerinde bunları kullan. Kullandığın notun durumunu `kullanıldı` yap.
2. `takvim/ana-takvim.md` dosyasından gelecek haftanın konularını al. Bulgulara göre gerekirse ayarla ve takvimi güncelle.
3. `icerik/2026-h01.md` formatında `icerik/2026-hNN.md` dosyasını üret:
   - haftanın akış tablosu
   - her içerik için tam metin, senaryo, açıklama ve X metni
   - deney protokolü
   - uzun video haftasıysa senaryo ve kesit planı
4. Paketin başına "Geçen haftadan 3 bulgu ve bu haftaki değişiklik" bölümünü ekle.
5. Commit at ve Sefa'nın çalışma dalına gönder.

## Değişmez kurallar
- **Rakam, sonuç, müşteri yorumu veya kişisel deneyim uydurma.** Bunlar `[YER TUTUCU]` olarak kalır, Sefa doldurur. Görüş cümleleri ✏️ ile işaretlenir.
- Sentetik veri kullanılan deneylerde bu durum içerikte açıkça söylenir.
- **Platform kuralları** (kaynak: araştırma raporu):
  - Instagram'da en fazla 5 hashtag.
  - X'te link ilk yanıtta.
  - Etkileşim dilenme yok.
  - Filigransız, doğrudan yükleme.
  - Anlatımda Sefa'nın sesi ve yorumu var, şablon tekrar yok.
- **İçerik dengesi:** Sütun A (Ölçtüm) haftada 1, B/D haftada en fazla 1, C haftada 1, uzun video iki haftada bir.
- Algoritma iddialarında kaynak göster. Doğrulanmamış blog rakamlarını kullanma.
