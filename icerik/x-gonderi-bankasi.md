# X Gönderi Bankası — @korgaAi

**Ne için:** Haftalık paketteki X gönderileri ana plandır. Bu banka şu boşlukları doldurur:
- paketin boş bıraktığı günler
- ani bir fikir gerektiğinde ya da bir gündem anında
- günde 2. özgün gönderi atmak istediğinde (en fazla 2)

**Kurallar:**
- Her gönderi **≤ 280 karakter**. Premium olmayan hesapta da sığar.
- Linkler ilk yanıta konur.
- `[YER TUTUCU]` olan gönderiler doldurulmadan atılmaz.
- ✏️ işaretli gönderiler görüş içerir. Kendi sesine uydur, katılmıyorsan atma.
- Kullandığın gönderinin yanına `✅ tarih` yaz. Pazar rutini kullanılmış gönderileri bankadan çıkarır, yerine yenisini ekler.

**Saat:**
- Önerilen saatler 09:00 veya 21:00.
- Paylaştıktan sonraki **2 saat** çevrimiçi ol. X yeni gönderiyi bu sürede test ediyor.

---

## 1. Mini ders / kontrol listesi
Bu gönderiler en çok kaydedilir ve paylaşılır. X kodunda en yüksek ağırlık "linki kopyala"da (20). Ağırlığın neye uygulandığı araştırma raporu 2.2'de.

**K1** ✏️
```
Bir işletmeye yapay zekâ asistanı kurarken ilk hafta modele değil şunlara bakıyorum:

1) En sık gelen 20 soru ne?
2) Cevapları şu an kim, nereden veriyor?
3) Yanlış cevabın bedeli ne?

Bu üçü netleşmeden model seçmek erken.
```

**K2**
```
RAG'i tek cümleyle anlatayım: modele, sorudan önce ilgili belgeleri bulup okutmak.

İşe yaradığı yer: cevabı belgelerinizde olan sorular.
Yaramadığı yer: belgede olmayan, yorum isteyen sorular.

İkincisinde model yine uydurabilir. Test etmeden canlıya almayın.
```

**K3**
```
"Yapay zekâ ajanı" çoğu zaman şu demek: bir model + birkaç araç (e-posta okumak, tabloya yazmak, API çağırmak) + bir döngü.

Model hangi aracı ne zaman kullanacağına kendisi karar veriyor.

Gücü de riski de burada.
```

**K4**
```
Bir yapay zekâ sistemini ölçmenin en ucuz yolu: doğru cevaplarıyla birlikte 50 gerçek örnek.

Her değişiklikten sonra aynı 50 örneği tekrar çalıştır. Doğruluk düştüyse değişikliği geri al.

Bunu yapmayan proje hissiyatla yönetiliyor demektir.
```

**K5**
```
Bir yapay zekâ botunun aylık maliyetinde 4 kalem var:

• Model ücreti (token)
• Altyapı (sunucu, veritabanı)
• Bakım (istem ve veri güncellemesi)
• Hata maliyeti (yanlış cevabın sana bedeli)

Çoğu hesapta sadece ilki yazıyor.
```

**K6** ✏️
```
Her yapay zekâ akışında sorduğum soru: hangi adımda bir insan onay vermeli?

Benim kuralım: geri alınamayan bir işlem varsa (ödeme, müşteriye giden mesaj, silme) önce insan onayı. Gerisi otomatiğe kalabilir.
```

**K7**: Ölçtüm #1'den önceki gün (Perşembe) için uygun
```
Her iş için en büyük modele gerek yok.

Sınıflandırma, etiketleme, kısa özet gibi işlerde küçük modeller çoğu zaman yeterli ve çok daha ucuz.

Ama "çoğu zaman" yetmez. Kendi verinle ölçmeden karar verme.

Yarın bunu ölçüyorum.
```

---

## 2. Görüş ✏️
Konumlanmanı netleştirir. Karşı görüş gelirse sohbet açılır.

**G1** ✏️
```
Popüler görüş: "Yapay zekâ müşteri hizmetlerini tamamen devralacak."

Benim gördüğüm: en iyi sonucu, basit soruları otomatiğe alıp zor olanları insana daha hızlı ulaştıran sistemler veriyor.

Hedef insansız destek değil, beklemesiz destek.
```

