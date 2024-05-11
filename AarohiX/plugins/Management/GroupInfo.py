from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app

@app.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("𝘗𝘭𝘦𝘢𝘴𝘦 𝘱𝘳𝘰𝘷𝘪𝘥𝘦 𝘢 𝘨𝘳𝘰𝘶𝘱 𝘶𝘴𝘦𝘳𝘯𝘢𝘮𝘦. 𝘌𝘹𝘢𝘮𝘱𝘭𝘦: /𝘨𝘳𝘰𝘶𝘱𝘪𝘯𝘧𝘰 𝘠𝘰𝘶𝘳𝘎𝘳𝘰𝘶𝘱𝘜𝘴𝘦𝘳𝘯𝘢𝘮𝘦")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"➖➖➖➖➖➖➖\n"
        f"➲ GROUP NAME : {group.title} ✅\n"
        f"➲ GROUP ID : {group.id}\n"
        f"➲ TOTAL MEMBERS : {total_members}\n"
        f"➲ DESCRIPTION : {group_description or 'N/A'}\n"
        f"➲ USERNAME : @{group_username}\n"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)

@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat
    status_text = f"Group ID: {chat.id}\n" \
                  f"Title: {chat.title}\n" \
                  f"Type: {chat.type}\n"
                  
    if chat.username:
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)
