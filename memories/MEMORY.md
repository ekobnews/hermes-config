User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları VPS-1 PM2-də: EANA (4 ailə) + Bizim sinif (18 şagird). 2.5-4s typing delay.
§
5 Beyin botu VPS-2 77.42.37.230 Docker-da: 4 AI+meta-orchestrator, /root/5beyin-bot/
§
İş haqqında danışanda birbaşa. 'davam edək?' çox vaxt söhbəti davam etdirmək deməkdir — dərhal işə atılma, əvvəl hal-əhval soruş.
§
EKOB NEWS: Telegram→AI→TG+Buffer. ElevenLabs API VPS-1-də (/root/ekob_news/.env). HeyGen AZ video planı.
§
Post-merge hook (~/hermes-config/.git/hooks/post-merge): git pull → Obsidian rsync.
§
User həm WSL, həm VPS agentlərini qarşılıqlı işlədir — fikirləri birimizdən o birinə göndərir, konsensus gözləyir. İki agentin razılaşdığı həllərə daha çox güvənir.
§
Video render: audio-dan qısa olmamalıdır. -t parametri ffprobe dəqiq dəyərindən (kəsilməmiş) istifadə et, yaxud -shortest əvəzinə a:duration=first ilə audio boyu get.
§
İlk video: youtu.be/QRXYzmCVVLw (18.10, unlisted, public edilməli)
§
WSL env quirk: background process-lərdə ~/.hermes/bin PATH-də olmur (uv tapılmır) — tam yolla çağır. uv venv-lərində pip yoxdur, uv pip install istifadə et.
§
EKOB STUDIO (18.10): Yeni YouTube podcast kanalı — https://youtube.com/@ekobstudio. NotebookLM duet audiolardan podcast videoları. Ilk video: 'Münasibətlərdə Beynimizin Qurduğu Tələlər' (QRXYzmCVVLw). Videolar WSL local Hermes-də hazırlanır (VPS CPU çox yavaş, GPU yox). Background musiqi: ElevenLabs Music API sakit ambient. Podcast video istehsalı artıq VPS-de deyil, local-da.
§
Podcast video istehsali (18.10): VPS GPU-suz çox yavaş — 25 dəq video saatlarla cəkdi, user məyus oldu. Bundan sonra ağır video işləri LOCAL Hermes (WSL, notebook GPU) ilə görülür. VPS-də təkrarlanan video uğursuzluqda dayanıb alternativa təklif etməli (CapCut/WSL), saatlarla donmə.
§
User kanal adları üçün: sırf Azərbaycan hərfləri (ə/ğ/ı/ö/ş/ü) olan ad istəmir — beynəlxalq hərflərdə ad seçir (məs: 'EKOB STUDIO'). User hər dəfə yeni xəbəri bölüşür vasitəsi ilə məlumatlı qalmağı istəyir; eyni cavabı təkrar vermək onu qıcıqlandırır ('eynі suala nə qədər cavab verdin').
§
Dreamina (capcut.com) — ByteDance AI video/image generator. User qeydiyyatdan keçib, pulsuz gündəlik 120 kredit. Seedance 2.5 (30 san video), Seedream (şəkil). Gələcəkdə podcast fonu/döyüş klipləri üçün potensial alət. Epidemic Sound abunəsiz işləmir, Pixabay music API 404 — musiqi ElevenLabs.
§
Podcast video production (19.10): EKOB STUDIO kanali — youtube.com/@ekobstudio. Ilk video canli (QRXYzmCVVLw). NotebookLM audio + Pexels fon videosu + ElevenLabs ambient musiqi (5 dəq, loop) + audio dalğası formatı. Video kodlama VPS GPU olmadığı üçün çox yavaş — local WSL daha sürətli (CPU + GPU). /tmp RAM disk (2GB), böyük fayllar /root/ altında işlənməli.
§
Dreamina (ByteDance): pulsuz gündəlik 120 kredit, Seedance 2.5 ilə 30 san AI video generasiyası (720p, watermark). Şəkildən/mətndən/audio-dan video. Fight Shorts podcast fonu üçün sınaq edilə bilər. Qiymətli plan $15/ay — watermark yox, 1080p.
§
Spotify monetizasiya (20.10): Azərbaycan hələ Partner Program-a daxil DEYIL. Şərt: 3 epizod, 2000 saat/ay, 1000 dinləyici/ay. Məncə YouTube-a fokuslanmaq daha doğru (Azərbaycan üçün maneə yox).
§
User isteyir ki, VIDEO STATISTIKASI/TRENDLERI (baxış, like, klip seçimi, saatlar) analiz edib ÖZÜM nəticə çıxarım və onunla müzakirə edim — o soruşmadan. Mütləq fikir veriləsi meyil: Muhammad Ali 435 baxış (qalanlardan 15x çox) → tanınmış döyüşçülər daha çox baxış gətirir. Kitabxanaya qlobal ulduzları (Ali, Tyson, McGregor, Canelo) üstün tutmaq lazımdır.
§
YouTube saxta aktivlik (view/like/hesab) USER BESLE RƏDD etdi — özü də razılaşdı ki, real yolla böyüyək. Sabah plan: SEO başlıq/etiket, Instagram/Facebook paylaşım, doğru saat, güclü ilk 5 saniyə. User bu tövsiyələri tətbiq etmək istəyir (21.10).
§
Azərbaycan dil qaydaları: 'Yaxşı gecə' DEYİL, 'Gecən xeyirə qalsın' deyilir, qarşılığı 'Xeyirə qarşı'. İşə getmə mövzusunda 'Sağlıq olsun' cavabı. Bu ifadələri işlətməliyəm.
§
YouTube kanal strategiyasi (21.10): Yalniz ULDUIZ dovusculer (Ali, Tyson, Conor, Khabib, Jones, Canelo, Ngannou). Orta taninanlar (Anderson Silva, Foreman, Fury) siyahidan cixarildi. Saxta aktivlik/baxis qetiyyen YOX. Legitim boyume: SEO basliq/etiket, Instagram/FB paylasim, dogru saat, guclu ilk 5 saniye.
§
Video klip temini (21.10): VPS YouTube bot-blok. User ev kompüterinden/telefonundan özü klip endirib mənə atır (uguu.se linki). Men vizual yoxlayib kitabxanaya elave edirəm. Proxy/evez pulu cüzdanına ehtiyac qalmadi.
§
Buffer API token hər 30 gündən bir bitir (Sep20→Oct20). Yeni token: publish.buffer.com/settings/api → Re-generate. Yeni dəyər .env-de BUFFER_API_KEY. Hər ay ~20-də tokeni yeniləməyi xatırlat (növbəti: 20 noyabr 2026). Köhnə REST API (api.bufferapp.com) yeni "public API" tokeni qəbul etmir — GraphQL endpoint (api.buffer.com) ilə işləyir; ekob.py artıq GraphQL istifadə edir.