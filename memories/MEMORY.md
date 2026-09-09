Lokal (WSL) hermes-gateway dayandırıldı və disable edildi — VPS-dəki gateway təkbaşına Telegram polling edir (conflict olmasın deyə).
§
User prefers problems fixed in one shot rather than iterative trial-and-error. When debugging, exhaust root-cause analysis before attempting fixes. User is Azerbaijani speaker, wants direct no-filler responses in Azərbaycan dili. Frustrated by: formal 'necə kömək edə bilərəm' tone, questions at end of every message, robotic/客服 style. Wants: səmimi/dost kimi tone, qısa cavablar (1-2 cümlə), sual ancaq həqiqətən lazım olanda.
§
Two GitHub repos under ekobnews: github.com/ekobnews/hermes-config (config + notes) and github.com/ekobnews/ekob-news-bot (bot code). Both pushed successfully Sep 5-6 2026.
§
Obsidian vault: /mnt/c/Users/ELBRUS/Documents/hermes-notes (Windows). Subdirs: gundelik/, projeler/, notlar/, qeydler/. Synced to GitHub via hermes-config repo notes/. VPS-ə də klonlanıb /root/hermes-config/notes/ — auto-pull hər 10 dəq. Sync script: hermes-config/scripts/sync-notes.sh.
§
EANA WhatsApp qrupu (994707551301-1569520529@g.us). Üzvlər: Elbrus/Abu (0707551301, 15.05.1979, DSMF Pensiya təyinatı şöbə müdiri). Alidə/Anka (0552270131, 19.07.1981, 96 saylı bağçada tərbiyəçi). Nailə/Nayka (0702442280, 05.11.2002, polis serjantı, ASAN). Ayan (0553272013, 31.12.2006, ADU erməni tərcümə). Nayka Tural (baş leytenant, Daxili Qoşunlar) ilə evli, ayrı ev. Bot VPS 95.217.157.137, PM2 whatsapp-agent, gpt-4o-mini (temp 0.3). BÜTÜN mesajlara cavab verir (trigger yoxdur). Yaddaş: memory.js + memory_store.json (max 200 fakt). Tarix/saat: Asia/Baku. Link: oembed+OG meta. Video: ffmpeg frame extraction. Tərz: səmimi, təbii, sualsız.
§
Full session sync active (6 Sep 2026): sqlite3 backup+merge bidirectional between WSL↔VPS every 5min (system crontab). Scripts: ~/.hermes/scripts/sync-sessions.sh, sync-sessions.py, backup-db.py. Memory sync: ~/.hermes/scripts/sync-memory.sh every 2min. Hər iki tərəf eyni sessions+memory görür.