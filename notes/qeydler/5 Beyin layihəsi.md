# "5 Beyin" Layihəsi — Tam Xülasə (Yenilənmiş)

**Yenilənmə tarixi:** 12.09.2026
**Status:** Docker image ready, .env faylı gözləyir

## 1. Layihənin Məqsədi

Telegram-da tək istifadəçi (Ebu) üçün 4 fərqli süni intellekt modelinin (ChatGPT, Gemini, DeepSeek, Claude) eyni qrup çatında sərbəst, təbii dost söhbəti formatında iştirak etdiyi bir sistem.

## 2. Ümumi Memarlıq

- **Platform:** Telegram bot (`@beshbeyin_bot`), qrup adı "5 Beyin"
- **Backend:** Python (python-telegram-bot kitabxanası), tək fayl (`bot.py`)
- **Hosting:** Hetzner VPS, Docker konteyner
- **Qovluq:** `/root/5beyin-bot/`
- **İzolyasiya:** Ayrı Docker konteyner, ayrı `.env`

## 4. Əlavə Olunan 8 Təkmilləşdirmə

### ✅ 1. Xərc Nəzarəti (Cost Tracking)
- Hər API çağırışı üçün token sayı və dəyəri `cost_log.txt`-ə yazılır
- `DAILY_COST_LIMIT` (default $2.00) dəyişəni ilə günlük limit tətbiq olunur
- `/stats` əmri ilə cari xərc görünür
- Gemini Free Tier olduğu üçün onun xərci 0 hesablanır

### ✅ 2. Səhv İdarəsi (Fallback Chain)
- Hər AI çağırışı uğursuz olsa, digər modellərə keçid edilir
- Fallback sırası: OpenAI → Anthropic → Google → DeepSeek
- Hər addım loglanır, xərc qeyd olunur
- Bütün modullar düşsə, "Bütün AI-lər müvəffəqiyyətsiz oldu" mesajı qayıdır

### ✅ 3. Avtomatik Yaddaş (Auto-Memory Extraction)
- Hər 5 istifadəçi mesajından sonra Gemini ilə avtomatik fakt çıxarılır
- Çıxarılan faktlar `memory.txt`-ə əlavə olunur
- Faktlar bütün gələcək söhbətlərdə sistem promptuna daxil edilir

### ✅ 4. @Mention Dəstəyi (AI Seçiminə Nəzarət)
- `@Çati`, `@Gemi`, `@Depi`, `@Klodi` yazmaqla həmin AI məcburi seçilir
- Bir neçə AI-ni eyni anda çağırmaq olar (maksimum 3)

### ✅ 5. Axtarış (Search)
- `/search <söz>` əmri ilə `memory.txt` və son 30 mesajda axtarış
- Həm AI cavabları, həm də istifadəçi mesajları axtarılır

### ✅ 6. Geniş Kontekst (50 mesaj)
- Kontekst ölçüsü 15-dən 50-yə qaldırıldı
- AI-lərə son 15 mesaj ötürülür (token limiti səbəbindən optimal)

### ✅ 7. İcazə / Təhlükəsizlik (Auth Whitelist)
- `ALLOWED_USER_IDS` dəyişəni ilə məhdudiyyət
- Yalnız icazə verilən Telegram user ID-ləri botu istifadə edə bilər

### ✅ 8. Standart Əmrlər
- `/start` — Giriş mesajı
- `/help` — Kömək, bütün əmrlərin siyahısı
- `/search <söz>` — Axtarış
- `/stats` — Xərc statistikası
- `/debate <mövzu>` — Debate rejimi
- `xatırlat: GG.AA.İİİİ SS:DD mətn` — Xatırlatma
- `yadda saxla: fakt` — Əl ilə yaddaş

## 5. Deploy üçün tələb olunan .env faylı

```
TELEGRAM_BOT_TOKEN=your_token_here
ALLOWED_USER_IDS=123456789
OPENAI_API_KEY=...
GEMINI_API_KEY=...
DEEPSEEK_API_KEY=...
ANTHROPIC_API_KEY=...
DAILY_COST_LIMIT=2.0
```

## 6. Deploy Əmrləri

```bash
docker stop 5beyin-bot 2>/dev/null; docker rm 5beyin-bot 2>/dev/null
docker build -t 5beyin-bot .
docker run -d --name 5beyin-bot --env-file .env \
  -v /root/5beyin-bot/memory.txt:/app/data/memory.txt \
  -v /root/5beyin-bot/reminders.txt:/app/data/reminders.txt \
  -v /root/5beyin-bot/cost_log.txt:/app/data/cost_log.txt \
  --restart unless-stopped 5beyin-bot
```

## 7. Hermes (Meta-Orchestrator) Rolu

- Hermes (mən) bu layihənin meta-orchestrator-uyam
- Kod, konfiqurasiya və deploy idarəçiliyi məndədir
- Həm WSL-dən, həm də VPS-dən istənilən dəyişiklik edilə bilər
- Bütün qeydlər Obsidian vault və GitHub `hermes-config` reposunda saxlanılır