# Hermes Config — Elbrus

Hermes Agent konfiqurasiya faylları. WSL (Ubuntu 26.04) üzərində işləyir.

## Struktur

```
hermes-config/
├── config.yaml          # Hermes əsas konfiqurasiyası
├── SOUL.md              # SOUL promptu
├── memories/
│   ├── MEMORY.md        # Hermes-in yaddaş qeydləri
│   └── USER.md          # İstifadəçi profili
├── gateway/             # Gateway konfiqurasiyası
├── vps-setup.md         # VPS qurulum haqqında qeydlər
└── .gitignore
```

## VPS

EKOB NEWS bot 95.217.157.137 ünvanında işləyir (Hetzner CX23, 4GB RAM).
Hermes orada Telegram gateway ilə 24/7 aktivdir.

## Bərpa

Yeni maşında bərpa üçün:

```bash
git clone git@github.com:ekobnews/hermes-config.git ~/.hermes-config
cp ~/.hermes-config/config.yaml ~/.hermes/config.yaml
# .env faylını əl ilə yarat
```