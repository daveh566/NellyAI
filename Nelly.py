import json
from time import sleep

import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import kuki

print("[INFO]: Checking your details")


@kuki.on_message(
    filters.text
    & filters.reply
    & ~filters.bot,
    group=2,
)
async def kukiai(client: Client, message: Message):
    msg = message.text
    chat_id = message.chat.id

    if msg and not message.document:
        await kuki.send_chat_action(chat_id, action="typing")
        kukiurl = requests.get(
            f"https://kuki-api.tk/api/Raiden/moezilla/message={msg}",
            timeout=30,
        )
        kuki_json = json.loads(kukiurl.text)
        reply = kuki_json.get("reply", "I could not generate a response.")
        sleep(0.3)
        await message.reply_text(reply, quote=True)


messageprivate = """
Hi, I'm Kuki Chat Bot
"""

messagegroup = """
Hi, I'm Kuki Chat Bot
"""


@kuki.on_message(filters.command("start"))
async def start(_, message: Message):
    self_user = await kuki.get_me()
    _ = self_user.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return

    buttons = [[InlineKeyboardButton("Github", url="https://github.com/daveh566")]]
    await message.reply_text(
        messageprivate,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


if __name__ == "__main__":
    print("\nYour Nelly is starting...\n")
    kuki.run()
