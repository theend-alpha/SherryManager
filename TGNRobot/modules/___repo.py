import os
 from pyrogram import Client, filters
 from pyrogram.types import *

 from TGNRobot.conf import get_str_key
 from TGNRobot import pbot

 REPO_TEXT = "**A 💪Powerful [BOT](t.me/Tiranga_BOT) to Make Your Groups Secured & OP😎 ! \n\n↼ Øwñêr ⇀ : 『 [𝐂𝐋𝐀𝐍𝐋𝐎𝐑𝐃](t.me/clanlord7) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» 😈🇮🇳😈🇮🇳😈 «««"

 BUTTONS = InlineKeyboardMarkup(
       [[
         InlineKeyboardButton("⚡ ʏᴏᴜᴛᴜʙᴇ 🔥", url=f"https://m.youtube.com/c/ALPHAFREEFIREE"),
       ],[
         InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ⚡", url="https://t.me/group_for_chatting_india"),
       ]]
     )


 @pbot.on_message(filters.command(["repo"]))
 async def repo(pbot, update):
     await update.reply_text(
         text=REPO_TEXT,
         reply_markup=BUTTONS,
         disable_web_page_preview=True,
         quote=True
     )
