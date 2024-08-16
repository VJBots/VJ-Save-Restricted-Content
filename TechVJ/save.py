# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import asyncio 
import pyrogram
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated, UserAlreadyParticipant, InviteHashExpired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, Chat
import time
import os
import threading
import json
from config import API_ID, API_HASH
from database.db import database 
from TechVJ.strings import strings, HELP_TXT

def get(obj, key, default=None):
    try:
        return obj[key]
    except:
        return default

def set_forward_chat(user_id: int, chat: Chat):
    database.update_one(
        {'chat_id': user_id},
        {'$set': {'forward_chat_id': chat.id}},
        upsert=True
    )

def get_forward_chat(user_id: int):
    user_data = database.find_one({'chat_id': user_id})
    return user_data.get('forward_chat_id') if user_data else None

def set_remove_caption(user_id: int, remove: bool):
    database.update_one(
        {'chat_id': user_id},
        {'$set': {'remove_caption': remove}},
        upsert=True
    )

def get_remove_caption(user_id: int):
    user_data = database.find_one({'chat_id': user_id})
    return user_data.get('remove_caption', False) if user_data else False

async def downstatus(client: Client, statusfile, message):
    while True:
        if os.path.exists(statusfile):
            break
        await asyncio.sleep(3)
    
    while os.path.exists(statusfile):
        with open(statusfile, "r") as downread:
            txt = downread.read()
        try:
            await client.edit_message_text(message.chat.id, message.id, f"Downloaded : {txt}")
            await asyncio.sleep(10)
        except:
            await asyncio.sleep(5)

async def upstatus(client: Client, statusfile, message):
    while True:
        if os.path.exists(statusfile):
            break
        await asyncio.sleep(3)
    
    while os.path.exists(statusfile):
        with open(statusfile, "r") as upread:
            txt = upread.read()
        try:
            await client.edit_message_text(message.chat.id, message.id, f"Uploaded : {txt}")
            await asyncio.sleep(10)
        except:
            await asyncio.sleep(5)

def progress(current, total, message, type):
    with open(f'{message.id}{type}status.txt', "w") as fileup:
        fileup.write(f"{current * 100 / total:.1f}%")