**G2**
```
"Hangi model en iyisi?" sorusunun tek dürüst cevabı: hangi iş için?

Genel benchmark'lar senin müşteri e-postanı, senin faturanı, senin Türkçeni ölçmüyor.

50 örnekle kendi testini yap.
```

**G3** ✏️
```
Demoda çalışan yapay zekâ ile işletmede çalışan yapay zekâ arasındaki fark: kirli veri.

Yazım hatalı e-posta, eğri taranmış PDF, yarım doldurulmuş form.

Asıl test bunlarla başlar.
```

**G4** ✏️
```
Bir yapay zekâ projesinin başarısını "ne kadar akıllı" sorusuyla değil, "ayda kaç saat geri kazandırdı" sorusuyla ölçüyorum.
```

---

## 3. Perde arkası
Güveni en çok bunlar kurar, çünkü süreci ve hataları gösterir.

**P1**: Doğrulanmış bilgi (Anthropic dokümantasyonu, Eylül 2026)
```
Ölçtüm #1'i hazırlarken öğrendiğim şey: yeni Claude modellerinde (Opus 5.5, Sonnet 5.5) temperature ayarı yok, gönderince istek hata veriyor. Opus 5.5'te düşünme modu da kapatılamıyor.

"Hepsini sıcaklık 0'da test ettim" artık her model için mümkün değil.
```

**P2**
```
Veri setine bilerek zor örnekler koydum: ironi ("Harika ürün, 2 günde bozuldu 👏"), tek kelimelik mesajlar, Türkçe karaktersiz yazılar.

Kolay örnekte modellerin hepsi iyi. Fark zor örnekte çıkıyor.
```

**P3**: U1 kaydından önce (Cmt 10 Ekim)
```
Bu hafta sonu kaydedeceğim video: bir şirketin dokümanlarına RAG kurup 50 soruyla test edeceğim.

10 sorunun cevabı dokümanda yok. Model "bilmiyorum" mu diyecek, yoksa uyduracak mı?

Sence kaçında uydurur?
```

**P4**: Şablon `[YER TUTUCU]`
```
Bugün [NE KURDUM]. İlk denemede [SORUN].

Sebebi: [NEDEN].
Çözüm: [ÇÖZÜM].

[ÇIKARIM, tek cümle]
```

**P5**: Şablon `[YER TUTUCU]`
```
[GÖREV] için aylık maliyeti hesapladım:

• Ayda [N] istek
• İstek başına ~[X] token
• Model: [MODEL]

Toplam: ayda ~[TL] TL.

Aynı işe bir çalışanın ayırdığı süre: ayda [SAAT] saat.
```

---

## 4. Sohbet başlatan
Gerçek sorulardır, etkileşim dilenme değildir. Gelen cevaplar sonraki Ölçtüm konularına kaynak olur.

**S1**
```
İşletme sahiplerine soru: haftada en çok vaktinizi alan, tekrar eden iş hangisi?

Sonraki ölçümlerimi bu cevaplardan seçeceğim.
```

**S2**
```
Yapay zekâyı işinde deneyip vazgeçen oldu mu? Neden vazgeçtiğini merak ediyorum.

Başarısız denemeler bana başarılılardan daha çok şey öğretiyor.
```

---

## 5. Diziler
Haftada 1–2 tane. Paketteki dizilere ek olarak kullanılabilir.

