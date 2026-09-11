
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
