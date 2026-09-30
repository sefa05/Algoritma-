# notlar/ — İkinci Beyin (Obsidian) Köprüsü

Bu klasör, Sefa'nın Obsidian kasasından (vault) içerik ajanına akan notların yeri. Ajan her Pazar buradaki yeni notları okur ve konu seçimine, ✏️ görüş cümlelerine ve perde arkası içeriklerine kaynak olarak kullanır.

## Bağlantı (Sefa yapar)
1. **Ayrı bir klasör olarak bağla:** Obsidian kasasındaki içerik klasörünü bu depodaki `notlar/` klasörü olarak bağla. Yöntemlerden biri:
   - Depoyu doğrudan kasanın içine klonla ve bu klasörü kullan, **ya da**
   - **Obsidian Git** eklentisiyle kasanın yalnızca bu klasörünü bu depoya senkronla.
2. **Otomatik senkron:** Obsidian Git ayarı "Auto commit-and-sync interval" = 60 dk. Dal: `ccr-3c57d9b4-54b9k2`.
3. ⚠️ **Gizlilik:**
   - Müşteri adı, telefon, fiyat teklifi, sözleşme detayı gibi hassas bilgileri **anonim** yaz. Örneğin: "İzmir'de bir diş kliniği".
   - Depo herkese açıksa kişisel notları bu klasöre koyma. Yalnızca içerik amaçlı notlar gelsin.

## Klasör yapısı
```
notlar/
├── fikirler/      Hızlı içerik fikirleri, tek satır bile olur
├── deneyimler/    "Kurarken şunu yaşadım" türü gerçek deneyimler. ✏️ cümlelerin kaynağı.
├── musteri/       Anonim müşteri gözlemleri: sorunlar, sorular, itirazlar
├── deneyler/      Ölçtüm deney notları ve ham sonuçlar
└── _sablon.md     Not şablonu
```

## Ajanın kullanım kuralları
- Notlardaki deneyim ve rakamlar içerikte **aynen** kullanılır. Ajan bunları abartmaz, genellemez.
- `yayin: hayır` etiketli notlar yalnızca bağlam içindir, içerikte alıntılanmaz.
- Bir not içeriğe dönüştüğünde ajan notun `durum` alanını `kullanıldı` yapar ve hangi pakete girdiğini yazar.
