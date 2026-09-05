# VPS Setup — EKOB NEWS

**Server**: Hetzner CX23, 4GB RAM, Ubuntu 26.04  
**IP**: 95.217.157.137  
**Hostname**: hermes-vps  

## Services

| Service | Status | Description |
|---------|--------|-------------|
| Hermes Agent | systemd (24/7) | AI agent with Telegram gateway |
| EKOB NEWS bot | systemd (24/7) | News monitoring + publishing |

## Hermes Gateway

- Platform: Telegram
- Provider: OpenAI API (custom `openai-api` provider)
- Model: `gpt-4o-mini` (openai_chat transport, api.openai.com/v1)
- Fallback providers configured in config.yaml
- .env faylında `OPENAI_API_KEY` var

## EKOB NEWS Bot

- Telegram kanallarını monitor edir
- RSS feed-ləri yoxlayır
- Claude Sonnet 4-5 ilə xəbərləri Azərbaycanca yenidən yazır
- Telegram (Telethon), Facebook/Instagram (Buffer API) paylaşır
- Buffer API 24h rate limitə düşə bilər, Telegram təsirlənmir

## Backup

VPS-ə SSH:
```bash
ssh elbrus@95.217.157.137
```

Mühüm yollar:
- `/home/elbrus/` — bot kodu
- `/home/elbrus/.hermes/` — Hermes konfiqurasiyası
- `/etc/systemd/system/hermes*.service` — systemd xidmətləri