# X, Instagram ve YouTube Algoritmaları — Eylül 2026 Araştırma Raporu

**Hazırlayan:** KorgaAI (Sefa Balaban) için · **Tarih:** 30 Eylül 2026
**Amaç:** Üç platformun güncel sıralama mantığını anlamak; ardından güven ve referans odaklı bir strateji kurmak.

---

## 0. Kısa özet

1. **Üç platform da artık aynı şeyi ödüllendiriyor: özgün içerik.** Instagram başkasının içeriğini paylaşan hesapları önerilerden çıkarıyor (Nisan 2026). X, çalınan içeriğin gelirini asıl sahibine veriyor (Temmuz–Ağustos 2026). YouTube şablon ve seri üretim içeriği para kazanmadan çıkarıyor (Temmuz 2026).
2. **En güçlü sinyal "paylaşım".** X'in kodunda "linki kopyala" ağırlığı 20, beğeni ağırlığı 0,5. Instagram'da Mosseri'ye göre yabancılara ulaşmanın bir numaralı sinyali DM ile gönderim.
3. **Olumsuz geri bildirim çok pahalı.** X'te "ilgilenmiyorum" −47,5, "sessize al" −58,8, "şikâyet" −234 ağırlıkla sayılıyor. Tık tuzağı kısa vadede izlenme getirse de uzun vadede erişimi keser.
4. **X, küçük hesaplara resmî bir test penceresi açıyor.** 50 bin takipçinin altındaki hesapların yeni ve özgün gönderileri, ilk 2 saat ve ilk 200 gösterim boyunca akışta yukarı taşınarak test ediliyor. Seçimde erken beğeni oranı belirleyici.
5. **X, karşılıklı takipleşmeyi güçlü biçimde öne çıkarıyor (Temmuz 2026).** Karşılıklı takipleştiğin kişilerin sana yanıt verme ihtimali 15 kat ek ağırlık alıyor. Küçük ama sıkı bir ağ, büyük ama pasif bir takipçi kitlesinden daha değerli.
6. **Kullanıcılar algoritmayı kendi cümleleriyle yönetmeye başladı.** Instagram'da "Your Algorithm", YouTube'da Gemini ile özel akışlar (Eylül 2026), X'te Grok ile konu takibi var. İçeriğin konusu ne kadar net söylenirse o kadar doğru kişiye gider.
7. **YouTube kalıcılığı ödüllendiriyor, Shorts ise tazeliği.** Uzun videolar arama ve öneriden yıllarca izlenebiliyor. Shorts'ta 30 günden eski içeriğin itilmesi belirgin biçimde düşmüş durumda (gözlem).

---

## 1. Yöntem ve güvenilirlik

| İşaret | Anlamı |
|---|---|
| ✅ **Doğrulandı** | Kaynak kodu doğrudan okundu ya da platform yöneticisi açıkça söyledi |
| 🟡 **Resmî duyuru** | Platform açıklaması, güvenilir basın (TechCrunch, Engadget, Social Media Today) üzerinden aktarıldı |
| ⚠️ **Gözlem / iddia** | Üretici topluluğu veya analistlerin gözlemi, resmî onayı yok |

- **X:** xAI'nin açık kaynak algoritma deposu (`github.com/xai-org/x-algorithm`, son güncelleme 30 Eylül 2026) doğrudan klonlandı. Ağırlıklar kodun kendisinden okundu.
- **Instagram ve YouTube:** Bu platformların sıralama kodu açık değil. Adam Mosseri'nin ve YouTube yöneticilerinin açıklamaları, güvenilir basın üzerinden derlendi.
- **Dışarıda bırakılanlar:** Pazarlama bloglarında dolaşan ama kaynağı olmayan rakamlar ("paylaşım beğeniden 3–5 kat değerli", "%40–60 özgünlük bonusu", "%70 görsel parmak izi eşiği", "yazarın yanıtladığı yanıt beğeniden 150 kat değerli" gibi) rapora alınmadı. Bunlardan biri kodla doğrudan çelişiyor; ayrıntısı 2.2'de.

