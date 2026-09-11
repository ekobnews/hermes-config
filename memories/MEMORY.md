User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
WhatsApp Bot (VPS 95.217.157.137, PM2 whatsapp-agent): Çox-qruplu sistem. 1) EANA: Hermes persona (Abu, Anka, Nayka, Ayan). 2) Bizim sinif: Həsən müəllim persona (1985-1995 məzunları, 'Bir salxım üzüm' kitabı, İlahə 'Allahın bacısı qızı', Almaz/Elbrus sinifkomlar, mərhum müəllimlər: Mehparə, Bəyaz, Sevil). 2.5-4s typing delay. Audio/video/şəkil/link hər iki qrupda aktiv.
§
agent.js deploy: Node.js regex'lərə diqqət (escape korlanması), syntax yoxla node -c ilə. Səsli mesaj transkripsiya + media analizi aktivdir.
§
OpenRouter hər iki maşında (WSL və VPS 77.42.37.230) yenidən qurulub, işləyir. Model: deepseek/deepseek-v4-flash via openrouter.
§
5 Beyin layihəsi: Telegram-da 4 AI agent (Çati-GPT4o, Gemi-Gemini3.6flash, Depi-DeepSeek, Klodi-Claude-sonnet4-6) + Ebu (istifadəçi). Bot: @beshbeyin_bot. Host: Hetzner VPS, Docker, /root/5beyin-bot/. Python-telegram-bot. Modullar: profil, yaddaş, xatırlatma, şəkil/PDF analiz, səsli mesaj (Whisper+TTS), debate rejimi. Reaction tanıma test edilir. Link/URL oxuma, real insan qoşulması, video analiz hələ yoxdur.
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.