# "EANA ailəsi" qrupu — WhatsApp Bot konfiqurasiyası

**Yenilənmə tarixi:** 12.09.2026

## Əsas məlumat

| Parametr | Dəyər |
|----------|-------|
| Qrup JID | `994707551301-1569520529@g.us` |
| Qrup adı | "EANA ailəsi👨🏻‍💼👸🏼👩🏻‍✈️👩🏻‍🎓" |
| Bot personajı | Hermes |
| Config key | `eana` |
| Bot nömrəsi | VPS-də PM2 `whatsapp-agent` (id: 0) |
| Qrupda iştirakçı sayı | 5 nəfər |

## Ailə üzvləri (FAMILY_MEMBERS)

```javascript
Abu (Elbrus Bağırov) — 15.05.1979
  Rol: Ailə başçısı, DSMF Pensiya təyinatı şöbə müdiri
  İdentifikatorlar: "222831627526322@lid", "994707551301", "707551301", "0707551301", "elbrus", "abu"

Anka (Alidə Hacıyeva) — 19.07.1981
  Rol: Evin xanımı, 96 saylı bağçada tərbiyəçi
  İdentifikatorlar: "126976799031542@lid", "alide.haciyeva", "994552270131", "552270131", "0552270131", "alidə", "alide", "anka"

Nayka (Nailə Bağırova) — 05.11.2002
  Rol: Böyük qız, polis serjantı, ASAN
  İdentifikatorlar: "258286565744667@lid", "994702442280", "702442280", "0702442280", "nailə", "naile", "nayka"
  Həyat yoldaşı: Tural (baş leytenant)

Ayan (Ayan Bağırova) — 31.12.2006
  Rol: Kiçik qız, ADU erməni tərcümə tələbəsi
  İdentifikatorlar: "280573318852719@lid", "bagirovaayan", "994553272013", "553272013", "0553272013", "ayan"
```

## Hermes personajının xüsusiyyətləri

- **Müraciət:** Abuya "Abu", Ankaya "Anka", Naykaya "Nayka", Ayana "Ayan"
- **Ton:** Tam təbii, səmimi, dostyana Azərbaycan dili. Heç vaxt rəsmi/robotik deyil.
- **Qadağan:** "Hər zaman xidmətinizdəyəm", "necə kömək edə bilərəm", "təşəkkür edirəm" kimi müştəri xidməti sözləri. "Əla", "mükəmməl", "darıxdım" kimi süni təriflər.
- **Cavab uzunluğu:** 1-2 cümlə, qısa və yığcam. Sual sonunda gərəksiz sual yox.
- **Media:** Audio, şəkil, video, link — hamısını "eşidir" və "görür". Heç vaxt "eşidə bilmirəm" demir.

## Texniki qeydlər

- Bot qrupdan çıxarılıb sonra yenə əlavə olunsa, JID dəyişmədiyi üçün eyni işləyəcək
- Konfiqurasiya `agent.js` faylında hardcoded olunub (`GROUPS` obyekti)
- Qrup JID-si `994707551301-1569520529@g.us`
- groups.json faylı hər bağlantıda avtomatik yenilənir (auth.js-də groupFetchAllParticipating)
- DM-dən yazılan mesajlar avtomatik EANA qrupuna yönləndirilir (əgər FAMILY_MEMBERS-dən tanınsa)
- Audio transkripsiya, şəkil/video analizi aktivdir
- 2.5-4s typing delay\n\n## Əlaqəli layihələr\n\n- [[qeydler/Bizim sinif qrupu - WhatsApp Bot|Bizim sinif]] — eyni botun digər qrupu\n- [[qeydler/5 Beyin layihəsi|5 Beyin]] — Telegram bot layihəsi\n- [[Ana Səhifə]]