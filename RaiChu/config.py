## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Zain_Musicbot")
API_ID = int(getenv("API_ID", "11656588"))
API_HASH = getenv("API_HASH", "47f06581edfba1d8c4ccb64fc175792a")
OWNER_NAME = getenv("OWNER_NAME", "zain_THE_smoker")
ALIVE_NAME = getenv("ALIVE_NAME", "Zain_Musicbot")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Play_All_Time")
BOT_USERNAME = getenv("BOT_USERNAME", "Zain_Musicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zain Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/+9Jfz4TpU3fkzOGFl")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/+9Jfz4TpU3fkzOGFl")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5102663914 5430094820 5390900681").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/f188ed62530d5aa7fc656.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/LDCbot/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/4a70f252bcf39c5f9ea99.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/4a70f252bcf39c5f9ea99.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/4a70f252bcf39c5f9ea99.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/4a70f252bcf39c5f9ea99.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/4a70f252bcf39c5f9ea99.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/4a70f252bcf39c5f9ea99.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/f188ed62530d5aa7fc656.jpg")
