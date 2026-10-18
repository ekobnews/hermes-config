# Podcast & YouTube Kanal Planı

**Tarix:** 18 Oktyabr 2026
**Status:** Plan mərhələsi

## Kanal
- EKOB NEWS-dan ayrı, yeni YouTube kanalı
- Mövzu: psixologiya, beyin, münasibətlər, özünü kəşf
- Dil: İngiliscə (kanal adı "EKOB Voice" istiqamətində)

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

## Növbəti addımlar
- YouTube kanalı açılışı
- Kanal adının qərarı