User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
WSL hermes-gateway disabled — VPS gateway tək polling edir. Session+memory sync WSL↔VPS hər 5/2 dəq (crontab).
§
User's triple-save pattern: hər dəfə yeni layihə/sistem/config haqqında məlumat verəndə, onu 1) Hermes memory-ə, 2) Obsidian vault-a (qeydler/), 3) GitHub hermes-config reposuna qeyd et. Obsidian vault həm WSL-də (/mnt/c/...), həm də hermes-config/notes/ qovluğunda sinxron saxlanılır.
§
WhatsApp botları VPS-1 PM2-də: EANA (4 ailə) + Bizim sinif (18 şagird). 2.5-4s typing delay.
§
5 Beyin botu VPS-2 77.42.37.230 Docker-da: 4 AI+meta-orchestrator, /root/5beyin-bot/
§
İş haqqında danışanda birbaşa. 'davam edək?' çox vaxt söhbəti davam etdirmək deməkdir — dərhal işə atılma, əvvəl hal-əhval soruş.
§
EKOB NEWS: Telegram→AI→TG+Buffer. ElevenLabs API VPS-1-də (/root/ekob_news/.env). HeyGen AZ video planı.
§
User həm WSL, həm VPS agentlərini qarşılıqlı işlədir — fikirləri birimizdən o birinə göndərir, konsensus gözləyir. İki agentin razılaşdığı həllərə daha çox güvənir.
§
Video render: audio-dan qısa olmamalıdır. -t parametri ffprobe dəqiq dəyərindən (kəsilməmiş) istifadə et, yaxud -shortest əvəzinə a:duration=first ilə audio boyu get.
§
EKOB STUDIO YT: 1) QRXYzmCVVLw (18.10), 2) znBIwVkSzVM (25.10), 3) HD6B5q0r-lk (31.10, '5 Saniyənin Sirri'). API upload: podcast_work/upload_youtube.py. Token invalid_grant → youtube_token.json sil, OAuth təzələ.
§
WSL env quirk: background process-lərdə ~/.hermes/bin PATH-də olmur (uv tapılmır) — tam yolla çağır. uv venv-lərində pip yoxdur, uv pip install istifadə et.
§
Podcast bg music: sakit piano (mixkit), 4% səs, loop stream_loop -1 + amix.
§
FIGHT SHORTS YT kanal ID: UC-GAoyXGXGjbn_vwdvdtmdA (@fightshorts2026). 31.10.2026 OAuth refresh token invalid_grant — youtube_auth.py ilə OAuth təzələmək lazımdır. Statistikanı public innertube API (youtubei/v1/browse) ilə də çəkmək olar: shorts grid-də view counts var.
§
Crypto trading bot (fyuçers, Binance Futures): VPS-2 77.42.37.230-da işləyir. Systemd servis: futures-test.service. Python bot.py — CCXT + OpenAI GPT-4o-mini + python-telegram-bot. Koinlər: BTC, ETH, SOL, BNB (Gemini-nin dediyi XRP/TRX/FIL/SUI deyil — real bot fərqlidir). Leveraj 3x, marja 100 USDT/əməl. Başlanğıc 1000 USDT, cari ~996.87 USDT (72 əməl, 37.5% uğur, -1.69 USDT). BNB 0% uğur (8/0, -5.95 USDT). state.json-da saxlanılır. İnteqrasiya planı: SSH bağlantısı tələb olunur (şifrə lazımdır, SSH açarı işləmir).