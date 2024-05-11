import requests
from requests import get 
from AarohiX import app
from pyrogram import filters
from pyrogram.types import InputMediaPhoto

@app.on_message(filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def pinterest(_, message):
     chat_id = message.chat.id

     try:
       query= message.text.split(None,1)[1]
     except:
         return await message.reply("**𝘎𝘪𝘷𝘦 𝘪𝘮𝘢𝘨𝘦 𝘯𝘢𝘮𝘦 𝘧𝘰𝘳 𝘴𝘦𝘢𝘳𝘤𝘩....🔍**")

     images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

     media_group = []
     count = 0

     msg = await message.reply(f"𝘚𝘤𝘳𝘢𝘱𝘪𝘯𝘨 𝘪𝘮𝘢𝘨𝘦𝘴....")
     for url in images["images"][:6]:
                  
          media_group.append(InputMediaPhoto(media=url))
          count += 1
          await msg.edit(f"=> 𝘚𝘤𝘳𝘢𝘱𝘦𝘥 𝘪𝘮𝘢𝘨𝘦𝘴 {count}")

     try:
        
        await app.send_media_group(
                chat_id=chat_id, 
                media=media_group,
                reply_to_message_id=message.id)
        return await msg.delete()

     except Exception as e:
           await msg.delete()
           return await message.reply(f"ᴇʀʀᴏʀ : {e}")
