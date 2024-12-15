import os
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait, UsernameNotOccupied
from config import API_ID, API_HASH, ERROR_MESSAGE
from database.db import db

class batch_temp:
    IS_BATCH = {}

# Download status
async def downstatus(client: Client, statusfile, message):
    while not os.path.exists(statusfile):
        await asyncio.sleep(3)
      
    while os.path.exists(statusfile):
        with open(statusfile, "r") as downread:
            txt = downread.read()
        try:
            if batch_temp.IS_BATCH.get(message.from_user.id):
                return
            await client.edit_message_text(message.chat.id, message.id, f"**Downloaded:** **{txt}**")
            await asyncio.sleep(10)
        except:
            await asyncio.sleep(5)

# Upload status
async def upstatus(client: Client, statusfile, message):
    while not os.path.exists(statusfile):
        await asyncio.sleep(3)
      
    while os.path.exists(statusfile):
        with open(statusfile, "r") as upread:
            txt = upread.read()
        try:
            if batch_temp.IS_BATCH.get(message.from_user.id):
                return
            await client.edit_message_text(message.chat.id, message.id, f"**Uploaded:** **{txt}**")
            await asyncio.sleep(10)
        except:
            await asyncio.sleep(5)

# Progress writer
def progress(current, total, message, type):
    with open(f'{message.id}{type}status.txt', "w") as fileup:
        if batch_temp.IS_BATCH.get(message.from_user.id):
            return
        fileup.write(f"{current * 100 / total:.1f}%")

# Start command with buttons
@Client.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
    
    buttons = [
        [InlineKeyboardButton("❓ Help", callback_data="help_command")],
        [InlineKeyboardButton("❣️ Developer", url="https://t.me/kingvj01"),
         InlineKeyboardButton("🔍 Support Group", url="https://t.me/vj_bot_disscussion")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await message.reply_text(
        f"👋 **Hi {message.from_user.mention}**, I am a bot to save restricted content.\n\n"
        "Use the buttons below to get started ⬇️",
        reply_markup=reply_markup
    )

# Help command
@Client.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply_text(
        "**Help Menu**\n\n"
        "1. Use /login to log in.\n"
        "2. Send a restricted content link (https://t.me/...) to start.\n"
        "3. Use /cancel to stop an active task.\n\n"
        "For more details, contact the developer or support group."
    )

# Cancel command
@Client.on_message(filters.command("cancel"))
async def cancel_command(client: Client, message: Message):
    batch_temp.IS_BATCH[message.from_user.id] = True
    await message.reply_text("**Batch Successfully Cancelled.**")

# Save and process content
@Client.on_message(filters.text & filters.private)
async def save(client: Client, message: Message):
    if "https://t.me/" in message.text:
        if batch_temp.IS_BATCH.get(message.from_user.id) == False:
            return await message.reply_text("**One Task Is Already Processing. Use /cancel to stop it.**")

        datas = message.text.split("/")
        temp = datas[-1].replace("?single", "").split("-")
        fromID = int(temp[0].strip())
        try:
            toID = int(temp[1].strip())
        except:
            toID = fromID
        
        batch_temp.IS_BATCH[message.from_user.id] = False
        for msgid in range(fromID, toID + 1):
            if batch_temp.IS_BATCH.get(message.from_user.id):
                break

            user_data = await db.get_session(message.from_user.id)
            if user_data is None:
                await message.reply_text("**Please /login first to download restricted content.**")
                batch_temp.IS_BATCH[message.from_user.id] = True
                return

            try:
                acc = Client("session", session_string=user_data, api_id=API_ID, api_hash=API_HASH)
                await acc.connect()
            except:
                batch_temp.IS_BATCH[message.from_user.id] = True
                return await message.reply_text("**Your session expired. Use /logout and login again.**")
            
            # Handling private/public messages
            username = datas[3] if "https://t.me/c/" not in message.text else int("-100" + datas[4])
            try:
                msg = await acc.get_messages(username, msgid)
                await client.copy_message(message.chat.id, msg.chat.id, msg.id)
            except Exception as e:
                if ERROR_MESSAGE:
                    await message.reply_text(f"Error: {e}")

            await asyncio.sleep(3)
        batch_temp.IS_BATCH[message.from_user.id] = True

# Get message type
def get_message_type(msg: Message):
    try:
        msg.document.file_id
        return "Document"
    except:
        pass
    try:
        msg.video.file_id
        return "Video"
    except:
        pass
    try:
        msg.animation.file_id
        return "Animation"
    except:
        pass
    try:
        msg.sticker.file_id
        return "Sticker"
    except:
        pass
    try:
        msg.voice.file_id
        return "Voice"
    except:
        pass
    try:
        msg.audio.file_id
        return "Audio"
    except:
        pass
    try:
        msg.photo.file_id
        return "Photo"
    except:
        pass
    try:
        msg.text
        return "Text"
    except:
        pass
        
