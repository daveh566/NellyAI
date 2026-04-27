import os

from pyrogram import Client

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ.get("TOKEN")
BOT_TOKEN = TOKEN

kuki = Client(
    "KukiBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
)