@Client.on_message(filters.command(["start"]))
async def send_start(client: Client, message: Message):
    buttons = [[
        InlineKeyboardButton("❣️ Developer", url = "https://t.me/kingvj01")
    ],[
        InlineKeyboardButton('🔍 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url='https://t.me/vj_bot_disscussion'),
        InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/vj_botz')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await client.send_message(message.chat.id, f"<b>👋 Hi {message.from_user.mention}, I am Save Restricted Content Bot, I can send you restricted content by its post link.\n\nFor downloading restricted content /login first.\n\nKnow how to use bot by - /help</b>", reply_markup=reply_markup, reply_to_message_id=message.id)

@Client.on_message(filters.command(["help"]))
async def send_help(client: Client, message: Message):
    await client.send_message(message.chat.id, f"{HELP_TXT}")

@Client.on_message(filters.command(["setchat"]))
async def set_chat(client: Client, message: Message):
    if len(message.command) > 1:
        chat = message.command[1]
        try:
            chat = await client.get_chat(chat)
            set_forward_chat(message.from_user.id, chat)
            await message.reply(f"Đã đặt {chat.title} làm nơi chuyển tiếp.")
        except Exception as e:
            await message.reply(f"Lỗi: {str(e)}")
    else:
        await message.reply("Vui lòng cung cấp ID hoặc username của chat.")

@Client.on_message(filters.command(["togglecaption"]))
async def toggle_caption(client: Client, message: Message):
    current_status = get_remove_caption(message.from_user.id)
    new_status = not current_status
    set_remove_caption(message.from_user.id, new_status)
    if new_status:
        await message.reply("Đã bật chế độ xóa caption khi chuyển tiếp video và ảnh.")
    else:
        await message.reply("Đã tắt chế độ xóa caption khi chuyển tiếp video và ảnh.")

@Client.on_message(filters.text & filters.private)
async def save(client: Client, message: Message):
    if "https://t.me/" in message.text:
        datas = message.text.split("/")
        temp = datas[-1].replace("?single","").split("-")
        fromID = int(temp[0].strip())
        try:
            toID = int(temp[1].strip())
        except:
            toID = fromID
        for msgid in range(fromID, toID+1):
            # private
            if "https://t.me/c/" in message.text:
                user_data = database.find_one({'chat_id': message.chat.id})
                if not get(user_data, 'logged_in', False) or user_data['session'] is None:
                    await client.send_message(message.chat.id, strings['need_login'])
                    return
                acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
                await acc.connect()
                chatid = int("-100" + datas[4])
                await handle_private(client, acc, message, chatid, msgid)
    
            # bot
            elif "https://t.me/b/" in message.text:
                user_data = database.find_one({"chat_id": message.chat.id})
                if not get(user_data, 'logged_in', False) or user_data['session'] is None:
                    await client.send_message(message.chat.id, strings['need_login'])
                    return
                acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
                await acc.connect()
                username = datas[4]
                try:
                    await handle_private(client, acc, message, username, msgid)
                except Exception as e:
                    await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            
            # public
            else:
                username = datas[3]
                try:
                    msg = await client.get_messages(username, msgid)
                except UsernameNotOccupied: 
                    await client.send_message(message.chat.id, "The username is not occupied by anyone", reply_to_message_id=message.id)
                    return
                try:
                    await client.copy_message(message.chat.id, msg.chat.id, msg.id, reply_to_message_id=message.id)
                except:
                    try:    
                        user_data = database.find_one({"chat_id": message.chat.id})
                        if not get(user_data, 'logged_in', False) or user_data['session'] is None:
                            await client.send_message(message.chat.id, strings['need_login'])
                            return
                        acc = Client("saverestricted", session_string=user_data['session'], api_hash=API_HASH, api_id=API_ID)
                        await acc.connect()
                        await handle_private(client, acc, message, username, msgid)
                        
                    except Exception as e:
                        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)

            # wait time
            await asyncio.sleep(3)

async def handle_private(client: Client, acc, message: Message, chatid: int, msgid: int):
    msg: Message = await acc.get_messages(chatid, msgid)
    msg_type = get_message_type(msg)
    
    forward_chat_id = get_forward_chat(message.from_user.id)
    if forward_chat_id:
        chat = forward_chat_id
    else:
        chat = message.chat.id

    remove_caption = get_remove_caption(message.from_user.id)

    if "Text" == msg_type:
        try:
            await client.send_message(chat, msg.text, entities=msg.entities, reply_to_message_id=message.id)
        except Exception as e:
            await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
            return

    smsg = await client.send_message(message.chat.id, 'Downloading', reply_to_message_id=message.id)
    dosta = asyncio.create_task(downstatus(client, f'{message.id}downstatus.txt', smsg))
    try:
        file = await acc.download_media(msg, progress=progress, progress_args=[message,"down"])
        os.remove(f'{message.id}downstatus.txt')
        
    except Exception as e:
        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
        return
    
    upsta = asyncio.create_task(upstatus(client, f'{message.id}upstatus.txt', smsg))

    if msg.caption and not remove_caption:
        caption = msg.caption
    else:
        caption = None
            
    try:
        if "Document" == msg_type:
            ph_path = await acc.download_media(msg.document.thumbs[0].file_id) if msg.document.thumbs else None
            await client.send_document(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])
            if ph_path: os.remove(ph_path)

        elif "Video" == msg_type:
            ph_path = await acc.download_media(msg.video.thumbs[0].file_id) if msg.video.thumbs else None
            video_caption = None if remove_caption else caption
            await client.send_video(chat, file, duration=msg.video.duration, width=msg.video.width, height=msg.video.height, thumb=ph_path, caption=video_caption, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])
            if ph_path: os.remove(ph_path)

        elif "Animation" == msg_type:
            await client.send_animation(chat, file, reply_to_message_id=message.id)

        elif "Sticker" == msg_type:
            await client.send_sticker(chat, file, reply_to_message_id=message.id)

        elif "Voice" == msg_type:
            await client.send_voice(chat, file, caption=caption, caption_entities=msg.caption_entities, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])

        elif "Audio" == msg_type:
            ph_path = await acc.download_media(msg.audio.thumbs[0].file_id) if msg.audio.thumbs else None
            await client.send_audio(chat, file, thumb=ph_path, caption=caption, reply_to_message_id=message.id, progress=progress, progress_args=[message,"up"])
            if ph_path: os.remove(ph_path)

        elif "Photo" == msg_type:
            photo_caption = None if remove_caption else caption
            await client.send_photo(chat, file, caption=photo_caption, reply_to_message_id=message.id)

    except Exception as e:
        await client.send_message(message.chat.id, f"Error: {e}", reply_to_message_id=message.id)
    
    if os.path.exists(f'{message.id}upstatus.txt'): 
        os.remove(f'{message.id}upstatus.txt')
    if os.path.exists(file):
        os.remove(file)
    await client.delete_messages(message.chat.id, [smsg.id])
            
    if os.path.exists(f'{message.id}upstatus.txt'): 
        os.remove(f'{message.id}upstatus.txt')
        os.remove(file)
    await client.delete_messages(message.chat.id,[smsg.id])

def get_message_type(msg: pyrogram.types.messages_and_media.message.Message):
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
        
