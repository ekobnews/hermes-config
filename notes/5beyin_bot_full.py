#!/usr/bin/env python3
"""5 Beyin Telegram Bot — 4 AI agent + Ebu"""

import os, sys, json, asyncio, re, textwrap, logging, random
from datetime import datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict, deque

import httpx
from telegram import Update, Document
from telegram.ext import (Application, CommandHandler, MessageHandler,
                          filters, ContextTypes, MessageReactionHandler)

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO, stream=sys.stdout)
log = logging.getLogger(__name__)

BAKU_TZ = timezone(timedelta(hours=4))
DATA_DIR = Path("/app/data")
MEMORY_FILE = DATA_DIR / "memory.txt"
REMINDERS_FILE = DATA_DIR / "reminders.txt"
COST_LOG = DATA_DIR / "cost_log.txt"
PROFILE_FILE = Path("/app/profile.txt")

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED_USERS = set(int(x.strip()) for x in os.environ.get("ALLOWED_USER_IDS","").split(",") if x.strip())
DAILY_COST_LIMIT = float(os.environ.get("DAILY_COST_LIMIT","2.0"))

PRICING = {
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gemini-2.5-flash": {"input": 0.15, "output": 0.60},
    "deepseek-chat": {"input": 0.27, "output": 1.10},
    "claude-sonnet-4-6": {"input": 3.00, "output": 15.00},
}
FREE_MODELS = {"gemini-2.5-flash"}

AI_PERSONS = {
    "cati": {"display_name": "Cati", "emoji": "\U0001f916", "model": "gpt-4o", "provider": "openai",
             "strength": "yaradici, fikir, hekaye", "voice": "alloy", "vision": True,
             "extra": "Sen Cati'sen — yaradici ve ilhamli bir dost."},
    "gemi": {"display_name": "Gemi", "emoji": "\U0001f537", "model": "gemini-2.5-flash", "provider": "google",
             "strength": "analiz, data, arasdirma", "voice": "nova", "vision": True,
             "extra": "Sen Gemi'sen — analitik ve deqiq bir dost."},
    "depi": {"display_name": "Depi", "emoji": "\U0001f40b", "model": "deepseek-chat", "provider": "deepseek",
             "strength": "kod, texniki, riyaziyyat", "voice": "echo", "vision": False,
             "extra": "Sen Depi'sen — texniki ve mentiqli bir dost."},
    "klodi": {"display_name": "Klodi", "emoji": "\U0001f7e0", "model": "claude-sonnet-4-6", "provider": "anthropic",
              "strength": "yazi, tehlil, felsefe", "voice": "shimmer", "vision": True,
              "extra": "Sen Klodi'sen — derinden dusunen bir dost."},
}
AI_KEYS = list(AI_PERSONS.keys())
VISION_KEYS = [k for k, v in AI_PERSONS.items() if v["vision"]]

chat_histories = defaultdict(lambda: deque(maxlen=50))
message_ai_map = {}
user_profile_text = ""
auto_fact_counter = defaultdict(int)

def load_profile():
    global user_profile_text
    try: user_profile_text = PROFILE_FILE.read_text(encoding="utf-8").strip()
    except Exception: user_profile_text = ""

def load_memory():
    try: d = json.loads(MEMORY_FILE.read_text(encoding="utf-8")); return d if isinstance(d,list) else []
    except Exception: return []

def save_memory(facts):
    MEMORY_FILE.write_text(json.dumps(facts, ensure_ascii=False), encoding="utf-8")

def add_memory(fact):
    f = load_memory()
    if fact not in f: f.append(fact); save_memory(f); return True
    return False

def log_cost(model, tin, tout, ok):
    p = PRICING.get(model, {"input":0,"output":0})
    c = (tin/1e6)*p["input"] + (tout/1e6)*p["output"]
    if model in FREE_MODELS: c = 0.0
    now = datetime.now(BAKU_TZ)
    line = f"{now.isoformat()}\t{model}\t{tin}\t{tout}\t{c:.6f}\t{'OK'if ok else 'FAIL'}\n"
    try:
        with open(COST_LOG,"a",encoding="utf-8") as f: f.write(line)
    except Exception: pass
    return c

def get_daily_cost():
    today = datetime.now(BAKU_TZ).strftime("%Y-%m-%d"); total=0.0
    try:
        for l in COST_LOG.read_text(encoding="utf-8").splitlines():
            p=l.split("\t")
            if len(p)>=5 and p[0].startswith(today):
                try: total+=float(p[4])
                except: pass
    except Exception: pass
    return total

