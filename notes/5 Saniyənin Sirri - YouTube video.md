# 5 Saniyənin Sirri — EKOB STUDIO YouTube Videosu

**Yüklənmə tarixi:** 31.10.2026
**Link:** https://youtu.be/HD6B5q0r-lk
**Status:** Public

## Texniki detallar

- **Audio:** 23:33 dəqiqə (5 Saniyə Qaydası.m4a)
- **Video:** 15 san 4K loop (17198552_3840_2160_30fps.mp4), 1080p-ə endirildi
- **İntro:** 5 san PNG qapaq şəkili (5 Saniyənin Sirri Podcast.png), həm də thumbnail
- **Fon musiqisi:** Sakit piano (mixkit ID 22), 4% səs, loop edildi
- **Yükləmə üsulu:** podcast_work/upload_youtube.py (Google API, refresh token)

## İş axını

1. Faylları WSL-ə kopyala (`~/ekob-video/`)
2. PNG-dən 5 san intro video hazırla (`ffmpeg -loop 1`)
3. Video loop et (`stream_loop -1`), audio ilə concat
4. Fon musiqisini əlavə et (`amix`, volume=0.04)
5. YouTube-a yüklə (unlisted → sonra public)

## Qeydlər

- Token vaxtı keçəndə `youtube_token.json` silinir, OAuth təzələnir
- Fon musiqisi danışığı basmamalı — 4% idealdır
- Video 2.6GB oldu (1080p, 23 dəq)
