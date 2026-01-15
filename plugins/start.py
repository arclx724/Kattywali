# plugins/start.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message):
    bot = await client.get_me()
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add Me to Your Group", url=f"https://t.me/{bot.username}?startgroup=true")],
        [InlineKeyboardButton("🛠️ Support", url="https://t.me/itsSmartDev")]
    ])
    await message.reply_text(
        "**✨ Welcome to Advanced Group Bot! ✨**\n\nI protect groups and have many features.",
        reply_markup=kb
    )

@Client.on_message(filters.command("help"))
async def help_handler(client: Client, message):
    text = (
        "**🛠️ Available Commands:**\n\n"
        "**Bio Protection:**\n"
        "`/config` - Setup punishment\n"
        "`/free` - Whitelist user\n"
        "`/unfree` - Remove whitelist\n"
        "`/freelist` - Check whitelist"
    )
    await message.reply_text(text)
  
