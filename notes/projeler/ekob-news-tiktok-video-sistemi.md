# EKOB NEWS — TikTok Video Sistemi

**Tarix**: 20 Sentyabr 2026

## Yeniliklər

### Buffer API
- Köhnə Buffer hesabında rate limit dolmuşdu (30 gün)
- Yeni API açarı alındı ($18 ödəniş)
- Assets formatı düzəldi: `[{"image":{"url":"..."}}]` → IG və TikTok işləyir

### Platforma Strategiyası
| Xəbər növü | Facebook | Instagram | TikTok |
|---|---|---|---|
| Mətn + şəkil | Şəkil + caption | Şəkil + caption | Video (TTS səs + caption) |
| Mətn + video | Video + caption | Video + caption | Video + caption |
| Sadəcə mətn | Mətn | Paylaşmır | Paylaşmır |

### TikTok Video Generator
- **Fayl**: `tiktok_video.py` — şəkil + TTS + fon musiqisi → MP4
- **TTS**: Edge TTS (`az-AZ-BabekNeural`) — təbii səs
- **Video**: MoviePy ilə montaj (15-30 saniyə)
- **Hosting**: Catbox.moe (pulsuz, 200MB limit)
- **Hashtaglar**: AI hər xəbərə İngiliscə 5-8 TikTok hashtagı əlavə edir

### Quraşdırma
- `/root/ekob_news/ekob.py` — əsas bot (systemd xidməti)
- `/root/ekob_news/tiktok_video.py` — video generator
- Venv-də moviepy, edge-tts quraşdırılıb

### Bağlantılar
- [[Ana Səhifə]]
- [[gundelik/20-09-2026|20 Sentyabr 2026]]