---

## 2. X (Twitter)

### 2.1 Nasıl çalışıyor ✅
- **Ocak 2026'dan beri** X'in "Sana Özel" akışı tek bir Grok tabanlı transformer modeliyle (Phoenix) sıralanıyor. Eskiden elle yazılmış yüzlerce kural vardı.
- **Aday havuzu iki kaynaktan geliyor:**
  - Takip ettiğin hesapların son gönderileri (ağ içi, "Thunder")
  - Takip etmediğin hesaplardan benzerliğe göre bulunan gönderiler (ağ dışı, Phoenix erişimi ve SimClusters)
- **Puanlama:** Model her gönderi için yaklaşık 20 eylemin olasılığını tahmin ediyor. Sonra puanı şöyle hesaplıyor:

  **Nihai puan = Σ (ağırlık × bu kullanıcının o eylemi yapma olasılığı)**

### 2.2 Gerçek ağırlıklar (`home-mixer/params/param.rs`, 30 Eylül 2026) ✅

| Eylem | Ağırlık | Yorum |
|---|---:|---|
| Beğeni | 0,5 | Referans noktası |
| Yanıt | 5,0 | Beğeninin 10 katı |
| + Karşılıklı takipleşilen kişiden yanıt | +15,0 | Temmuz 2026 eklemesi. Toplam 20 |
| Alıntı | 5,0 | |
| Repost | 1,0 | Sanıldığından düşük |
| Paylaş (genel) | 2,0 | |
| DM ile paylaş | 5,0 | |
| **Linki kopyala** | **20,0** | En yüksek pozitif ağırlık |
| Yazarı takip et | 4,0 | |
| Tıklama | 0,3 | |
| Dış linke tıklama | 0,2 | Çok düşük |
| Profil tıklaması | 0,0 | |
| Tıklayıp okuma süresi | 0,4 | |
| Fotoğraf büyütme / video açma | 0,05 / 0,07 | |
| İlgilenmiyorum | −47,52 | |
| Engelle | −31,2 | |
| Sessize al | −58,8 | |
| Şikâyet et | −234,0 | |

> ⚠️ **Kodun kendi uyarısı:** Ağırlıklar ham sayılarla değil, tahmin edilen olasılıklarla çarpılıyor. Örneğin şikâyetin ağırlığı büyük, çünkü şikâyet beğeniden 1000 kat daha nadir. Bu yüzden "1 şikâyet 468 beğeniyi siler" gibi okumalar yanlış. Aynı nedenle bloglarda geçen "yazarın yanıtladığı yanıt beğeniden 150 kat değerli" iddiası da bu kodla uyuşmuyor.

**Pratikte:**
- İnsanların kaydedip başkasına gönderdiği, altında sohbet açtığı içerik kazanıyor.
- Beğeni tek başına zayıf bir sinyal.
- Dış link tıklaması neredeyse hiçbir şey kazandırmıyor.
- Karşılıklı takipleştiğin kişilerle konuşmak özellikle güçlü.

### 2.3 Küçük hesaplar için test penceresi ✅ (`scorers/author_cold_start.rs`)

Her akış yenilemesinde X, uygun gönderiler arasından birini seçip sıralamada yaklaşık **16. sıraya** taşıyor.

**Uygunluk koşulları:**
- Yanıt veya repost değil, **özgün gönderi**
- Yazarın **≤ 50.000 takipçisi** var
- Gönderi **≤ 2 saatlik**
- Ana akışta **< 200 gösterim** almış

**Seçim yöntemi:** Thompson örneklemesi. İlk gösterimlerdeki **beğeni oranı** yüksek olan gönderi daha çok seçiliyor. Başlangıç varsayımı yaklaşık %1,5 beğeni oranı.