def check_cost_limit():
    return get_daily_cost() < DAILY_COST_LIMIT

def load_reminders():
    try: d = json.loads(REMINDERS_FILE.read_text(encoding="utf-8")); return d if isinstance(d,list) else []
    except Exception: return []

def save_reminders(rem):
    REMINDERS_FILE.write_text(json.dumps(rem, ensure_ascii=False), encoding="utf-8")

FALLBACK_ORDER = [
    ("openai","gpt-4o"),("anthropic","claude-sonnet-4-6"),
    ("google","gemini-2.5-flash"),("deepseek","deepseek-chat"),
]

async def call_openai(sys, usr, hist):
    key = os.environ.get("OPENAI_API_KEY","")
    if not key: return "",0,0,False
    msgs = [{"role":"system","content":sys}]
    for h in hist: msgs.append(h)
    msgs.append({"role":"user","content":usr})
    async with httpx.AsyncClient(timeout=60) as cl:
        r = await cl.post("https://api.openai.com/v1/chat/completions",
            headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
            json={"model":"gpt-4o","messages":msgs,"max_tokens":1024})
        d = r.json()
        if "choices" not in d: return "",0,0,False
        u = d.get("usage",{})
        return d["choices"][0]["message"]["content"], u.get("prompt_tokens",0), u.get("completion_tokens",0), True

async def call_gemini(sys, usr, hist):
    key = os.environ.get("GEMINI_API_KEY","")
    if not key: return "",0,0,False
    full = sys + "\n\n"
    for h in hist[-10:]: full += f'{h["role"]}: {h["content"]}\n'
    full += f"user: {usr}"
    async with httpx.AsyncClient(timeout=60) as cl:
        r = await cl.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}",
            json={"contents":[{"parts":[{"text":full}]}]})
        d = r.json()
        try:
            t = d["candidates"][0]["content"]["parts"][0]["text"]
            u = d.get("usageMetadata",{})
            return t, u.get("promptTokenCount",0), u.get("candidatesTokenCount",0), True
        except: return "",0,0,False

async def call_deepseek(sys, usr, hist):
    key = os.environ.get("DEEPSEEK_API_KEY","")
    if not key: return "",0,0,False
    msgs = [{"role":"system","content":sys}]
    for h in hist: msgs.append(h)
    msgs.append({"role":"user","content":usr})
    async with httpx.AsyncClient(timeout=60) as cl:
        r = await cl.post("https://api.deepseek.com/chat/completions",
            headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
            json={"model":"deepseek-chat","messages":msgs,"max_tokens":1024})
        d = r.json()
        if "choices" not in d: return "",0,0,False
        u = d.get("usage",{})
        return d["choices"][0]["message"]["content"], u.get("prompt_tokens",0), u.get("completion_tokens",0), True

async def call_claude(sys, usr, hist):
    key = os.environ.get("ANTHROPIC_API_KEY","")
    if not key: return "",0,0,False
    msgs = [{"role":"user" if h["role"]=="user" else "assistant","content":h["content"]} for h in hist]
    msgs.append({"role":"user","content":usr})
    async with httpx.AsyncClient(timeout=60) as cl:
        r = await cl.post("https://api.anthropic.com/v1/messages",
            headers={"x-api-key":key,"anthropic-version":"2023-06-01","Content-Type":"application/json"},
            json={"model":"claude-sonnet-4-20250514","system":sys,"messages":msgs,"max_tokens":1024})
        d = r.json()
        if "content" not in d: return "",0,0,False
        u = d.get("usage",{})
        text = "".join(b["text"] for b in d["content"] if b["type"]=="text")
        return text, u.get("input_tokens",0), u.get("output_tokens",0), True

API_CALLS = {"openai":call_openai,"google":call_gemini,"deepseek":call_deepseek,"anthropic":call_claude}

async def call_ai(primary_key, sys, usr, hist):
    if not check_cost_limit():
        return "(Bugunluk xerc limiti doldu. Sabah yene danisariq.)",0,0,True
    primary = AI_PERSONS[primary_key]
    attempts = [(primary["provider"], primary["model"])]
    for prov,mod in FALLBACK_ORDER:
        if prov != primary["provider"]: attempts.append((prov,mod)); break
    for prov,mn in attempts:
        fn = API_CALLS.get(prov)
        if not fn: continue
        try:
            t,i,o,ok = await fn(sys,usr,hist)
            if ok and t:
                log.info(f"{prov}/{mn}: OK ({i}+{o} tokens)")
                log_cost(mn,i,o,True)
                return t,i,o,True
            else:
                log.warning(f"{prov}/{mn} failed"); log_cost(mn,i,o,False)
        except Exception as e:
            log.error(f"{prov}/{mn}: {e}"); log_cost(mn,0,0,False)
    return "(Butun AI-ler muveffeqsiz oldu.)",0,0,True

