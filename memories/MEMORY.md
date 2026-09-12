User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
agent.js deploy: Node.js regex'lərə diqqət (escape korlanması), syntax yoxla node -c ilə. Səsli mesaj transkripsiya + media analizi aktivdir.
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları (VPS PM2): EANA (Hermes persona, 4 üzv) + Bizim sinif (Həsən müəllim persona, 18 şagird). agent.js. Aynur=Tofiq Ramazanlı 0515027812. YALNIZ Elbrus+Almaz sinifkom idi.
§
5 Beyin botu (VPS Docker): 4 AI, meta-orchestrator. /root/5beyin-bot/. .env gözləyir. Fallback yox — xəta mesajı qaytarır.
§
OpenRouter WSL+VPS. Model: deepseek/deepseek-v4-flash (WSL), openai/gpt-4o-mini (WhatsApp). User prefers Gemini for natural Azerbaijani, OpenRouter temporary.
§
5 Beyin fallback: AI modeli uğursuz olanda başqa modelə keçmir — sadəcə xəta mesajı göstərir. Hər AI yalnız öz modeli ilə cavab verir. (Səhvən fallback əlavə etmişdim, düzəltdim.)
§
Telegram gateway conflict fix: WSL+VPS eyni bot token ilə polling edəndə 'other getUpdates request' xətası. Həll: (1) VPS-də WhatsApp-ı söndür (hermes config set whatsapp.enabled false) - əgər gateway startını bloklayırsa, (2) TELEGRAM_BOT_TOKEN və OPENROUTER_API_KEY-i WSL .env-dən VPS .env-yə kopyala, (3) VPS gateway restart, (4) WSL gateway stop (hermes gateway stop). Yalnız bir instance Telegram-a qoşulsun.
§
User insists discuss-before-act: 'hələ heç nə etmə, sadəcə müzakirə'. Do NOT make code changes without explicit ok even if fix seems obvious.