import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from AarohiX import app

# ------------------------------------------------------------------------------- #

chatQueue = []

stopProcess = False

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["zombies","clean"]))
async def remove(client, message):
  global stopProcess
  try: 
    try:
      sender = await app.get_chat_member(message.chat.id, message.from_user.id)
      has_permissions = sender.privileges
    except:
      has_permissions = message.sender_chat  
    if has_permissions:
      bot = await app.get_chat_member(message.chat.id, "self")
      if bot.status == ChatMemberStatus.MEMBER:
        await message.reply("➠ | 𝘐 𝘯𝘦𝘦𝘥 𝘢𝘥𝘮𝘪𝘯 𝘱𝘦𝘳𝘮𝘪𝘴𝘴𝘪𝘰𝘯 𝘵𝘰 𝘳𝘦𝘮𝘰𝘷𝘦 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 𝘢𝘤𝘤𝘰𝘶𝘯𝘵𝘴.")  
      else:  
        if len(chatQueue) > 30 :
          await message.reply("➠ | 𝘐'𝘮 𝘢𝘭𝘳𝘦𝘢𝘥𝘺 𝘸𝘰𝘳𝘬𝘪𝘯𝘨 𝘰𝘯 𝘮𝘺 𝘮𝘢𝘹𝘪𝘮𝘶𝘮 𝘯𝘶𝘮𝘣𝘦𝘳 𝘰𝘧 30 𝘤𝘩𝘢𝘵𝘴 𝘢𝘵 𝘵𝘩𝘦 𝘮𝘰𝘮𝘦𝘯𝘵. 𝘗𝘭𝘦𝘢𝘴𝘦 𝘵𝘳𝘺 𝘢𝘨𝘢𝘪𝘯 𝘴𝘩𝘰𝘳𝘵𝘭𝘺.")
        else:  
          if message.chat.id in chatQueue:
            await message.reply("➠ | 𝘛𝘩𝘦𝘳𝘦'𝘴 𝘢𝘭𝘳𝘦𝘢𝘥𝘺 𝘢𝘯 𝘰𝘯𝘨𝘰𝘪𝘯𝘨 𝘱𝘳𝘰𝘤𝘦𝘴𝘴 𝘪𝘯 𝘵𝘩𝘪𝘴 𝘤𝘩𝘢𝘵. 𝘗𝘭𝘦𝘢𝘴𝘦 [/𝘴𝘵𝘰𝘱] 𝘵𝘰 𝘴𝘵𝘢𝘳𝘵 𝘢 𝘯𝘦𝘸 𝘰𝘯𝘦.")
          else:  
            chatQueue.append(message.chat.id)  
            deletedList = []
            async for member in app.get_chat_members(message.chat.id):
              if member.user.is_deleted == True:
                deletedList.append(member.user)
              else:
                pass
            lenDeletedList = len(deletedList)  
            if lenDeletedList == 0:
              await message.reply("⟳ | 𝘕𝘰 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 𝘢𝘤𝘤𝘰𝘶𝘯𝘵𝘴 𝘪𝘯 𝘵𝘩𝘪𝘴 𝘤𝘩𝘢𝘵.")
              chatQueue.remove(message.chat.id)
            else:
              k = 0
              processTime = lenDeletedList*1
              temp = await app.send_message(message.chat.id, f"🧭 | 𝘛𝘰𝘵𝘢𝘭 𝘰𝘧 {lenDeletedList} 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 𝘢𝘤𝘤𝘰𝘶𝘯𝘵𝘴 𝘩𝘢𝘴 𝘣𝘦𝘦𝘯 𝘥𝘦𝘵𝘦𝘤𝘵𝘦𝘥\n🥀 | 𝘌𝘴𝘵𝘪𝘮𝘢𝘵𝘦𝘥 𝘵𝘪𝘮𝘦: {processTime} 𝘴𝘦𝘤𝘰𝘯𝘥𝘴 𝘧𝘳𝘰𝘮 𝘯𝘰𝘸")
              if stopProcess: stopProcess = False
              while len(deletedList) > 0 and not stopProcess:   
                deletedAccount = deletedList.pop(0)
                try:
                  await app.ban_chat_member(message.chat.id, deletedAccount.id)
                except Exception:
                  pass  
                k+=1
                await asyncio.sleep(10)
              if k == lenDeletedList:  
                await message.reply(f"✅ | 𝘚𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘳𝘦𝘮𝘰𝘷𝘦𝘥 𝘢𝘭𝘭 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 𝘢𝘤𝘤𝘰𝘶𝘯𝘵𝘴 𝘧𝘳𝘰𝘮 𝘵𝘩𝘪𝘴 𝘤𝘩𝘢𝘵.")  
                await temp.delete()
              else:
                await message.reply(f"✅ | 𝘚𝘶𝘤𝘤𝘦𝘴𝘴𝘧𝘶𝘭𝘭𝘺 𝘳𝘦𝘮𝘰𝘷𝘦𝘥 {k} 𝘥𝘦𝘭𝘦𝘵𝘦𝘥 𝘢𝘤𝘤𝘰𝘶𝘯𝘵𝘴 𝘧𝘳𝘰𝘮 𝘵𝘩𝘪𝘴 𝘤𝘩𝘢𝘵.")  
                await temp.delete()  
              chatQueue.remove(message.chat.id)
    else:
      await message.reply("👮🏻 | 𝘚𝘰𝘳𝘳𝘺, **𝘖𝘕𝘓𝘠 𝘈𝘋𝘔𝘐𝘕** 𝘤𝘢𝘯 𝘦𝘹𝘦𝘤𝘶𝘵𝘦 𝘵𝘩𝘪𝘴 𝘤𝘰𝘮𝘮𝘢𝘯𝘥.")  
  except FloodWait as e:
    await asyncio.sleep(e.value)                               
        

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["admins","staff"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"**𝘎𝘳𝘰𝘶𝘱 𝘚𝘵𝘢𝘧𝘧 - {message.chat.title}**\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 𝘖𝘸𝘯𝘦𝘳\n└ {owner.mention}\n\n👮🏻 𝘈𝘥𝘮𝘪𝘯𝘴\n"
      else:
        text2 += f"👑 𝘖𝘸𝘯𝘦𝘳\n└ @{owner.username}\n\n👮🏻 𝘈𝘥𝘮𝘪𝘯𝘴\n"
    except:
      text2 += f"👑 𝘖𝘸𝘯𝘦𝘳\n└ <i>Hidden</i>\n\n👮🏻 𝘈𝘥𝘮𝘪𝘯𝘴\n"
    if len(adminList) == 0:
      text2 += "└ <i>𝘈𝘥𝘮𝘪𝘯𝘴 𝘢𝘳𝘦 𝘩𝘪𝘥𝘥𝘦𝘯</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"✅ | **𝘛𝘰𝘵𝘢𝘭 𝘯𝘶𝘮𝘣𝘦𝘳 𝘰𝘧 𝘢𝘥𝘮𝘪𝘯𝘴**: {lenAdminList}"  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)       

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("bots"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"**ʙᴏᴛ ʟɪsᴛ - {message.chat.title}**\n\n🤖 ʙᴏᴛs\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"✅ | *𝘛𝘰𝘵𝘢𝘭 𝘯𝘶𝘮𝘣𝘦𝘳 𝘰𝘧 𝘣𝘰𝘵𝘴**: {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
    
# ------------------------------------------------------------------------------- #
