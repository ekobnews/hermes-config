# Fight Shorts — Sistem Tam Quraşdırma (04.10.2026)

## Kanala aid aktivlər
- **Avatar:** Kanal şəkli — user əl ilə yükləyib (API dəstəkləmir)
- **Banner:** YouTube API ilə yükləndi — `yt3.googleusercontent.com/...`
- **İntro (5 kadr):** ring → siluet → əlcək → FIGHT SHORTS → SUBSCRIBE — hər video başında 4.7s
- **Watermark:** Fight Shorts loqosu, sağ alt küncdə daimi

## Texniki quraşdırma
- **auto_shorts.py** — gündə 1 short, 18:00 AZ (cron)
- **Musiqi:** Kevin MacLeod (incompetech.com) — CC BY 4.0, claim-free, monetizasiya təhlükəsiz
- **Səs:** ElevenLabs (Starter $5/ay, voice ID: bfGb7JTLUnZebZRiFYyq)
- **Intro + Watermark** auto_shorts.py pipeline-ə əlavə olundu
- **Video keyfiyyət:** 720p (veryfast preset)
- **Cookies:** `youtube_cookies.txt` — Playwright profili də hazırlanıb

## API Açarları (.env)
- ElevenLabs: sk_979b3cd530fe3721ba2e6c8ae70bf66a21e3315563add8ed
- Pixabay: 57878638-d911c1b83460ea2246f4a1d40

## Döyüşçü Sırası
1. ✅ Mike Tyson (yüklənib)
2. ✅ Muhammad Ali (yüklənib)
3. ⏳ Conor McGregor — 05.10.2026 18:00 AZ
4. Khabib, Jones, Canelo, Ngannou, Silva, Foreman, Fury

## GitHub
- `ekob-news-bot` reposu: auto_shorts.py, assets/, .env (API açarları)