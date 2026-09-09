Lokal WSL hermes-gateway dayandırıldı/disable edildi — VPS-dəki gateway təkbaşına Telegram polling edir.
§
User is Azerbaijani speaker, wants direct no-filler Azərbaycan dilində responses. Frustrated by: formal tone, 'necə kömək edə bilərəm', questions at end of every message, robotic/客服 style, süni 'darıxdım/əla/mükəmməl'. Wants: səmimi/dost kimi, qısa 1-2 cümlə, sual only when genuinely needed, heç vaxt cümlə sonunda sual vermə.
§
Two GitHub repos under ekobnews: github.com/ekobnews/hermes-config (config + notes) and github.com/ekobnews/ekob-news-bot (bot code). Both pushed successfully Sep 5-6 2026.
§
Obsidian vault: /mnt/c/Users/ELBRUS/Documents/hermes-notes (Windows). Subdirs: gundelik/, projeler/, notlar/, qeydler/. Synced to GitHub via hermes-config repo notes/. VPS-ə də klonlanıb /root/hermes-config/notes/ — auto-pull hər 10 dəq. Sync script: hermes-config/scripts/sync-notes.sh.
§
EANA WhatsApp bot: VPS 95.217.157.137, PM2 whatsapp-agent, gpt-4o-mini temp 0.3, trigger yox (hər mesaja cavab), yaddaş memory.js+memory_store.json (max 200 fakt), tarix/saat Asia/Baku hər sorğuda. Link: YouTube oembed+OG meta. Video: ffmpeg frame extraction. Qrup qoşulub: 994707551301-1569520529@g.us. agent.js edit: Python execute_code ilə Node.js regex yazma escape korlayır — scp ilə göndər, node -c ilə syntax yoxla.
§
Full session sync active (6 Sep 2026): sqlite3 backup+merge bidirectional between WSL↔VPS every 5min (system crontab). Scripts: ~/.hermes/scripts/sync-sessions.sh, sync-sessions.py, backup-db.py. Memory sync: ~/.hermes/scripts/sync-memory.sh every 2min. Hər iki tərəf eyni sessions+memory görür.