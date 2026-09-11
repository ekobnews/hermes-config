
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
