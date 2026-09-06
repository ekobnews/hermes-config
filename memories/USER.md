Elbrus Bağırov. Runs EKOB NEWS (Telegram/FB/IG). GitHub: ekobnews (ebuabu79@gmail.com). Obsidian vault: C:\Users\ELBRUS\Documents\hermes-notes. Prefers Azerbaijani, direct no-filler responses. Needs step-by-step numbered instructions for browser tasks. When browser fails, switch to terminal/PowerShell immediately. For GitHub repo via device flow, use Python urllib (not shell text manipulation) to avoid token truncation.
§
Hetzner VPS (77.42.37.230, CX23, 4GB, Ubuntu 26.04): runs Hermes Agent with Telegram gateway (24/7 systemd). EKOB NEWS bot runs on Railway, NOT on this VPS.
§
EKOB NEWS bot: monitors Telegram + RSS, uses Claude to rewrite news in Azerbaijani, publishes via Telethon (TG) + Buffer API (FB/IG).
§
VPS (77.42.37.230): Hermes gateway uses OpenAI API key (OPENAI_API_KEY in .env). Local WSL gateway stopped+disabled to prevent Telegram polling conflict. Primary model: gpt-4o-mini via custom provider (openai_chat transport, https://api.openai.com/v1). Gemini API key depleted (prepaid credits ran out).
§
EKOB NEWS bot runs on Railway (not VPS). VPS (77.42.37.230) runs Hermes Agent only.
§
Obsidian notes cloned on VPS at /root/hermes-config/notes/ — auto-pull hər 10 dəqiqə. VPS Hermes ora baxa bilər.