**Senin için anlamı:**
1. Her özgün gönderi ilk 2 saatte bir sınavdan geçiyor. Yanıt ve repost bu pencereden yararlanamıyor.
2. İlk 200 gösterimdeki beğeni oranı kaderi belirliyor. İlk cümle, ilk görsel ve paylaşım saati kritik.
3. Günde çok sayıda vasat gönderi atmak yerine az ama güçlü özgün gönderi atmak daha mantıklı.

### 2.4 2026'nın diğer önemli değişiklikleri
- 🟡 **Karşılıklı takip güçlendirmesi (Temmuz 2026):**
  - 10 Temmuz'da A/B testi olarak başladı.
  - 13 Temmuz'da değer 20 olarak yaygınlaştırıldı.
  - 24 Temmuz'da 15'e düşürüldü. Gerekçe: Dünya Kupası sohbetleri akışlardan kayboldu.
  - Sonuç: yanıt bölümleri ve akışlar tanıdık kişilerle doluyor, ilgi alanı kümeleri daha kolay oluşuyor.
- 🟡 **Link cezası:**
  - X ürün başkanı Nikita Bier, linkli gönderilerin daha az erişim aldığını kabul etti. Tarayıcı açılınca kullanıcı beğenmeyi veya yanıtlamayı unutuyor, algoritma sinyal alamıyor.
  - Uygulama içi tarayıcı test ediliyor.
  - Koddaki link tıklama ağırlığı (0,2) de bunu destekliyor.
- 🟡 **Etkileşim dilenme yasağı (Temmuz 2026):** "Yanıt verenleri takip ederim" gibi talepleri 3 kez veya daha fazla yapan hesaplar gelir paylaşım programından çıkarılıyor ve askıya alınmak üzere politika ekibine yönlendiriliyor. Grok bunları otomatik yakalıyor.
- 🟡 **Özgün İçerik Ödülleri (Ağustos 2026):**
  - Eski gelir paylaşımının yerini aldı.
  - Kopyalanan içeriğin geliri asıl sahibine gidiyor. Tek bir dönemde 1,5 milyon çalıntı gönderi tespit edildi.
  - X kendi video düzenleyicisini ekledi ve platforma özel video içeriğini teşvik ediyor.
- ✅ **Premium ve mavi tik:** Açık kaynak sıralama kodunda (home-mixer) Premium veya onaylı hesaplara doğrudan puan artışı **bulamadım**. Başka katmanlarda (yanıt sıralaması, erişim) etkisi olabilir, ama "Premium alırsan patlarsın" iddiası bu koda dayanmıyor.

### 2.5 X için özet kurallar
- Linki ana gönderiye değil, ilk yanıta koy.
- Kaydedilip başkasına gönderilecek içerik üret: kontrol listeleri, ölçüm tabloları, "bunu bilmeden ajan kurma" türü dersler.
- Aynı niş içinde 50–100 hesapla **karşılıklı** ilişki kur: Türk yapay zekâ ve yazılım topluluğu ile hedef sektördeki kurucular.
- Paylaştıktan sonraki ilk 2 saat içinde gelen yanıtlara cevap ver ve konuşmayı açık tut.
- Asla etkileşim dilenme.

---

## 3. Instagram

### 3.1 Nasıl çalışıyor
- ✅ **Tek bir algoritma yok.** Akış, Reels, Hikâyeler ve Keşfet için ayrı sistemler var ve her biri sinyalleri farklı tartıyor.
- ✅ **En önemli üç sinyal (Mosseri):** izlenme süresi, görüntülenme başına beğeni ve görüntülenme başına **gönderim** (DM ile paylaşım).
- ✅ **Yeni kitleye ulaşmada en belirleyici sinyal gönderim.** Mosseri'ye göre DM ile gönderim, beğeni ve yorum sayısından da, izlenme süresinden de daha önemli.
- ✅ **İlk 2 saniye kritik.** İzleyici burada kalmazsa geri kalanı önemsiz.
- 🟡 **Toplam görüntülenme değil, oran önemli.** Etkileşim oranı toplam beğeni veya izlenme sayısından daha anlamlı.

