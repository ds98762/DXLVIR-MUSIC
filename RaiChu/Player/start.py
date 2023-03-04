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
        f"""━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.

┏━━━━━━━━━━━━━━━━━┓
┣★ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 : [𝐃𝐇𝐈𝐌𝐀𝐍](https://t.me/i_dxlvir)
┣★ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 » : @ABOUT_VISHU
┣★ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 » : @S_0_P_H
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐌𝐮𝐬𝐢𝐜.
━━━━━━━━━━━━━━━━━━━━━━━━
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "🌷𝐀𝐝𝐝 𝐌𝐞 𝐌𝐨𝐢 𝐋𝐮𝐯🌷", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    ),
                ],
                [
                    InlineKeyboardButton(
                       "🍒𝐉𝐨𝐢𝐧 𝐁𝐚𝐛𝐲🥀", url=f"https://t.me/ABOUT_VISHU"
                    ),
                    InlineKeyboardButton(
                       "😇𝐂𝐨𝐦𝐞 𝐇𝐞𝐫𝐞⛦⃕͜🇮🇳", url=f"https://t.me/S_0_P_H"
                    )
                ],[
                    InlineKeyboardButton(
                        "★ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ★",
                        url=f"https://t.me/I_DXLVIR",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f01f58c3d9b187ae1d8a1.jpg",
        caption=f"""🍒𝐇𝐞𝐫𝐞 𝐈𝐬 𝐓𝐡𝐞 𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐨𝐝𝐞 𝐅𝐨𝐫𝐤 𝐀𝐧𝐝 𝐆𝐢𝐯𝐞 𝐒𝐭𝐚𝐫𝐬✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹𝐃𝐇𝐈𝐌𝐀𝐍 𝐌𝐔𝐒𝐈𝐂🌹", url=f"https://github.com/DS98762")
                ]
            ]
        ),
    )
