from bot import mxabot
from handlers.adduser import *
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
from plugins.forcesub import force_sub

bot = client.get_me()
bot_username = bot.username
bot_id = bot.id
START_TEXT = '''Hᴇʟʟᴏ {}, I Aᴍ [bot_username](bot_id)'''


#@mxabot.on_message(filters.private)
#async def _(bot: Client, message: Message):
 #   await add_user_in_db(bot, message)
  #  return

@mxabot.on_message(filters.command('start'))
async def start(client, message):
    await message.delete()
    fsub = await force_sub(client, message)
    if fsub == 400:
        return
    # me = self.get_me()
    await message.reply_text(
        START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                    InlineKeyboardButton("Close ❌", callback_data=f"delete")
                ]
            ]
        )
    )