### 3.2 Mosseri'nin 2026 için dört ilkesi 🟡
1. **Özgünlük:** Orijinal üreticiye öncelik, yeniden paylaşanlara değil.
2. **Tazelik:** Paylaşım zamanı sıralamada ciddi rol oynuyor.
3. **Küçük üreticilere fırsat:** Küçük üreticilerin içeriği, onları takip etmeyen kişilere de bilinçli olarak gösteriliyor.
4. **Model büyüklüğü:** Modeller büyütülüyor ve daha çok faktörü aynı anda değerlendiriyor.

### 3.3 Nisan 2026: özgün olmayan içeriğe ceza 🟡
- **Kural:** Başkasının içeriğini ciddi bir düzenleme yapmadan paylaşan hesaplar Reels, fotoğraf ve carousel dahil **tüm öneri yüzeylerinden çıkarılıyor.** Ölçüt: son 30 günde 10 veya daha fazla paylaşım.
- **Ceza süresi:** Son özgün olmayan paylaşımdan 30 gün sonra hesap önerilere tekrar uygun hale geliyor.
- **Takipçilere etkisi yok:** Ceza sadece takipçi olmayanlara erişimi kesiyor.
- **Senin durumun:** Kendi ürettiğin içerik olduğu için risk yok. Yine de başka bir hesabın videosunu tepki veya yorumla paylaşacaksan, üzerine gerçek bir katkı ekle.

### 3.4 Araçlar ve format değişiklikleri
- ✅ **Deneme Reels'i (Trial Reels):** Reels önce sadece takipçi olmayanlara gösterilir, sonucu görüp profile alıp almamaya karar verirsin. Mosseri deneme yapmak için bunu özellikle öneriyor.
- 🟡 **"Your Algorithm":** Kullanıcılar ilgi alanlarını elle seçiyor ve düzenliyor. Özellik Reels'ten Keşfet'e genişledi. Bu yüzden içeriğin konusu açıkça söylenmeli: ekrandaki yazıda, açıklamada ve sesli anlatımda.
- 🟡 **Hashtag sınırı:** Paylaşım başına en fazla 5 hashtag.
- 🟡 **Carousel:** 20 slayta kadar, slayt bazında ayrı açıklama eklenebiliyor (Haziran 2026).
- 🟡 **Profil ızgarası:** Artık dikey 3:4 önizleme kullanılıyor. Kapak görsellerini buna göre tasarla.

### 3.5 Mosseri'nin çürüttüğü efsaneler ✅
- **Hikâyede kendi gönderini paylaşmak** erişimi artırmaz.
- **Ne izlediğin**, içeriğinin kime gösterileceğini etkilemez. "Nişini beslemek için benzer içerik izle" tavsiyesi yanlış.
- **Uzun açıklama yazmak** erişimi artırmaz.

### 3.6 Instagram için özet kurallar
- DM ile gönderilecek içerik üret. Test sorusu: "Bunu işletme sahibi bir arkadaşıma atar mıyım?"
- İlk 2 saniyede sonucu ya da çatışmayı göster.
- Yeni formatları önce Deneme Reels'i ile dene.
- Hashtag en fazla 5 tane olsun, konu açıkça söylensin.

---

## 4. YouTube

### 4.1 Nasıl çalışıyor
- 🟡 **Temel ölçü izleyici memnuniyeti.** İzlenme süresi hâlâ önemli ama tek başına yetmiyor. YouTube anketlerle ve davranış sinyalleriyle izleyicinin "bu videoya harcadığım zamandan memnun muyum" duygusunu ölçüyor.
- 🟡 **Önerinin ilerleyişi:** İlk 24–48 saatte tıklama oranı, izleyici tutma ve memnuniyet güçlüyse video sonraki 7–14 gün içinde daha geniş kitlelere açılıyor.
- 🟡 **Shorts ve uzun videonun önerileri ayrı.** Kötü giden Shorts uzun videoları aşağı çekmiyor. İzleyicinin hangi formatı tercih ettiği de hesaba katılıyor.
- ⚠️ **Shorts'ta tazelik ön planda.** Eylül 2025'ten beri pek çok kanalda 30 günden eski Shorts'un izlenmesi sert biçimde düştü ("the flattening"). Shorts kısa ömürlü, uzun video kalıcı.

