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
