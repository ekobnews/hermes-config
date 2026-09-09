Elbrus Bağırov. Runs EKOB NEWS (Telegram/FB/IG). GitHub: ekobnews (ebuabu79@gmail.com). Obsidian vault: C:\Users\ELBRUS\Documents\hermes-notes. Prefers Azerbaijani, direct no-filler responses. Needs step-by-step numbered instructions for browser tasks. When browser fails, switch to terminal/PowerShell immediately. For GitHub repo via device flow, use Python urllib (not shell text manipulation) to avoid token truncation.
§
Hetzner VPS (77.42.37.230, CX23, 4GB, Ubuntu 26.04): runs Hermes Agent with Telegram gateway (24/7 systemd). EKOB NEWS bot runs on Railway, NOT on this VPS.
§
EKOB NEWS bot: monitors Telegram + RSS, uses Claude to rewrite news in Azerbaijani, publishes via Telethon (TG) + Buffer API (FB/IG).
§
VPS (77.42.37.230, CX23, 4GB, Ubuntu 26.04): runs Hermes Agent (Telegram gateway 24/7 systemd) + EANA WhatsApp bot. Google Gemini 2.5 Flash API key aktiv (AI Studio pulsuz). WhatsApp bot Gemini 2.5 Flash ilə işləyir.
§
Obsidian notes cloned on VPS at /root/hermes-config/notes/ — auto-pull hər 10 dəqiqə. VPS Hermes ora baxa bilər.
§
User wants the EANA WhatsApp bot to speak in completely natural, human-like Azerbaijani — no robotic/formal tone, no unnecessary questions at end of replies. Prefers Gemini over gpt-4o-mini for natural tone.