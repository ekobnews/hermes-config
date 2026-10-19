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