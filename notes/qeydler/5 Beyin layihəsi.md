# "5 Beyin" Layihəsi — Tam Xülasə

**Yenilənmə tarixi:** 12.09.2026

## 1. Layihənin Məqsədi

Telegram-da tək istifadəçi (Ebu) üçün 4 fərqli süni intellekt modelinin (ChatGPT, Gemini, DeepSeek, Claude) eyni qrup çatında sərbəst, təbii dost söhbəti formatında iştirak etdiyi bir sistem. Məqsəd — istifadəçinin istənilən mövzunu "5 dost" ilə (özü + 4 AI) müzakirə edə bilməsi, klassik bir AI-dən sual-cavab formatında deyil.

## 2. Ümumi Memarlıq

- **Platform:** Telegram bot (username: `@beshbeyin_bot`), qrup adı "5 Beyin"
- **Backend:** Python (python-telegram-bot kitabxanası), tək fayl (`bot.py`)
- **Hosting:** Hetzner VPS, Docker konteyner
- **Qovluq:** `/root/5beyin-bot/`
- **İzolyasiya:** Eyni serverdəki kripto trade botundan ayrı Docker konteyner, ayrı `.env`, ayrı qovluq
- **Restart:** `--restart unless-stopped`

### Fayllar
- `bot.py` — əsas kod
- `Dockerfile` — Docker build
- `requirements.txt` — Python dependency-lər
- `.env` — API açarları
- `profile.txt` — istifadəçi profili (volume mount)
- `memory.txt` — uzunmüddətli yaddaş (volume mount)
- `reminders.txt` — xatırlatmalar (volume mount)

### API açarları (.env)
- `TELEGRAM_BOT_TOKEN`, `OPENAI_API_KEY`, `GEMINI_API_KEY`, `DEEPSEEK_API_KEY`, `ANTHROPIC_API_KEY`

## 3. AI-lərin Təmsili

| Görünən ad | Emoji | Əsl model | TTS səsi | Güclü tərəf |
|---|---|---|---|---|
| Çati | 🤖 | OpenAI GPT-4o | alloy | yaradıcı, fikir, hekayə |
| Gemi | 🔷 | Google Gemini (gemini-2.5-flash) | nova | analiz, data, araşdırma |
| Depi | 🐋 | DeepSeek (deepseek-chat) | echo | kod, texniki, riyaziyyat |
| Klodi | 🟠 | Anthropic Claude (claude-sonnet-4-6) | shimmer | yazı, təhlil, fəlsəfə |

İstifadəçiyə müraciət: **Ebu**

## 4. Söhbət Məntiqi

1. İstifadəçi mesaj yazır
2. Sistem keyword əsaslı + təsadüfi amillə 2-3 AI seçir
3. AI-lər **ardıcıl** cavab verir — hər biri əvvəlkilərin cavabını görür
4. Hər AI mesaj başına 1 dəfə cavab verir
5. Son 10-15 mesaj kontekst saxlanılır

## 5. Modullar

### Modul 1 — Şəxsi Profil
- `profile.txt` faylında, Docker build zamanı konteynerə kopyalanır
- Sistem promptuna avtomatik əlavə olunur

### Modul 2 — Uzunmüddətli Yaddaş
- `memory.txt` faylında (volume mount ilə daimi)
- Tetik: "yadda saxla:" ifadəsi
- Fayla yazılır, təsdiq göndərilir, AI-lərə sorğu getmir

### Modul 3 — Xatırlatma/Scheduler
- `reminders.txt` faylında JSON formatında (volume mount ilə daimi)
- Format: `xatırlat: GG.AA.İİİİ SS:DD mətn`
- Fon prosesi hər 30 saniyədə yoxlayır
- Vaxt zonası: Bakı vaxtı (UTC+4), server UTC-də

### Modul 4 — Şəkil/Sənəd Təhlili
- **Şəkil:** Vision dəstəkləyən 2 təsadüfi AI (ChatGPT, Gemini, Claude arasından)
- **PDF:** pypdf ilə mətn çıxarılır (ilk 10 səhifə, 6000 simvol), AI-lərə göndərilir
- DeepSeek vision dəstəkləmir, PDF moduluna daxil deyil

### Modul 5 — Səsli Mesaj Dəstəyi
- **Giriş:** OpenAI Whisper API ilə mətnə çevrilir
- **Çıxış:** "səsli cavab ver" ifadəsi olduqda TTS ilə səsli mesaj

### Debate Rejimi
- Tetik: "debat et: mövzu"
- 4 AI iştirak edir, 2 lehinə + 2 əleyhinə (təsadüfi)
- ✅ LEHİNƏ / ❌ ƏLEYHİNƏ etiketi
- Tək mesajlıq keçid, sonra normal rejim

## 6. Yarım Qalan / Test Edilən

### Reaction Tanıma
- `MessageReactionHandler` əlavə olunub
- Reaction-lar `chat_histories`-ə yazılır
- **Status:** tətbiq olunub, real test gözləyir

## 7. Gələcək Planlar

- Link/URL məzmunu oxuma
- Real insanların qoşulması (çoxistifadəçi dəstəyi)
- Video təhlili (yalnız Gemini dəstəkləyir)
- REST API formatına keçid (Telegram-dan asılı olmayan)

## 8. Deploy Əmrləri

```bash
docker stop 5beyin-bot && docker rm 5beyin-bot
docker build -t 5beyin-bot .
docker run -d --name 5beyin-bot --env-file .env \
  -v /root/5beyin-bot/memory.txt:/app/memory.txt \
  -v /root/5beyin-bot/reminders.txt:/app/reminders.txt \
  --restart unless-stopped 5beyin-bot
```

## 9. Status

✅ Tamamlanan: profil, yaddaş, xatırlatma, şəkil/PDF analiz, səsli mesaj, debate
🔄 Testdə: reaction tanıma
❌ Hələ yox: link oxuma, çoxistifadəçi, video analiz, REST API