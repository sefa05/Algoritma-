# Ana Takvim — Ekim–Kasım 2026 (8 hafta) · ✍️ Sadece metin modu

**Amaç:** İlgi çekici ve bilgilendirici **yazılı** içerik. Video, deney ve satış çağrısı yok (bkz. `CLAUDE.md` → Mevcut mod).

**Platformlar:**
- **X:** Ana platform.
- **Threads:** X'teki metnin aynısı.
- **Instagram:** İsteğe bağlı, haftalık metin görseli.
- **YouTube:** Beklemede.

## Haftalık kalıp (uzman tonu, `CLAUDE.md` → Uzman tonu standardı)
| Gün | Saat | Tür |
|---|---|---|
| **Pzt** | 09:00 | **Ana dizi** ya da **teknik not**. Haftanın en güçlü içeriği. |
| **Sal** | 21:00 | Teknik not: tek bir mekanizma ya da hata |
| **Çar** | 21:00 | **Dizi:** teşhis sırası, karar çerçevesi ya da kontrol listesi |
| **Per** | 09:00 | **Gelişme:** son bir haftanın önemli değişikliği ve pratik etkisi, kaynaklı |
| **Cum** | 21:00 | **Mit mi gerçek mi:** yaygın bir inanç, kaynaklı cevap |
| **Cmt** | 12:00 | Görüş ✏️ |
| **Paz** | 12:00 | Teknik not (kısa) |

## Konular
| Hafta | Tarih | Ana dizi / teknik not | Çar · Dizi | Cum · Mit mi gerçek mi |
|---|---|---|---|---|
| **H1** | 5–11 Eki | LLM sistemleri üretimde neden bozulur: 6 kırılma noktası · Prompt caching | RAG teşhis sırası | "LLM hakem objektiftir" |
| **H2** | 12–18 Eki | Hibrit arama ve reranker: anlamsal arama neden tek başına yetmez? | Değerlendirme seti nasıl kurulur: 6 adım | "Bağlam penceresi 1M oldu, RAG'e gerek kalmadı" (kaynak: Liu vd., *Lost in the Middle*, 2023 + maliyet/gecikme) |
| **H3** | 19–25 Eki | Yapılandırılmış çıktı: JSON'u istemle değil şemayla garantilemek | Tamamlanan iş başına maliyet: hesap şablonu (gerçek fiyatlarla) | "Fine-tuning modele yeni bilgi öğretmenin en iyi yolu" |
| **H4** | 26 Eki–1 Kas | Ajan araç tasarımı: iyi bir aracın 4 özelliği | Ajan ne zaman gereksiz? Otomasyon, tek çağrı, ajan | "Daha büyük model her zaman daha iyi sonuç verir" |
| **H5** | 2–8 Kas | Dolaylı istem enjeksiyonu: saldırı yüzeyi ve önlemler | Üretimde LLM gözlemlenebilirliği: neyi kaydetmeli? | "Yapay zekâ metin dedektörleri güvenilirdir" (kaynak: OpenAI 2023'te kendi sınıflandırıcısını düşük doğruluk nedeniyle kaldırdı) |
| **H6** | 9–15 Kas | Türkçe için embedding seçimi: neye bakılmalı? | Parçalama stratejileri: sabit, yapısal, anlamsal | "Modele 'adım adım düşün' demek her zaman işe yarar" (düşünme modlu modellerde durum) |
| **H7** | 16–22 Kas | Batch API: acil olmayan işlerde maliyeti yarıya indirmek | İnsan onayı nereye konmalı: risk matrisi | "Açık kaynak model her zaman daha ucuzdur" (barındırma maliyeti) |
| **H8** | 23–29 Kas | Model geçişi: yeni sürüme geçerken neler bozulur? | LLM sistemini üretime almadan önce 12 maddelik kontrol listesi | "Temperature 0 deterministik çıktı demektir" |

- **Perşembe gelişme gönderisi** her hafta gündeme göre seçilir. Pazar rutini web'de araştırır, kaynağı ilk yanıta koyar.
- **Konu önceliği:** Takipçilerden gelen teknik sorular listeyi değiştirebilir.

## Doğruluk kuralları
- **Mit mi gerçek mi** ve **gelişme** gönderilerindeki her iddia resmî bir kaynağa ya da güvenilir bir habere dayanır. Kaynak ilk yanıtta yer alır.
- **Belirsiz cevaplar:** Cevap "kısmen doğru" ise öyle yazılır. Kesinlik abartılmaz.
- **Rakamlar:** Kaynağı yoksa kullanılmaz.

## Kontrol noktaları
- **H4 sonu (1 Kas):**
  - Hangi tür (kavram, dizi, mit, gelişme) en çok kaydediliyor, paylaşılıyor ve yanıt alıyor? Ona göre ağırlık değişir.
  - Saatler gözden geçirilir.
- **H8 sonu (29 Kas):** 8 haftalık değerlendirme. Yazıyla devam mı, video veya deney eklemek mi? Kararı Sefa verir.

## Esneklik
- **Gündemde büyük bir gelişme olursa:** O hafta Pazartesi kavramı ya da Cuma miti bu konuya döner.
- **Gün kaçarsa:** Telafi etmeye çalışma. Ertesi günün gönderisiyle devam et.