### 4.2 Yapay zekâ içeriği politikası 🟡 (16 Temmuz 2026)
- **Para kazanamayan içerik:** Genel geçer, tekrar eden veya şablonla seri üretilmiş "özgün olmayan" içerik, YouTube Partner Programı'nda para kazanamıyor.
- **Serbest olan:** **Yapay zekâ kullanmak serbest.** Hikâye anlatımını güçlendirmek için yapay zekâ kullanan kanallar para kazanmaya uygun kalıyor.
- **Neal Mohan'ın 2026 mektubu:** "Yapay zekâ bir ifade aracı olarak kalacak, insanın yerini almayacak." Düşük kaliteli yapay zekâ içeriğine ("AI slop") karşı spam ve tık tuzağı sistemleri genişletiliyor.
- **Senin için risk:** "Aynı görev, iki model" formatı her seferinde aynı şablonla ve senin yorumun olmadan tekrarlanırsa şablon içerik gibi görünebilir. Senin yorumun, ölçümün ve kararın her videoda görünür olmalı.

### 4.3 Made On YouTube 2026 (23 Eylül 2026) 🟡
- **Video A/B testi:** Aynı videonun **3 farklı kurgusu** test edilip hangisinin dikkati daha iyi tuttuğu ölçülebiliyor. İlk saniyeleri optimize etmek için ideal.
- **Shorts serileri:** Shorts'ları sezon ve bölümler halinde düzenleme imkânı. **"Ölçtüm" serisi için birebir uygun.**
- **Özel akışlar:** İzleyiciler istediklerini Gemini'ye kendi cümleleriyle yazıp kendilerine özel bir akış kuruyor. Başlık, açıklama ve konuşma net olmalı ki bu tür bir istekle eşleşebilsin. Örnek istek: "işletmeler için yapay zekâ otomasyonu anlatan Türkçe videolar".
- **Studio'da yapay zekâ destekli araçlar:** Taslak geri bildirimi, kanal tarzına uygun küçük resim üretimi, sohbet ederek video düzenleme.

### 4.4 YouTube için özet kurallar
- Shorts erişim getirir. Güven ve iş ise **uzun videodan** gelir: izleyiciyle 10–20 dakika geçirmek referans değeri taşır.
- Başlıklar sonucu vaat etsin ama tık tuzağı olmasın. Memnuniyet anketi tuzağı cezalandırır.
- Kanal açıklaması, bölümler ve oynatma listeleri konuyu net söylesin.
- Türkçe "RAG nasıl kurulur" veya "işletmede yapay zekâ ajanı" gibi aramalarda rekabet görece düşük. Bu yorumum, kesin ölçüm değil.

---

## 5. Üç platformun ortak noktaları

| Eğilim | X | Instagram | YouTube | Senin için anlamı |
|---|---|---|---|---|
| **Özgünlük ödülü** | Çalıntı içerik geliri asıl sahibine | Başkasının içeriğini paylaşanlar önerilerden çıkıyor | Şablon içerik para kazanamıyor | Kendi ürettiğin demolar büyük avantaj. Her platforma doğrudan yükle, başka platformun filigranını taşıma. |
| **Paylaşım en güçlü sinyal** | Linki kopyala 20, DM 5 | DM gönderimi bir numara | Paylaşım memnuniyet göstergesi | "Birine gönderilir mi?" testi |
| **Olumsuz sinyal pahalı** | −47 / −58 / −234 | Tahmini | Memnuniyet anketi | Tık tuzağı yok, vaat edilen neyse o |
| **Küçük üreticiye test** | ≤50 bin takipçi, 2 saat, 200 gösterim | Küçük üreticiler takipçi olmayanlara da gösteriliyor, Deneme Reels'i | Yeni içerik hızlı test ediliyor | Hesabın yeni olması dezavantaj değil. Tutarlı paylaşım şart. |
| **Kullanıcı kendi algoritmasını yazıyor** | Grok ile konu takibi | Your Algorithm | Gemini ile özel akışlar | Konu anahtar kelimeleri tutarlı olsun: LLM, RAG, ajan, otomasyon, işletme |
| **İlişki ağırlığı** | Karşılıklı takip +15 | Takipçilerle DM etkileşimi | Abone sadakati | Küçük ama gerçek bir ağ |

