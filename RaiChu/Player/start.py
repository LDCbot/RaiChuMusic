from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Process.filters import other_filters2
from time import time
from Process.filters import command
from datetime import datetime
from Process.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""Hello {message.from_user.mention()}, My name is {BOT_NAME}.
I'm a telegram streaming bot with some useful features.
Feel free to add me to your groups.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "Commands & Help ❔", callback_data="cbbasic"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "How to Use Me ❓", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       "🍹 Developer", url=f"https://t.me/zain_THE_smoker"
                    ),
                    InlineKeyboardButton(
                       "🥂 Support", url=f"https://t.me/+9Jfz4TpU3fkzOGFl"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["fed", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/f188ed62530d5aa7fc656.jpg",
        caption=f"""Here Is The Our Federation Support ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Federation ⚒️", url=f"https://t.me/Death_Soul_Federation")
                ]
            ]
        ),
    )
