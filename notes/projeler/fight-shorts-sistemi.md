# Fight Shorts — Sistem Sənədi (yenilənib: 16.10.2026)

## Kanala aid aktivlər
- **Avatar:** Kanal şəkli — user əl ilə yükləyib
- **Banner:** YouTube API ilə yükləndi
- **Watermark:** Fight Shorts loqosu, sağ alt küncdə daimi (`/root/fight_shorts_assets/watermark_small.png`)
- **İntro çıxarıldı** (piksel problem)
- **Kanal:** FIGHT SHORTS — https://www.youtube.com/@fightshorts2026

## Video Kitabxana (`/root/fight_shorts_library/`)
- **46+ klip, 10 döyüşçü** (proxy ilə YouTube 720p-dən yığıldı)
- **`clip_verdicts.json`** — hər klipin vizual yoxlama nəticəsi (gemini-2.5-flash): "DÖYÜŞ" / "YOX"
- auto_shorts.py **YALNIZ döyüş səhnəsi təsdiqlənmiş** kliplərdən seçir (müsahibə/trash talk RƏDD)
- Seçim: təsdiqlənmişlər arasından ən böyük 1/3 → təsadüfi

## Musiqi — ElevenLabs Music API (Kevin MacLeod TAMAMEN ÇIXARILDI)
- Hər short üçün **orijinal AI musiqi** generasiya olunur (təkrarsız, claim-free)
- Prompt: 3-hissəli ark — gərgin intro → buildup → drop, 145 BPM, aqressiv elektronik
- Müddət: **58 san** (video ilə sinxron)
- Key: `/root/ekob_news/.env` → `ELEVENLABS_API_KEY` (cron-da da işləyir)
- Fallback: `fight_shorts_music/` keşi (ElevenLabs fail olsa)

## Montaj (shorts_editor.py) — professional standart
- Rəng korreksiyası: contrast 1.08, saturation 1.22, gamma 0.98
- Ken Burns: yavaş zoom 1.0 → 1.06
- Səs: loudnorm (-14 LUFS), fade in 1.2s / fade out 2s
- Format: h264 + yuv420p + faststart (Telegram/mobil uyğunluq)
- **Müddət: maks 58 san** ← COPYRIGHT QAYDASI (60+ san YouTube bloklayır!)

## YouTube OAuth (KRİTİK)
- Client: **"Fight Shorts Web"** (Web application) — `977493157543-o328j3ipjj223533loa8h4p360b6vqad...`
- **Desktop client işləmir** (redirect_uri_mismatch)
- Redirect URI: `https://developers.google.com/oauthplayground` (sonunda `/oauth2` YOXUDUR!)
- Scope: `https://www.googleapis.com/auth/youtube.upload` (yalnız yükləmə — silmə üçün `youtube` scope lazımdır)
- Refresh token: OAuth Playground-dan (16.10 təzələndi)

## Cron (Hermes)
- **Həftə içi (BE–CÜ) 20:00 AZ** — `auto_shorts.py --skip-upload` → video hazırlanır, sənə göstərilir → "ok" → yüklənir
- **Cümə 14:00 UTC** — Weekly Best Of kompilasiya
- **Şənbə 20:00 AZ** — Həftəlik icmal (baxış/like/abunə)
- **Bazar** — istirahət
- Hər günün videosu `/root/fight_shorts_review/GG-AA-YYYY_dovuscu.mp4` arxivində

## Yüklənmiş videolar (YouTube)
- Tyson lj6blzyvoQ0 | Ali 7yDnLGCX_YI | Khabib Yi00EE8lnXI | Canelo pCrq7ZaHbZM
- Tyson Fury Kr9ERoQGgXY (14.10) | Khabib 58s Vs_QY6Suuxo (16.10)
- Bloklu/dublikat (silmək lazımdır, geniş icazəli token yox): hjn6UI_R0p4 (66s Khabib), WiEiKNyhabE (Conor dublikat)

## Döyüşçü Sırası (16.10)
- done: conor-mcgregor, khabib, jon-jones, canelo, ngannou, foreman, tyson-fury
- **Növbəti: anderson-silva** → sonra siyahı yenidən başlayır

## GitHub
- `ekob-news-bot` repo: auto_shorts.py, shorts_editor.py, build_library.py, upload_video.py, weekly_best_of.py, check_balance.py, clip_verdicts.json