---

## 6. KorgaAI hesaplarına yansıması (strateji öncesi teşhis)

| Tespit | Algoritma açısından sonucu |
|---|---|
| Instagram: 13 gönderi, 0 takipçi, son 30 günde 1,3 bin izlenme | Erişim var, takibe dönüşüm yok. Algoritma içeriği yabancılara gösteriyor ama profil takip etmek için bir neden sunmuyor. |
| X: 2 takipçi, 37 takip edilen, sabit gönderi 66 gösterim | Soğuk başlangıç penceresi kullanılıyor ama karşılıklı ağ neredeyse yok. Karşılıklı takip güçlendirmesinden yararlanılamıyor. |
| YouTube: 3 Shorts, uzun video yok, kanal açıklaması yok | Kalıcı ve aranabilir içerik yok. Özel akışlar ve arama için konu sinyali zayıf. |
| İçerik: model karşılaştırmaları, oyunlar, 3D demolar | Görsel olarak güçlü, ama konu kümesi "yapay zekâ eğlencesi" olarak etiketleniyor, "işletmeye LLM sistemi" olarak değil. Algoritma seni yanlış kitleye eşleştirebilir. |
| "Ben sadece ne istediğimi söyledim" anlatısı | Özgünlük ve memnuniyet sinyali açısından riskli. İzleyici katkıyı modele atfediyor, YouTube'da da şablon içerik riski doğuruyor. |
| Profil açıklaması: "LLM sistemleri kuruyorum… ölçüp yayınlıyorum" | Güçlü ve net. Konu sinyali için ideal. İçerik bu cümleyle hizalanırsa üç platformda da doğru kümeye düşersin. |

**Stratejiye taşınacak ana sorular:**
1. İçerik konu kümesi "yapay zekâ eğlencesi"nden "ölçülmüş işletme çözümleri"ne nasıl kaydırılır, havalı demo gücü kaybedilmeden?
2. X'te ilk 50–100 karşılıklı bağlantı kimlerle kurulacak?
3. YouTube'da ilk uzun video hangi vaka olacak? "Ölçtüm" bir Shorts serisine nasıl dönüşecek?
4. Tek içerik üç platforma yerel olarak nasıl uyarlanacak, filigran ve şablon riskine düşmeden?

---

## 7. Kaynaklar

**Birincil (doğrudan incelendi)**
- xAI — X öneri algoritması kaynak kodu: https://github.com/xai-org/x-algorithm
  - `home-mixer/params/param.rs` (ağırlıklar ve soğuk başlangıç parametreleri)
  - `home-mixer/scorers/author_cold_start.rs` (küçük hesap test penceresi)
  - `home-mixer/scorers/value_model.rs` (puan birleştirme)
  - `docs/BIDIRECTIONAL_BOOST_CHANGE.md` (Temmuz 2026 karşılıklı takip değişikliği)

