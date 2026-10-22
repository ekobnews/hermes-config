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
qa
§
Yükləmə axını (21.10): YouTube OAuth tokeni Testing rejimində 7 günə ölür. Videoları user özü yükləyir (YouTube Studio-ya əl ilə). Mənim işim: məzmun hazırlamaq (montaj, musiqi, vizual yoxlama) + başlıq/təsvir hazırlamaq. User uguu.se/GDrive ilə mənbə faylları göndərir, mən emal edib hazır video kimi geri qaytarıram. Bu, VPS-dən YouTube blokunu keçməyin ən praktik yoludur.
§
WSL Hermes çökür — RAM çatışmazlığı (mem verified, user agreed). Yükəliş EKOB STUDIO videoları üçün: VPS-də 25 dəq video kodlamaq saatlar çəkir (GPU yox). Bu işi local WSL notebook-da edir. Upload: YouTube Studio əl ilə (OAuth token ölür). Fayl ötürmə: uguu.se <20MB, Google Drive folder (hər ölçü) üstün. ElevenLabs Music API 429 system_busy — 3 retry 45/90/135san.