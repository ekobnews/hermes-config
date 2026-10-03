#!/bin/bash
# Bərpa üçün təlimat
# 1. Şifrəni backup-password.txt faylından oxu
# 2. openssl ilə deşifrə et
# 3. tar ilə aç

PASS=$(cat /root/hermes-config/notes/backup-password.txt 2>/dev/null)
if [ -z "$PASS" ]; then
    echo "XƏTA: Şifrə faylı tapılmadı!"
    exit 1
fi

openssl enc -d -aes-256-cbc -in "$1" -out /tmp/ekob-restored.tar.gz -pass pass:"$PASS" 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Deşifrə olundu: /tmp/ekob-restored.tar.gz"
    echo "İçində: ekob_news/.env, .hermes/.env, .hermes/config.yaml, ekob_news/ekob_dash.db"
    echo "Çıxartmaq üçün: cd / && sudo tar xzf /tmp/ekob-restored.tar.gz"
else
    echo "❌ Deşifrə xətası!"
fi