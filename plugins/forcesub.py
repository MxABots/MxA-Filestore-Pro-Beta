from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import UserNotParticipant

async def force_sub(client, message, fsub: int):
    if fsub:
        try:
            user = await client.get_chat_member(fsub, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("Sorry, you are banned 🥲")
                return
        except UserNotParticipant:
            await message.reply_text(
                text="Hey bruh, you have to subscribe to my update channel to use me",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Channel 📣", url="t.me/NG_Bots")
                        ],
                        [
                            InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306")
                        ]
                    ]
                )
            )
            return
