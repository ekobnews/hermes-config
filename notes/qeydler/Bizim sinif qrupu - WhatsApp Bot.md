# "Bizim sinif" qrupu — WhatsApp Bot konfiqurasiyası

**Yenilənmə tarixi:** 12.09.2026

## Əsas məlumat

| Parametr | Dəyər |
|----------|-------|
| Qrup JID | `120363298388199346@g.us` |
| Qrup adı | "Bizim sinif" |
| Bot personajı | Həsən müəllim |
| Config key | `classmates` |
| Bot nömrəsi | VPS-də PM2 `whatsapp-agent` (id: 0) |

## Şagird identifikasiyası (CLASSMATE_MEMBERS)

```javascript
Elbrus  → "222831627526322@lid", "994707551301", "707551301", "0707551301"
Mətanət → "❤️", "matanat", "mətanət", "metanet"
Fuad    → "fuadimanov", "fuad"
Esmira  → "esmira"
Almaz   → "almaz"
İlahə   → "ilahə", "ilahe"
Araz    → "araz"
Səba    → "səba", "seba"
Günay   → "günay", "gunay"
Səkinə  → "səkinə", "sekine"
Nata    → "nata", "natəvan", "natevan"
Maarif  → "maarif"
Rəşad   → "rəşad", "reshad"
Etiş    → "etiş", "etish", "etibar"
```

## Şagirdlər haqqında qeydlər

- **Məktəb:** Mehdiabad qəsəbə tam orta məktəbi (1985 qəbul, 1995 məzun)
- **Qrupda 18 nəfər** keçmiş sinif yoldaşı
- **Sinifkomlar:** Almaz (Londonda yaşayır, qızı nüfuzlu universitetə qəbul olub) və Elbrus
- **İlahə** — "Allahın bacısı qızı", Sumqayıtda yaşayır, FHN-dən pensiyaçı
- **Nata (Natəvan)** — gözəllik salonu işlədir
- **Esmira** — ingilis dili müəlliməsi, Maarifin övladına dərs deyir
- **Maarif** — Qazel yük maşını ilə tikinti materialı daşıyır
- **Araz** — sinifə 1 il gec gəlib (Ermənistan, Yexeqnadzor), rabitə sistemində işləyir
- **Səba** — tibbi ekspertizada həkim
- **Fuad** — kişi salonunda bərbər, keçəldir. Atası Mədət müəllim (rəhmətlik) məktəbin direktor müavini
- **Etiş (Etibar)** — tarix müəllimi rəhmətlik İdris müəllimin oğlu
- **Rəşad** — Türkiyədə yaşayır
- **Günay** — kofe içməyi çox sevir
- **Səkinə** — keçmiş məktəb direktoru
- **Mətanət** — sinif yoldaşı
- **Almaz** — 24 oktyabrda Bakıya gələcək, sinifə qonaqlıq vermək istəyir

## Məktəb rəhbərliyi və müəllimlər

- **Direktorlar:** Qəzənfər → Məhər → Xanım müəllimə
- **Zavuç:** Mədət müəllim (Fuadın atası, rəhmətlik)
- **Tarix:** İdris müəllim (Etişin atası, rəhmətlik)
- **Coğrafiya:** Mehparə müəllimə (rəhmətlik)
- **İngilis dili:** Bəyaz müəllimə (rəhmətlik) və gəlini Növrəstə müəllimə
- **Riyaziyyat:** Sevil müəllimə (rəhmətlik)
- **Fizika:** Gülarə müəllimə
- **Kimya:** Şəfiqə müəllimə (rəhmətlik)

## Həsən müəllim personajının xüsusiyyətləri

- Həm sinif rəhbəri/pedaqoq, həm də yazıçı
- "Bir salxım üzüm" kitabının müəllifi
- İlahəyə "Allahın bacısı qızı" deyir
- Söhbətdə "uzun işdir", "çətin məsələdir" ifadələrini işlədir
- Xatirələr: İlahənin Elbrusa qırıq stul qoyması; Esmiranın Fuadın başını divara vurması; Arazın "havla"/"şavlar" səhvləri
- Son görüşlər: 1) 15 iyun — Elbrusun qızının toyu; 2) 24 avqust — başqa görüş

## Texniki qeydlər

- Bot qrupdan çıxarılıb sonra yenə əlavə olunsa, JID dəyişmədiyi üçün eyni işləyəcək
- Konfiqurasiya `agent.js` faylında hardcoded olunub (`GROUPS` obyekti)
- Qrup JID-si `120363298388199346@g.us` — groups.json faylından asılı deyil
- Bot qrupa əlavə olunanda xüsusi "welcome/handler" yoxdur, sadəcə mesaj gələndə işə düşür
- Audio transkripsiya, şəkil/video analizi aktivdir
- 2.5-4s typing delay\n\n## Əlaqəli layihələr\n\n- [[qeydler/EANA ailəsi - WhatsApp Bot|EANA ailəsi]] — eyni botun digər qrupu\n- [[qeydler/5 Beyin layihəsi|5 Beyin]] — Telegram bot layihəsi\n- [[Ana Səhifə]]