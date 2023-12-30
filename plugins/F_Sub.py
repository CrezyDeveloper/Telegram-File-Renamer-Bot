from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢Join My Update Channel📢", url=client.invitelink) ]]
    text = "**𝚂𝙾𝚁𝚁𝚈 𝙳𝚄𝙳𝙴 𝚈𝙾𝚄𝚁 𝙽𝙾𝚃 𝙹𝙾𝙸𝙽𝙳 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 😔. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 🙏 **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          



