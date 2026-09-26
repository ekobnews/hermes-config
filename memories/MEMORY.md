User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları (VPS PM2 whatsapp-agent): EANA (Hermes persona, 4 ailə üzvü) + Bizim sinif (Həsən müəllim persona, 18 şagird). Hər ikisi agent.js-də hardcoded. 2.5-4s typing delay. Audio/video/şəkil/link aktiv.
§
5 Beyin Telegram botu (VPS Docker): 4 AI (Çati-GPT4o, Gemi-Gemini2.5flash, Depi-DeepSeek, Klodi-Claude). Meta-orchestrator rolu bəndə. 8 təkmilləşdirmə: xərc, fallback, auto-memory, @mention, search, kontekst, auth, əmrlər. /root/5beyin-bot/. .env gözləyir.
§
EKOB NEWS AI redaktor GPT-4o-mini (OpenRouter, Claude fallback). OPENROUTER_API_KEY .env-də yox idi, Hermes açarı əlavə edildi. Buffer LimitReachedError (Free limiti doldu) FB/IG/TT dayandırıb. Həll üçün Buffer Essentials plan.
§
EKOB NEWS Pipeline: (1) GPT-4o-mini OpenRouter əsas AI, Claude fallback. (2) Uguu.se hosting (Catbox sınmış). (3) Keepalive: RSS-də client.get_me() + cron hər 2 saat restart. (4) Ölü @username bot crash edir - yoxla əvvəl. (5) STRING_SESSION .env-də də olmalı. (6) Buffer FB token 60 günlük - browser yenidən qoşul (post.status=error). (7) Analytics cron: daily 1df96361be3a, weekly 28fa91ac61ec, 02:00 UTC (=06:00 AZ).
§
EKOB NEWS 26.09: Telegram mənbə (8): @Axaraz, @eco_expert, @BanksterShow, @expertonomics, @aipost, @WatcherGuru, @NatGeoSociety, @wowwvd. RSS (4): BBC, InterestingEngineering, tr.beincrypto.com/feed/, news.google.com/rss. AI: GPT-4o-mini (Claude fallback). Keepalive: hər 30 dəq. Analytics: gündəlik 06:00 AZ + həftəlik Bazar 06:00 AZ.