### T1: Ajan ne zaman gereksiz? (6 gönderi)
```
1/ "Yapay zekâ ajanı" bu yılın en çok satılan kelimesi. Ama çoğu işletmenin ajana ihtiyacı yok.

Ne zaman gerekir, ne zaman gereksiz? 🧵
```
```
2/ Önce fark:

Otomasyon: adımlar önceden belli. "Fatura gelince tabloya yaz."
Ajan: adımlara model karar veriyor. "Müşterinin derdini anla, gerekeni yap."
```
```
3/ Adımlar her seferinde aynıysa otomasyon yeterli. Daha ucuz, daha hızlı, daha öngörülebilir.

Ajan ancak her vaka farklı bir yol gerektiriyorsa değer katar.
```
```
4/ Ajanın gizli maliyeti: model her adımda karar verdiği için her adımda hata yapabilir.

5 adımlık bir işte her adım %95 doğruysa uçtan uca doğruluk yaklaşık %77'ye düşer.
```
```
5/ Benim sıram:

1) Süreç kural ile çözülüyor mu? → Otomasyon
2) Tek bir karar noktası mı var? → Otomasyon + tek model çağrısı
3) Her vaka farklı mı? → Ajan, insan onayıyla
```
```
6/ Kısacası: ajan bir araç, hedef değil.

Önce en basit çözümü dene, gerçekten yetmediğini ölç, sonra karmaşıklaştır.
```
> 4/'teki hesap: 0,95⁵ ≈ 0,774. Adımların bağımsız olduğu varsayımıyla basit bir örnek, ölçüm değil.

### T2: Canlıya almadan önce yaptığım test (5 gönderi) ✏️
```
1/ Bir yapay zekâ sistemini müşteriye teslim etmeden önce yaptığım test, adım adım 🧵
```
```
2/ Gerçek verilerden 50–100 örnek topluyorum. Kolay olanları değil: yazım hatalı, iki konulu, eksik bilgili olanları da.
```
```
3/ Her örneğin doğru cevabını önceden yazıyorum. Mümkünse işi şu an yapan kişiyle birlikte.
```
```
4/ Sistemi çalıştırıp üç şeye bakıyorum: kaç doğru, kaç lira, kaç saniye. Sonra yanlışları tek tek okuyorum. Asıl ders orada.
```
```
5/ Sonra bir eşik koyuyorum: bu oranın altına düşerse sistem durur ve insana devreder.

Ölçemediğin sistemi teslim edemezsin.
```

---

## 6. Yanıt kalıpları (`Hedef` listesi, günde 10)
X'te ağ burada kurulur. Karşılıklı takipleştiğin birinden gelen yanıtın ağırlığı +15. "Harika paylaşım" gibi boş yanıtlar yok, ilk yanıtta satış teklifi yok, link yok.

| Durum | Kalıp |
|---|---|
| Katılıyorsun | "Katılıyorum. Benim [DENEYİM/ÖLÇÜM] örneğimde [SOMUT GÖZLEM]. Sizde [SORU]?" |
| Kısmen katılmıyorsun | "Bir noktada farklı düşünüyorum: [NOKTA]. Çünkü [GEREKÇE veya ÖRNEK]. Siz bunu hangi ölçekte denediniz?" |
| İşletme sahibi bir sorun anlatıyor | "Burada önce şuna bakardım: [SORU]. Cevap [A] ise [ÖNERİ 1], [B] ise [ÖNERİ 2]." |
| Geliştirici teknik bir şey paylaşıyor | "Benzerini [YÖNTEM] ile çözdüm, [SONUÇ]. Sizde darboğaz [TAHMİN] mi?" |
| Biri yeni bir model veya araç duyuruyor | "Bunu [İŞ GÖREVİ] üzerinde denemek istiyorum. Türkçe performansına dair bir gözlemin var mı?" |
| Kendi gönderine soru geldi | Soruyu doğrudan cevapla. Konu işine benziyorsa bir cümle ekle: "Sizdeki duruma özel bakmamı istersen DM açık." |
| Eleştiri geldi | "Haklı bir nokta. Bu testin sınırı: [SINIR]. Bir sonraki ölçümde [DEĞİŞİKLİK] ile tekrar deneyeceğim." |
| Veri seti istendi | "Veri setini şimdilik paylaşmıyorum ama yöntemi yazdım. Kendi verinle aynısını kurmak istersen DM'den yaz." |

---

## 7. Alıntılayarak yorum (haftada 2–3)
Sadece gerçek bir katkın varsa yap. Kalıp:
```
[Gönderinin iddiası, tek cümle] doğru, ama işletme tarafında eksik bir parça var: [EKSİK PARÇA].

[Kendi gözlemin veya ölçümün]
```
