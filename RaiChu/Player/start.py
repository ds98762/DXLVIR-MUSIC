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
🍂 ʜᴇʟʟᴏ ᴅᴇᴀʀ !! ɪ ᴀᴍ sᴜᴘᴇʀғᴀsᴛ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ , ɴᴏ ʟᴀɢ ᴠᴄ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ 🥀❤️

┏━━━━━━ • ✿ • ━━━━━━┓
┣★ ᴏᴡɴᴇʀ : [ᴅʜɪᴍᴀɴ 👒](https://t.me/i_dxlvir)
┣★ ғᴇᴇʟɪɴɢs : [ᴄʟɪᴄᴋ ʜᴇʀᴇ 😘](https://t.me/DHIMAN_FEELINGS)
┣★ sᴜᴘᴘᴏʀᴛ : [ᴄʟɪᴄᴋ ʜᴇʀᴇ 🫰🏻❤️](https://t.me/S_0_P_H)
┗━━━━━━ • ✿ • ━━━━━━┛

🎗 ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ sᴜᴘᴇʀ ǫᴜᴀʟɪᴛʏ ᴍᴜsɪᴄ 🎧🍷
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
                       "🖤 ᴊᴏɪɴ ʙᴀʙʏ 🖤", url=f"https://t.me/ABOUT_VISHU"
                    ),
                    InlineKeyboardButton(
                       "🖤 ᴅʜɪᴍᴀɴ ᴄʜᴀᴛᴛɪɴɢ 🖤", url=f"https://t.me/S_0_P_H"
                    )
                ],[
                    InlineKeyboardButton(
                        "ᴅʜɪᴍᴀɴ 🕊️",
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
        caption=f"""🥀 𝙃𝙀𝙍𝙀 𝙄𝙎 𝙏𝙃𝙀 𝙎𝙊𝙐𝙍𝘾𝙀 𝘾𝙊𝘿𝙀 𝙁𝙊𝙍𝙆 𝘼𝙉𝘿 𝙂𝙄𝙑𝙀 𝙎𝙏𝘼𝙍𝙎 ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹𝘿𝙃𝙄𝙈𝘼𝙉 𝙈𝙐𝙎𝙄𝘾🐍", url=f"https://github.com/DS98762")
                ]
            ]
        ),
    )
