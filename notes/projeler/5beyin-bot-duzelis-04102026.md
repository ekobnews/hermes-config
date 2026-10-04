# 5 Beyin Bot — Düzəlişlər (04.10.2026)

## Problem
- Klodi (Claude) və Depi (DeepSeek) cavab vermirdi
- Səbəb: Hər iki model təqaüdə çıxmışdı (retired)

## Düzəlişlər
- **Klodi:** `claude-sonnet-4-20250514` → `claude-sonnet-5` (Anthropic API)
- **Depi:** `deepseek-chat` → `deepseek-flash` (DeepSeek API)
- **Conflict:** VPS-də ikinci instance (host-da birbaşa işləyən bot) öldürüldü, yalnız Docker-də qaldı

## Hazırki vəziyyət
- ✅ Çati (GPT-4o) — işləyir
- ✅ Gemi (Gemini 2.5 flash) — işləyir
- ✅ Depi (DeepSeek Flash) — işləyir
- ✅ Klodi (Claude Sonnet 5) — işləyir

## Xərc məlumatları
- `deepseek-flash` giriş $0.27/M, çıxış $1.10/M (deepseek-chat ilə eyni qiymət)
- `claude-sonnet-5` giriş $3/M, çıxış $15/M (əvvəlkindən baha deyil, Sonnet 4-6 ilə eyni)