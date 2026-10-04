# Fight Shorts — YouTube Avtomatlaşdırma Sistemi

## 03-04.10.2026

### YouTube API Quraşdırması
- **Google Cloud Console:** "Fight Shorts" layihəsi yaradıldı
- **YouTube Data API v3:** Enable edildi
- **OAuth Consent Screen:** Konfiqurasiya edildi (test user: ebuabu79@gmail.com)
- **OAuth Client:** "Fight Shorts Bot" — Desktop app
- **Redirect URI:** `urn:ietf:wg:oauth:2.0:oob`
- **Refresh Token:** ✅ Alındı (qalıcı)
- **PKCE:** code_verifier ilə işləyir
- **Playwright:** Kalıcı browser profili `/root/.youtube_session` (cookie rotasiyası üçün)

### Kanal
- Ad: **Fight Shorts**
- ID: `UCTD-nHfgAhWNOn41VJQoGWw`
- Tip: Brand Account (Google hesabı altında)

### Video Pipeline
1. **yt-dlp** — YouTube-dan mənbə video axtarır (720p, keyfiyyətli)
2. **FFmpeg** — 720x1280 Shorts formatına çevirir, 30-40san kəsir
3. **Edge TTS** (DavisNeural) — kişi səsi ilə təsvir
4. **FFmpeg (amix)** — səs + epik döyüş musiqisi qarışdırır
5. **YouTube API v3** — Fight Shorts kanalına yükləyir

### Döyüşçü Sırası
| # | Döyüşçü | Tarix | Status |
|---|---|---|---|
| 1 | Mike Tyson | 04.10 | ✅ [YouTube](https://youtube.com/watch?v=lj6blzyvoQ0) |
| 2 | Muhammad Ali | 04.10 | ✅ [YouTube](https://youtube.com/watch?v=7yDnLGCX_YI) |
| 3 | Conor McGregor | 05.10 | ⏳ |
| 4 | Khabib Nurmagomedov | 06.10 | ⏳ |
| 5 | Jon Jones | 07.10 | ⏳ |
| 6 | Canelo Alvarez | 08.10 | ⏳ |
| 7 | Francis Ngannou | 09.10 | ⏳ |
| 8 | Anderson Silva | 10.10 | ⏳ |
| 9 | George Foreman | 11.10 | ⏳ |
| 10 | Tyson Fury | 12.10 | ⏳ |

### Fayllar
- `auto_shorts.py` — master avtomatlaşdırma skripti (gündə 1 short)
- `youtube_uploader.py` — YouTube API uploader
- `youtube_auth.py` — OAuth auth skripti
- `youtube_session.py` — Playwright session meneceri
- `youtube_cookies.py` — Cookie yönəticisi
- `fight_shorts.py` — ilkin generator (köhnə)
- `youtube_cookies.txt` — Saxlanmış YouTube cookies

### Cron
- **Fight Shorts Daily** — hər gün 14:00 UTC (18:00 AZ)
- auto_shorts.py işləyir, nəticəni bura bildirir

### Dərslər
- YouTube cookies tez rotasiya olunur → Playwright profili qalıcı həll
- FFmpeg `-c copy` ilə kəsmək işləmir (keyframe alignment)
- 1080x1920 encoding VPS-də yavaşdır → 720p istifadə edirik
- Edge TTS bəzən "No audio received" xətası verir → Hermes TTS daha stabil