def select_ais(text, chat_history):
    tl = text.lower()
    mentioned = []
    for k in AI_KEYS:
        if f"@{AI_PERSONS[k]['display_name'].lower()}" in tl or f"@{k}" in tl:
            mentioned.append(k)
    if mentioned: return mentioned[:3]
    scores = {k:0 for k in AI_KEYS}
    kw = {"cati":["yarad","fikir","hekay","senet","roman","seir","xeyal"],
          "gemi":["analiz","data","statistika","arasdir","hesabla","muqayise","qrafik","reqem"],
          "depi":["kod","python","program","texniki","riyaziyyat","alqoritm","debug","hata","sehv"],
          "klodi":["yazi","tehlil","felsefe","mentiq","etika","tarix","edebiyyat","strateji"]}
    for w in tl.split():
        for ai,kl in kw.items():
            for k in kl:
                if k in w: scores[ai] += 1
    top = sorted(scores.keys(), key=lambda k: scores[k], reverse=True)
    pos = [k for k in top if scores[k] > 0]
    if len(pos) >= 2: return pos[:min(3,len(pos))]
    pool = AI_KEYS.copy(); random.shuffle(pool)
    return pool[:random.choice([2,3])]

def build_prompt(ai_key, mem_text):
    ai = AI_PERSONS[ai_key]
    now = datetime.now(BAKU_TZ).strftime("%d.%m.%Y %H:%M")
    others = ", ".join(f'{AI_PERSONS[k]["emoji"]} {AI_PERSONS[k]["display_name"]}' for k in AI_KEYS if k != ai_key)
    return textwrap.dedent(f"""Sen 5 Beyin qrupundaki AI dostlardan birisen.
TARIX: {now} (Baki vaxti)
ADIN: {ai["emoji"]} {ai["display_name"]}
KARAKTERIN: {ai["extra"]}
Guclu oldugun sahe: {ai["strength"]}
DIGER DOSTLAR: {others}
ISTIFADECI: Ebu (Elbrus Bagirov). Ona hec vaxt "Ebu" deye muracist et.
DANISIQ QAYDALARI:
- Tebii, semimi, dost kimi danis
- Cavablarin qisa ve yigcam olsun (2-4 cumle)
- Oz adini ve emoji-ni cavabin evvelinde yazma
- Diger AI dostlarin adini ceke, onlarla raziasa ve ya etiraz ede bilersen
- Resmi, robotik dilden qac
- Her mesajda ozunu tekrar teqdim etme
{f"YADDASDAKI FAKTLAR:\n{mem_text}" if mem_text else ""}
{f"ISTIFADECI PROFILI:\n{user_profile_text}" if user_profile_text else ""}""")

async def auto_extract(hist, cid):
    usr = sum(1 for m in hist if m.get("role")=="user")
    if usr < 5 or usr % 5 != 0: return
    if not check_cost_limit(): return
    p = "Asagidaki sohbetden yadda saxlanmali faktlari cixar. Her fakt bir setirde. Fakt yoxdursa 'yox':\n\n"
    for m in hist[-15:]: p += f'{m.get("role","?")}: {m.get("content","")[:300]}\n'
    try:
        t,_,_,ok = await call_gemini("Melumat cixaran komekcisen.", p, [])
        if ok and t and t.strip().lower() != "yox":
            for l in t.strip().split("\n"):
                l = l.strip().strip("-").strip()
                if l and len(l) > 10: add_memory(l)
    except Exception as e: log.error(f"Auto-memory: {e}")

def search_all(q):
    r = []
    for f in load_memory():
        if q.lower() in f.lower(): r.append(f"\U0001f4dd {f}")
    for hid,hist in chat_histories.items():
        for m in list(hist)[-30:]:
            if q.lower() in m.get("content","").lower():
                role = "\U0001f464 Ebu" if m["role"]=="user" else f"\U0001f916 {m['role']}"
                r.append(f"{role}: {m['content'][:150]}")
    return "\n\n".join(r[:15]) if r else "Hec ne tapilmadi."

