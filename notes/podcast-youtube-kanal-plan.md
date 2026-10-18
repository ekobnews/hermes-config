# Podcast & YouTube Kanal Planı

**Tarix:** 18 Oktyabr 2026
**Status:** Plan mərhələsi

## Kanal
- Ad: **EKOB STUDIO** (18.10.2026 qərara alındı)
- Google hesabı: elbrusbagirov1979@gmail.com
- EKOB NEWS-dan ayrı, yeni YouTube kanalı
- Mövzu: psixologiya, beyin, münasibətlər, özünü kəşf — müxtəlif mövzulu podcastlar (daimi)
- Dil: İngiliscə

## Workflow (test olunub)
1. **NotebookLM** → duet podcast (mətn + audio)
2. **Pexels** → background video (4K stock video)
3. **ElevenLabs Music API** → background musiqi ("soft ambient piano", 5 dəq, loop)
4. **FFmpeg** → hamısını birləşdir:
   - pexels video (scale 1920×1080, 30fps)
   - podcast audio (əsas səs)
   - bg music (ElevenLabs) volume 0.08
   - showwaves waveform overlay (aşağıda)
   - CRF 28, AAC 128k, h264

## Vacib qeydlər
- Video audio-dan 1 saniyə belə qısa olmamalıdır. Tam audio uzunluğu qədər getsin.
- Cover şəklində "NotebookLM" yazısı olmamalıdır.
- Pexels 4K video böyük fayldır, CRF optimallaşdırıla bilər.
- Sekvensial prompt sistemi: hər addım bir prompt, nəticə gözlə, sonrakı prompt.

## Status (18.10.2026 axşam)
- Kanal **EKOB STUDIO** açıldı
- Video **yükləndi**: https://youtu.be/QRXYzmCVVLw (unlisted) — başlıq + təsvir + etiketlər + AZ captions + custom thumbnail ✅
  (İlk cəhd taH2eTja3NM kanal təsdiqi olmadan 15 dəqiqə limitinə görə silinmişdi; kanal təsdiqləndi → yenidən yükləndi)
- Custom thumbnail: ✅ (kanal təsdiqlənib)
- Video: `podcast_final_upload.mp4` — 1.62 GB, CRF 33, 1080p, 25:13 ✅
- Mövzu: Münasibətlərdə beynimizin qurduğu tələlər
- OAuth qurulub: client_secret + youtube_token.json (avtomatik yükləmə gələcək üçün hazırdır)

## Növbəti addımlar
- ~~Kanal adının qərarı~~ → **EKOB STUDIO** ✅
- ~~Kanal açılışı~~ ✅ (studio.youtube.com → create channel)
- Video yükləmə: istifadəçi upload edir (thumbnail.png seçilməli)
- Transkript: transcript.txt + transcript.vtt → description/captions