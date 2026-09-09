Lokal (WSL) hermes-gateway dayandırıldı və disable edildi — VPS-dəki gateway təkbaşına Telegram polling edir (conflict olmasın deyə).
§
User prefers problems fixed in one shot rather than iterative trial-and-error. When debugging, exhaust root-cause analysis before attempting fixes.
§
Two GitHub repos under ekobnews: github.com/ekobnews/hermes-config (config + notes) and github.com/ekobnews/ekob-news-bot (bot code). Both pushed successfully Sep 5-6 2026.
§
Obsidian vault: /mnt/c/Users/ELBRUS/Documents/hermes-notes (Windows). Subdirs: gundelik/, projeler/, notlar/, qeydler/. Synced to GitHub via hermes-config repo notes/. VPS-ə də klonlanıb /root/hermes-config/notes/ — auto-pull hər 10 dəq. Sync script: hermes-config/scripts/sync-notes.sh.
§
EANA WhatsApp qrupu (994707551301-1569520529@g.us). Üzvlər: Elbrus/Abu (0707551301, 15.05.1979, DSMF Pensiya təyinatı şöbə müdiri). Alidə/Anka (0552270131, 19.07.1981, 96 saylı bağçada tərbiyəçi). Nailə/Nayka (0702442280, 05.11.2002, polis serjantı, ASAN). Ayan (0553272013, 31.12.2006, ADU erməni tərcümə). Nayka Tural (baş leytenant, Daxili Qoşunlar) ilə evli, ayrı ev. Bot OpenAI gpt-4o-mini, qrupda yalnız "Hermes" trigger. Tərz: səmimi, təbii.
§
Full session sync active (6 Sep 2026): sqlite3 backup+merge bidirectional between WSL↔VPS every 5min (system crontab). Scripts: ~/.hermes/scripts/sync-sessions.sh, sync-sessions.py, backup-db.py. Memory sync: ~/.hermes/scripts/sync-memory.sh every 2min. Hər iki tərəf eyni sessions+memory görür.