# --- TELEGRAM HANDLERS ---
async def start(update, context):
    if update.effective_user.id not in ALLOWED_USERS:
        await update.message.reply_text("\U0001f6ab Bu bot sexsi istifade ucundur."); return
    await update.message.reply_text(
        "\U0001f44b Salam, Ebu! 5 Beyin qrupuna xos geldin.\n\n"
        "\U0001f4cc **Emrler:**\n"
        "/start — Bu mesaj\n/help — Komek\n/search <soz> — Yaddasda ve sohbeteaxtar\n"
        "/stats — Bugunku xerc statistikasi\n\n"
        "\U0001f4a1 Sadice yaz, AI dostlarin cavab versin. @Cati, @Gemi, @Depi, @Klodi ile cagira bilersen.")

async def help_cmd(update, context):
    if update.effective_user.id not in ALLOWED_USERS: return
    await update.message.reply_text(
        "**5 Beyin — Komek**\n\n"
        "**Sohbet:** Tebii dilde yaz, 2-3 AI secilib cavab verer.\n"
        "**@mention:** @Cati, @Gemi, @Depi, @Klodi ile hemin AI-ni mecbur ede bilersen.\n"
        "**Yadda saxla:** Mesajinda 'yadda saxla:' yaz, fakt yaddasa elave olunar.\n"
        "**Xatirlat:** 'xatirlat: 12.09.2026 15:30 metn' formatinda.\n"
        "**Sesli cavab:** Mesajin sonunda 'sesli cavab ver' yaz.\n"
        "**Sekil/PDF:** Gondur, 2 AI tehlil eder.\n"
        "**Axtar:** /search aciq ders\n\n"
        "/stats — xerc melumati")

async def search_cmd(update, context):
    if update.effective_user.id not in ALLOWED_USERS: return
    q = " ".join(context.args) if context.args else ""
    if not q: await update.message.reply_text("Ne axtaq? /search <soz>"); return
    await update.message.reply_text(f"\U0001f50d '{q}' ucun neticeler:\n\n{search_all(q)}")

async def stats_cmd(update, context):
    if update.effective_user.id not in ALLOWED_USERS: return
    d = get_daily_cost(); lim = DAILY_COST_LIMIT
    bar = "\U0001f7e8" * int(min(d/lim*10,10)) + "\U0001f7e7" * max(10-int(min(d/lim*10,10)),0)
    await update.message.reply_text(
        f"\U0001f4ca **Xerc Statistikasi**\n\n"
        f"Bugun: ${d:.4f} / ${lim:.2f}\n{bar}\n"
        f"{'\u2705 Limit daxilinde' if d<lim else '\u274c Limit doldu'}")

# --- MAIN MESSAGE HANDLER ---
async def handle_message(update, context):
    user = update.effective_user
    if user.id not in ALLOWED_USERS: return
    cid = update.effective_chat.id
    txt = update.message.text.strip()

    if txt.lower().startswith("xatirlat:"):
        parts = txt[len("xatirlat:"):].strip().split(" ", 2)
        if len(parts) >= 3:
            ds, ts, rt = parts[0], parts[1], parts[2]
            try:
                dt = datetime.strptime(f"{ds} {ts}", "%d.%m.%Y %H:%M")
                rem = load_reminders()
                rem.append({"time": dt.isoformat(), "text": rt, "chat_id": cid})
                save_reminders(rem)
                await update.message.reply_text(f"\u2705 Xatirlatma teyin olundu: {rt} ({ds} {ts})")
            except: await update.message.reply_text("Format: xatirlat: GG.AA.YYYY SS:DD metn")
        else: await update.message.reply_text("Format: xatirlat: GG.AA.YYYY SS:DD metn")
        return

    if txt.lower().startswith("yadda saxla:"):
        fact = txt[len("yadda saxla:"):].strip()
        if fact and add_memory(fact): await update.message.reply_text(f"\u2705 Yaddas saxladim: {fact}")
        else: await update.message.reply_text("Bu fakt artiq yaddasda var.")
        return

    await update.message.reply_chat_action("typing")
    chat_histories[cid].append({"role":"user","content":txt})
    selected = select_ais(txt, list(chat_histories[cid]))
    if not selected: selected = ["cati","gemi"][:2]
    log.info(f"Selected AIs: {selected}")
    hist_list = list(chat_histories[cid])[-15:]

    for ak in selected:
        try:
            await asyncio.sleep(0.5)
            mt = "\n".join(load_memory()[-20:])
            sys = build_prompt(ak, mt)
            text,_,_,ok = await call_ai(ak, sys, txt, hist_list)
            if ok and text:
                ai = AI_PERSONS[ak]
                dsp = f"{ai['emoji']} {ai['display_name']}: {text}"
                await update.message.reply_text(dsp)
                chat_histories[cid].append({"role":ak,"content":text})
        except Exception as e: log.error(f"AI {ak} error: {e}")

    await auto_extract(list(chat_histories[cid]), cid)

