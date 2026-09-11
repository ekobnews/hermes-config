# "5 Beyin" Layihəsi — Yenilənmiş məlumat

**Yenilənmə tarixi:** 12.09.2026
**Bot serveri:** 77.42.37.230 (crypto-bot serveri)
**Bot:** @beshbeyin_bot (Docker konteynerdə)

## Tətbiq olunan 8 təkmilləşdirmə

1. ✅ **Xərc nəzarəti** — cost_log.txt, günlük $2 limit, /stats əmri
2. ✅ **Fallback** — API uğursuz olanda digər model işə düşür
3. ✅ **Auto-memory** — hər 5 mesajdan bir GPT-4o-mini ilə fakt çıxarma
4. ✅ **@Mention** — @Çati @Gemi @Depi @Klodi ilə AI seçimi
5. ✅ **Axtarış** — /search əmri
6. ✅ **Kontekst** — 30 mesaj
7. ✅ **İcazə** — ALLOWED_USER_IDS ağ siyahısı
8. ✅ **Əmrlər** — /start, /help, /search, /stats

## Hermes (meta-orchestrator) rolu

- Mən 5 Beyin layihəsinin meta-orchestrator-uyam
- Həm WSL, həm də VPS üzərindən idarə etmək olar
- Kod: 77.42.37.230 → /root/5beyin-bot/bot.py