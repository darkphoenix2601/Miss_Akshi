from telethon import events, Button, custom
import re, os
from Miss_Akshi.events import register
from Miss_Akshi import telethn as tbot
from Miss_Akshi import telethn as tgbot
PHOTO = "https://telegra.ph/file/1ebb791d3370bea387a51.jpg"
@register(pattern=("/alive"))
async def awake(event):
 Miss_Akshi = event.sender.first_name
 Miss_Akshi = "**β‘ I,m Miss_Akshiπ** \n\n"
 Miss_Akshi += "**β‘ I'm Working with awesome speed**\n\n"
 Miss_Akshi += "**β‘Miss_Akshi : 1.0 LATEST**\n\n"
 Miss_Akshi += "**β‘ ππΊ π°πΈπ―π¦π³ :** [ππ΄π©πΆπ](t.me/doreamon_music)\n\n"
 Miss_Akshi += "**β‘ Telethon Version : 1.23.0**\n\n"
 BUTTON = [[Button.url("ππΆπ±π±π°π³π΅π₯", "https://t.me/phoenix_music_suport"), Button.url("ππ±π₯π’π΅π¦π΄", "https://t.me/phoenix_music_new")]]
 await tbot.send_file(event.chat_id, PHOTO, caption=Miss_Akshi,  buttons=BUTTON)
