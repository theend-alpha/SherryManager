import os
 from pyrogram import Client, filters
 from pyrogram.types import *

 from TGNRobot.conf import get_str_key
 from TGNRobot import pbot

 REPO_TEXT = "**A ๐ชPowerful [BOT](t.me/Tiranga_BOT) to Make Your Groups Secured & OP๐ ! \n\nโผ รwรฑรชr โ : ใ [๐๐๐๐๐๐๐๐](t.me/clanlord7) ใ\nโญโโโโโโโโโโโโโโ\nโฃโ ยป Python ~ 3.8.6\nโฃโ ยป Update ~ Recently\nโฐโโโโโโโโโโโโโโ\n\nยปยปยป ๐๐ฎ๐ณ๐๐ฎ๐ณ๐ ยซยซยซ"

 BUTTONS = InlineKeyboardMarkup(
       [[
         InlineKeyboardButton("โก สแดแดแดแดสแด ๐ฅ", url=f"https://www.youtube.com/channel/UCinfnBzi83lI-VzXDfKhsWQ/"),
       ],[
         InlineKeyboardButton("๊ฑแดแดแดแดสแด โก", url="https://t.me/group_for_chatting_india"),
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