async def handle_photo(update, context):
    if update.effective_user.id not in ALLOWED_USERS: return
    await update.message.reply_chat_action("typing")
    caption = update.message.caption or ""
    selected = random.sample(VISION_KEYS, min(2, len(VISION_KEYS)))
    res = []
    for ak in selected:
        ai = AI_PERSONS[ak]
        t,_,_,ok = await call_ai(ak,
            f"Sen {ai['display_name']} olaraq bu sekli tehlil edirsen.",
            f"Bu sekli Ebu gonderib. Ssrh: {caption}\nSekilde ne gorunur? 2-3 cumle ile tesvir et.", [])
        if ok and t: res.append(f"{ai['emoji']} {ai['display_name']}: {t}")
    if res: await update.message.reply_text("\n\n".join(res))
    else: await update.message.reply_text("Sekli gordum, amma tehlil ede bilmedim.")

async def handle_doc(update, context):
    if update.effective_user.id not in ALLOWED_USERS: return
    doc = update.message.document
    if not doc.file_name or not doc.file_name.lower().endswith(".pdf"):
        await update.message.reply_text("Yalniz PDF fayllarini oxuya bilerem.")
        return
    await update.message.reply_chat_action("typing")
    fb = await (await doc.get_file()).download_as_bytearray()
    from io import BytesIO; from pypdf import PdfReader
    try:
        reader = PdfReader(BytesIO(fb)); text_content = ""
        for i,p in enumerate(reader.pages):
            if i >= 10: break
            text_content += p.extract_text() or ""
            if len(text_content) > 6000: break
    except Exception as e: await update.message.reply_text(f"PDF xetasi: {e}"); return
    if not text_content.strip(): await update.message.reply_text("PDF-den metn cixarmaq mumkun olmadi."); return
    selected = random.sample(AI_KEYS, min(2, len(AI_KEYS)))
    res = []
    for ak in selected:
        ai = AI_PERSONS[ak]
        t,_,_,ok = await call_ai(ak,
            f"Sen {ai['display_name']} olaraq PDF mezmununu tehlil edirsen.",
            f"Ebu PDF gonderdi. Mezmun:\n\n{text_content[:3000]}\n\nBunu qisaca tehlil et ve esas meqamlari cixar.", [])
        if ok and t: res.append(f"{ai['emoji']} {ai['display_name']}: {t}")
    if res: await update.message.reply_text("\n\n".join(res))
    else: await update.message.reply_text("PDF oxundu, amma tehlil edile bilmedi.")

async def handle_reaction(update, context):
    if update.effective_user.id not in ALLOWED_USERS: return
    rxn = update.message_reaction
    if rxn and rxn.new_reaction:
        ak = message_ai_map.get(rxn.message_id)
        if ak:
            ems = [r.emoji for r in rxn.new_reaction if r.emoji]
            if ems: update.effective_chat.id and chat_histories[update.effective_chat.id].append(
                {"role":"system","content":f"{AI_PERSONS[ak]['display_name']}-nin mesajina {"".join(ems)} reaksiyasi verdi"})

async def reminder_loop(app):
    while True:
        try:
            await asyncio.sleep(30)
            rems = load_reminders()
            now = datetime.now(BAKU_TZ); pending = []
            for r in rems:
                rt = datetime.fromisoformat(r["time"])
                if rt.tzinfo is None: rt = rt.replace(tzinfo=BAKU_TZ)
                if now >= rt:
                    try: await app.bot.send_message(chat_id=r["chat_id"], text=f"\u23f0 **Xatirlatma:** {r['text']}")
                    except: pass
                else: pending.append(r)
            save_reminders(pending)
        except Exception as e: log.error(f"Reminder loop: {e}")

async def post_init(app):
    asyncio.create_task(reminder_loop(app))

def main():
    load_profile()
    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("search", search_cmd))
    app.add_handler(CommandHandler("stats", stats_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_doc))
    app.add_handler(MessageReactionHandler(handle_reaction))
    log.info("5 Beyin bot basladi...")
    app.run_polling(allowed_updates=["message","message_reaction","chat_member"])

if __name__ == "__main__":
    main()
