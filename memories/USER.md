Prefers Azerbaijani; direct, concise, no-filler responses.
§
Elbrus Bağırov. Runs EKOB NEWS (Telegram/FB/IG).
§
Self-hosted Hetzner VPS (95.217.157.137, CX23, 4GB, Ubuntu 26.04). Hermes Agent + EKOB NEWS bot as 24/7 systemd services.
§
EKOB NEWS bot: monitors Telegram + RSS, uses Claude to rewrite news in Azerbaijani, publishes via Telethon (TG) + Buffer API (FB/IG).
§
VPS (95.217.157.137): Hermes gateway uses OpenAI API key (OPENAI_API_KEY in .env). Local WSL gateway stopped+disabled to prevent Telegram polling conflict. Primary model: gpt-4o-mini via custom provider (openai_chat transport, https://api.openai.com/v1). Gemini API key depleted (prepaid credits ran out).
§
GitHub: ekobnews / ebuabu79@gmail.com. First-time GitHub user — prefers step-by-step guidance when learning new tools.