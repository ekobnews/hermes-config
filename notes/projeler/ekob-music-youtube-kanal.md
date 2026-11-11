# EKOB MUSIC YouTube Kanalı

## Ümumi
- **YouTube kanal:** EKOB MUSIC (keçmiş EKOB STUDIO / Fight Shorts)
- **Kanal ID:** fight-shorts-510509 Google Cloud layihəsi
- **Google OAuth:** Client ID: 977493157543-vr81oeklr8kjq66lknbpcjiiepacpoq0
- **Test user:** ebuabu79@gmail.com
- **Token yeri:** /home/elbrus/podcast_work/youtube_token.json (WSL), sync olunacaq
- **Upload script:** /home/elbrus/podcast_work/upload_youtube.py

## Video Yükləmə Prosesi
1. Video faylı `/mnt/c/Users/ELBRUS/Downloads/`-dan `/home/elbrus/podcast_work/podcast_final_upload.mp4`-ə kopyalanır
2. `/home/elbrus/podcast_work/thumbnail.png` qapaq şəkli
3. `/home/elbrus/podcast_work/video_metadata.txt` - metadata (başlıq, təsvir, etiketlər)
4. `upload_youtube.py` işə salınır — unlisted yükləyir, thumbnail və caption əlavə edir
5. Sonra public edilir

## CFR Fix (Donma Problemi)
- Mənbə video CapCut VFR çıxarışı səbəbindən donur
- Fix: `ffmpeg -i input.mp4 -vf "fps=30" -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 128k -movflags +faststart output.mp4 -y`

## Yüklənmiş Videolar
| Tarix | Video | Link |
|-------|-------|------|
| 11.11.2026 | Ömrün O Tayında | https://youtu.be/BGvaHQyVwJY |

## Qeydlər
- Köhnə `ekob-studio` Google Cloud layihəsi işləmir (ebuabu79@gmail.com-un icazəsi yoxdu)
- Thumbnail API-si 403 qaytara bilər — kanal təsdiqi tələb olunur
- Caption yalnız danışıq varsa əlavə olunmalıdı, transcript.vtt köhnə podkastdan qalmışdı