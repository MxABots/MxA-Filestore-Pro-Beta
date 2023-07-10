from bot import mxabot
from handlers.adduser import *
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message#,
   # BotCommand
)
from plugins.forcesub import force_sub

START_TEXT = '''Hᴇʟʟᴏ {}, I Aᴍ MxA Pɪᴍɪᴜᴍ Fɪʟᴇsᴛᴏʀᴇ Bᴏᴛ!'''

async def handle_private_message(client: Client, message: Message):
    await adduser(client, message)

@mxabot.on_message(filters.command('start'))
async def start(client, message):
    await handle_private_message(client, message)
    await message.delete()
    fsub = await force_sub(client, message)
    if fsub == 400:
        return
    await message.reply_text(
        START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                    InlineKeyboardButton("Close ❌", callback_data="delete")
                ]
            ]
        )
    )



#mxabot.set_bot_commands([
#    BotCommand("start", "Start the bot"),
#    BotCommand("help", "Get help and instructions"),
#    BotCommand("settings", "Bot settings")])
