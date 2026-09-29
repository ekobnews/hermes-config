User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları (VPS PM2 whatsapp-agent): EANA (Hermes persona, 4 ailə üzvü) + Bizim sinif (Həsən müəllim persona, 18 şagird). Hər ikisi agent.js-də hardcoded. 2.5-4s typing delay. Audio/video/şəkil/link aktiv.
§
5 Beyin Telegram botu (VPS Docker): 4 AI (Çati-GPT4o, Gemi-Gemini2.5flash, Depi-DeepSeek, Klodi-Claude). Meta-orchestrator rolu bəndə. 8 təkmilləşdirmə: xərc, fallback, auto-memory, @mention, search, kontekst, auth, əmrlər. /root/5beyin-bot/. .env gözləyir.
§
EKOB NEWS PWA PORTAL: Emergent.sh (AI full-stack builder, React/Next.js+FastAPI). Öz domen. Kateqoriyalar (8): Yaşıl Tex, İqlim, Təbiət, Eko-həyat, AI, Kripto, İqtisadiyyat, Siyasət. Ticker: BTC,ETH + CSCO,SCHD. API: /api/news, /api/market-prices. Bot bazaya xəbər yazacaq. Logo yaşıl+gümüşü.
§
User qaydası (CRITICAL): Hər hansı kod/config düzəlişi etməzdən əvvəl MÜTLƏQ soruş. Sən deməsən icra etmə. Təsdiq gözlə.
§
EKOB NEWS lesson (28.09): Telethon event handler üçün `chats=` parametri ilə resolve yerinə runtime username filter işlə. `chats=` hər restartda resolve olunur — uğursuz olanda kanal itir. `@client.on(events.NewMessage)` + daxildə `chat.username` yoxlaması daha etibarlıdır.
§
User interested in YouTube Shorts avtomatlaşdırma (fight sports, boxing, MMA). Müzakirə mərhələsindədir, hələ layihə deyil.