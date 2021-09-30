print("[INFO]: Importing Your API_ID, API_HASH, BOT_TOKEN")

from pyrogram.types import (
  Message, 
)
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os
from config import kuki, BOT_TOKEN
bot_token= BOT_TOKEN

print("[INFO]: Checking... Your Details")
@kuki.on_message(
    filters.text
    & filters.reply
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  if message.text and not message.document:
        if not kuki_message(context, message):
            return
        Message = message.text
        kuki.send_chat_action(chat_id, action="typing")
        kukiurl = requests.get('https://kuki-api.tk/api/Raiden/moezilla/message='+Message)
        Kuki = json.loads(kukiurl.text)
        kuki = Kuki['reply']
        sleep(0.3)
        message.reply_text(kuki, timeout=60)


messageprivate = '''
Hi, I'm Kuki Chat Bot
'''

messagegroup = '''
Hi, I'm Kuki Chat Bot
'''






@kuki.on_message(filters.command("start"))
async def start(_, message):
    self = await kuki.get_me()
    busername = self.username
    if message.chat.type != "private":
        await message.reply_text(messagegroup)
        return
    else:
        buttons = [[InlineKeyboardButton("Github", url="https://github.com/daveh566"),
                    ]]
        await message.reply_text(messageprivate, reply_markup=InlineKeyboardMarkup(buttons))

        await kuki.start()
print(
        """
Your Nelly Is Deployed Successfully.
"""
