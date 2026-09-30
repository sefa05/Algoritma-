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
1. `veri-seti-modele-giden.csv` dosyasındaki her e-postayı `sistem-istemi.md` ile üç modele gönder.
   - **Ayarlar:** Sıcaklık 0. Tek e-posta = tek istek.
2. **Kaydet:**
   - Her cevabı `sonuc-sablonu.csv` dosyasına yaz.
   - Yanıt süresini ölç.
   - Toplam giriş ve çıkış token'ını not al: maliyet = token × fiyat, TL'ye çevir, kur ve tarihi de not et.
3. **Geçersiz cevaplar:** Model etiket dışında bir şey döndürürse **yanlış** say. Bunu ayrıca "format hatası" olarak da say, içerikte ilginç bir bulgu olabilir.
4. **Ekran kaydı:** Deney çalışırken ekran kaydı al. Reels'in 10–30. saniyeleri buradan çıkacak.
5. **Teslim:** Doldurulmuş `sonuc-sablonu.csv` dosyasını ve token ve süre notlarını bu sohbete gönder ya da depoya ekle. Doğruluğu, kategori bazında hata tablosunu, en çok karıştırılan çiftleri ve zor örneklerdeki başarıyı ben hesaplarım, ardından H1 paketindeki yer tutucuları doldururum.
