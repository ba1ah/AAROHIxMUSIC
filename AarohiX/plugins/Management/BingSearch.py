from AarohiX import app 
import requests as r
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import filters 

API_URL = "https://sugoi-api.vercel.app/search"

@app.on_message(filters.command("bingsearch"))
async def bing_search(dilop, message):
    try:
        if len(message.command) == 1:
            await message.reply_text("𝘗𝘭𝘦𝘢𝘴𝘦 𝘱𝘳𝘰𝘷𝘪𝘥𝘦 𝘢 𝘬𝘦𝘺𝘸𝘰𝘳𝘥 𝘵𝘰 𝘴𝘦𝘢𝘳𝘤𝘩.")
            return

        keyword = " ".join(message.command[1:])
        params = {"keyword": keyword}
        response = r.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("𝘕𝘰 𝘳𝘦𝘴𝘶𝘭𝘵𝘴 𝘧𝘰𝘶𝘯𝘥.")
            else:
                message_text = ""
                for result in results[:7]:
                    title = result.get("title", "")
                    link = result.get("link", "")
                    message_text += f"{title}\n{link}\n\n"
                await message.reply_text(message_text.strip())
        else:
            await message.reply_text("𝘚𝘰𝘳𝘳𝘺, 𝘴𝘰𝘮𝘦𝘵𝘩𝘪𝘯𝘨 𝘸𝘦𝘯𝘵 𝘸𝘳𝘰𝘯𝘨 𝘸𝘪𝘵𝘩 𝘵𝘩𝘦 𝘴𝘦𝘢𝘳𝘤𝘩.")
    except Exception as e:
        await message.reply_text(f"𝘈𝘯 𝘦𝘳𝘳𝘰𝘳 𝘰𝘤𝘤𝘶𝘳𝘳𝘦𝘥: {str(e)}")