**X**
- TechCrunch — X just tweaked its algorithm to make it more friendly (13.07.2026): https://techcrunch.com/2026/07/13/x-just-tweaked-its-algorithm-to-make-it-more-friendly-less-battleground/
- TechCrunch — X replaces revenue sharing with Original Content Rewards (08.08.2026): https://techcrunch.com/2026/08/08/x-replaces-misaligned-revenue-sharing-program-with-original-content-rewards/
- TechCrunch — X cracks down on creators who steal content (16.07.2026): https://techcrunch.com/2026/07/16/x-cracks-down-on-creators-who-steal-content/
- Social Media Today — X updates its engagement bait detection: https://www.socialmediatoday.com/news/x-updates-its-engagement-bait-detection/825495/
- Social Media Today — X Is Testing a New Way To Handle Links in Posts: https://www.socialmediatoday.com/news/x-formerly-twitter-testing-links-in-app-link-post-penalties/803176/
- Social Media Today — X Publishes AI-Powered Algorithm Code: https://www.socialmediatoday.com/news/x-formerly-twitter-publishes-ai-powered-algorithm-code/810015/

**Instagram**
- TechCrunch — Instagram cracks down on content aggregators (30.04.2026): https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/
- Engadget — Instagram will penalize 'unoriginal' photo and carousel posts: https://www.engadget.com/2160560/instagrams-recommendation-algorithm-will-penalize-unoriginal-photo-and-carousel-posts/
- Social Media Today — Instagram chief shares algorithm insights and posting tips: https://www.socialmediatoday.com/news/instagram-chief-shares-algorithm-insights-and-posting-tips/831326/
- Social Media Today — Instagram chief debunks popular engagement hack: https://www.socialmediatoday.com/news/instagram-chief-debunks-popular-engagement-hack/816781/
- Social Media Today — Instagram engagement rates provide insight into reach: https://www.socialmediatoday.com/news/instagram-engagement-rates-provide-insight-into-reach/821170/
- Social Media Today — Instagram expands Your Algorithm tool to Explore: https://www.socialmediatoday.com/news/instagram-expands-your-algorithm-tool-to-explore/817772/
- About Instagram — Control Your Instagram Reels Algorithm: https://about.instagram.com/blog/announcements/reels-algorithm-control
- Social Media Today — IG Chief Says Longer Captions Won't Increase Reach: https://www.socialmediatoday.com/news/instagram-chief-says-longer-captions-dont-impact-post-reach/758462/

**YouTube**
- YouTube Blog — Neal Mohan'ın 2026 mektubu: https://blog.youtube/inside-youtube/the-future-of-youtube-2026/
- YouTube Blog — Made On YouTube 2026: https://blog.youtube/news-and-events/innovation-youtube-era-made-on-viewers-creators/
- TechCrunch — YouTube adds video A/B testing, dynamic thumbnails (23.09.2026): https://techcrunch.com/2026/09/23/youtube-adds-new-creator-tools-like-video-a-b-testing-dynamic-thumbnails-and-live-dubbing/
- TechCrunch — YouTube's new 'Shorts series' feature (23.09.2026): https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/
- TechCrunch — YouTube will let you build your own algorithm with AI (23.09.2026): https://techcrunch.com/2026/09/23/youtube-will-let-you-build-your-own-algorithm-with-ai/
- TechCrunch — YouTube clarifies policies around AI slop (20.07.2026): https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- Engadget — YouTube explains its AI slop policy: https://www.engadget.com/2226445/youtube-explains-ai-slop-policy-why-some-creators-wont-get-paid/
- Tubefilter — The YouTube Shorts algorithm appears to have changed to prioritize newer uploads: https://www.tubefilter.com/?p=189768

**Sınırlamalar**
- Instagram ve YouTube'un sıralama kodu açık değil. Bu bölümler resmî açıklamalar ve basın aktarımlarına dayanıyor.
- Bu çalışma ortamından yalnızca GitHub'a doğrudan erişilebildi. Diğer kaynaklar arama motoru özetleri üzerinden doğrulandı.
- X'in kodundaki değerler varsayılan değerler. Deneylerde kullanıcı gruplarına göre farklı değerler kullanılabiliyor ve xAI depoyu yaklaşık 4 haftada bir güncelliyor.
