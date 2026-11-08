# Hermes Skill-ləri (07.11.2026)

Elbrusun istəyinə əsasən, 4 bənd üzrə skill-lər quruldu — həqiqi işlək, sınaqdan keçmiş.

## 1. ai-youtube-video (media)
Mövzu başlığından TAM hazır YouTube videosu:
- Ssenari (Deepseek) → Şəkillər (Gemini Flash Image) → Səs (ElevenLabs Rachel) → Musiqi → Montaj (FFmpeg) → Upload
- Skriptlər skill-dədir: `scripts/gen_scene_images.py`, `scripts/build_video.py`
- **Sınaq:** "5 Things Successful People Do Before 7 AM" — 2:36 video, 7 səhnə, işlədi

**Pitfalls:**
- FFmpeg concat filter (tək komanda) → qara ekran; hər səhnə ayrı render + concat demuxer etibarlıdır
- Audio indekslər: şəkillər 0..N-1, voiceover=N, music=N+1
- Azərbaycanca ElevenLabs premade səslər robotik; ingilis Rachel təbii

## 2. cartoon-story-biznes (media)
Uşaq şəkli → cizgi qəhrəmanı → nağıl → səs → video (Bebora.Stories modeli)
- Cizgi obrazı: Gemini Flash Image (img2img, imgbb linki ilə) ✅ işləyir (Abu nümunəsi)
- Nağıl: Deepseek, Azərbaycanca
- **Məhdudiyyət:** uşaq animasiyası (hərəkət) üçün Kling AI ($10/ay) və ya Dreamina (pulsuz, watermark) lazımdır. OpenRouter video modelləri (minimax) real video ETMİR.
- Bazar: kitab 30-50 AZN, video 50-100 AZN; ayda 15-20 sifariş = 600-800 AZN

## 3. ekob-studio-podcast (media)
Podcast audio → video (EKOB STUDIO kanalı)
- 52 movzu videosu loop + audio mix + sakit musiqi
- Video müddəti = audio müddəti (MÜTLƏQ)
- Build skript: /root/ekob_news/build_ekob_studio.py

## 4. kripto-muhafize-hesabat (crypto-trading-bots gücləndirildi)
- Günlük hesabat formatı əlavə olundu (22:00 AZ)
- Health check 10:00 AZ (səssiz), P&L hesabat 22:00 AZ (məcburi)

## Əsas nəticə
Nə qədər çox iş görsək, skill-lər o qədər dəqiqləşir. Skill = yaddaş + prosedur + dərslər. Bir daha eyni səhvi etməmək üçün öz-özünə təkmilləşir.