# Backup + Monitoring Sistemi — 03.10.2026

## Risk və Həllər

| Risk | Həll |
|---|---|
| API açarları itərsə | ✅ Şifrəli backup (`ekob-critical-backup-20261003.enc`) |
| Bot çökərsə (xəbərsiz) | ✅ Health check hər 5 dəq + Hermes alert |
| VPS sıfırlanarsa | ✅ Backup + bərpa skripti hazırdır |

## Backup
- **Fayl:** `ekob-critical-backup-20261003.enc`
- **Şifrə:** `backup-password.txt` (eyni repo-da, private)
- **İçində:** `.env` faylları (bütün API açarları), `config.yaml`, `ekob_dash.db`
- **Alqoritm:** AES-256-CBC (openssl)
- **Bərpa:** `restore-backup.sh` skripti ilə

## Monitoring
- **Health check:** `ekob_news/health-check.sh` (cron: hər 5 dəq)
- **Alert:** Hermes cron job (hər 10 dəq) — bot çökərsə restart + bildiriş
- **Restart:** Cron `0 1,3,5,7,9,11,13,15,17,19,21,23` (tək saatlar)

## Cron-lar (crontab -l)
*/10 * * * * /root/hermes-sync/sync-memory.sh
0 1,3,5,7,9,11,13,15,17,19,21,23 * * * systemctl restart ekob-news.service
*/5 * * * * /root/ekob_news/health-check.sh

---
⬆️ [[Ana Səhifə]]