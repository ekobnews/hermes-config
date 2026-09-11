User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
agent.js deploy: Node.js regex'lərə diqqət (escape korlanması), syntax yoxla node -c ilə. Səsli mesaj transkripsiya + media analizi aktivdir.
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları (VPS PM2 whatsapp-agent): EANA (Hermes persona, 4 ailə üzvü) + Bizim sinif (Həsən müəllim persona, 18 şagird). Hər ikisi agent.js-də hardcoded. 2.5-4s typing delay. Audio/video/şəkil/link aktiv.
§
5 Beyin Telegram botu (VPS Docker): 4 AI (Çati-GPT4o, Gemi-Gemini2.5flash, Depi-DeepSeek, Klodi-Claude). Meta-orchestrator rolu bəndə. 8 təkmilləşdirmə: xərc, fallback, auto-memory, @mention, search, kontekst, auth, əmrlər. /root/5beyin-bot/. .env gözləyir.
§
OpenRouter WSL+VPS hər ikisində işləyir. Model: deepseek/deepseek-v4-flash.