
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
