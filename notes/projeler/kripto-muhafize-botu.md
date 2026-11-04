# Kripto Mühafizə Botu

**Tarix:** 03.11.2026
**Server:** VPS-2 (77.42.37.230)
**Yol:** /root/futures-bot/bot.py
**Systemd:** futures-test.service (aktiv, 24.10.2026-dən)
**SSH:** root@77.42.37.230

## Strategiya
- Deterministik qaydalar (OpenAI olmadan)
- İndikatorlar: RSI (14), MACD (12/26/9), ADX (14), ATR (14)
- **Koinlər:** BTC/USDT, ETH/USDT, SOL/USDT (BNB çıxarıldı — 8/0 uduzurdu)
- **Mövqe:** 100 USDT marja, 2x leverage
- **İstiqamət:** LONG + SHORT (sıx filter — 03.11 + 04.11 iki dəfə tənzimləndi)
- **Giriş şərtləri (04.11 son versiya):** ADX 25-60, Həcm >1.2x, RSI 30-70, MACD kəsişməsi + 24h trend ±1.5% + qiymət ortalamadan düzgün tərəfdə + histogram momentum
- **Çıxış:** SL=2.5x ATR, TP=5.0x ATR, Trailing 3%/1.5%, deterministik erkən çıxış (RSI+MACD)

## Hesabat
- Telegram: 08:00 / 16:00 / 22:00 AZ (bot özü göndərir)
- Hermes monitor: hər gün 10:00 AZ (səssiz sağlamlıq yoxlaması, problem olsa xəbərdarlıq)
- Hermes günlük hesabat: hər gün **22:00 AZ** (məcburi — qazanc/zərər, balans, son əməliyyatlar)

## Nəticə (keçmiş)
- 72 əməliyyat, 37.5% uğur, -1.69 USDT (virtual, 2+ ay)
- BNB səbəbiylə zərər (çıxarıldı)

## İdarəetmə
- `systemctl restart futures-test.service` — restart
- `journalctl -u futures-test.service -n 50 --no-pager` — log
- `/root/futures-bot/state.json` — cari durum
- `/root/futures-bot/bot.py` — kod
- `/root/futures-bot/.env` — tokenlər