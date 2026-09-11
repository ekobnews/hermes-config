
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
