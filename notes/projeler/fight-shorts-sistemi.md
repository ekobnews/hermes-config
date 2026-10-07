# Fight Shorts — Sistem Quraşdırma (08.10.2026)

## Kanala aid aktivlər
- **Avatar:** Kanal şəkli — user əl ilə yükləyib
- **Banner:** YouTube API ilə yükləndi
- **Watermark:** Fight Shorts loqosu, sağ alt küncdə daimi
- **İntro çıxarıldı** (piksel problem)

## Video Kitabxana (`/root/fight_shorts_library/`)
- 25 klip, 4 döyüşçü: Conor(6), Khabib(3), Jon Jones(10), Canelo(6)
- auto_shorts.py əvvəl kitabxanaya baxır, tapmasa → YouTube (Dailymotion fallback)
- YouTube VPS IP bot-blok — library daimi həll

## Musiqi Kitabxana (`/root/fight_shorts_music/`)
- **17 track** Kevin MacLeod (CC BY 4.0, claim-free, monetizasiya təhlükəsiz)
- Ən kəskin: Clash Defiant, Aggressor, Stoneworld Battle, Darkest Child
- Musiqi heç vaxt download olunmur — local

## Süjet Xətti (shorts_editor.py)
- Video 3 hissəyə bölünür: **THE STAGE IS SET** (16s, ağ yazı) → **THE BATTLE** (32s, qırmızı yazı) → **THE CHAMPION** (25s, sarı yazı)
- Musiqi tədricən güclənir: 0.06 → 0.10 → 0.12
- Watermark hər yerdə

## Çıxarılan xüsusiyyətlər
- ❌ **Səs:** ElevenLabs səsi robotik idi, çıxarıldı. Voice Lab düzəldəndə qayıdacaq
- ❌ **Slow-mo:** ML/GPU tələb edir (pose/impact detection). Gələcəkdə OpenCV ilə

## Cron
- Gündə 1 short, **18:00 AZ** (14:00 UTC)
- Cümə: **Weekly Best Of compilation** (14:00 UTC → YouTube)
- auto_shorts.py → shorts_editor ilə 60-75 san video
- Hər short avtomatik `/root/fight_shorts_weekly/<həftə>/` qovluğuna saxlanılır

+ ## 5 Beyin Bot Düzəlişi (07.10)
+ - **Dil:** Prompta "YALNIZ Azərbaycan dilində" əlavə olundu
+ - **Şəkil oxuma:** handle_photo indi şəkli base64-ə çevirib OpenAI/Gemini/Claude vision API-yə göndərir
+ - **Conflict:** Köhnə instance öldürüldü, təmiz qaldı

## Döyüşçü Sırası
1. ✅ Mike Tyson
2. ✅ Muhammad Ali
3. ✅ Conor McGregor
4. ✅ Khabib (yüklənib, Dailymotion)
5. ⏳ Jon Jones — növbəti
6. Canelo, Ngannou, Silva, Foreman, Fury

## GitHub
- `ekob-news-bot` repo: auto_shorts.py, shorts_editor.py, build_library.py, refresh_cookies.py, assets/, music/