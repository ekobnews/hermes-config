
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
