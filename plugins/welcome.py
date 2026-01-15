from pyrogram import Client, filters

@Client.on_message(filters.new_chat_members)
async def welcome_user(client, message):
    for member in message.new_chat_members:
        await message.reply(f"Welcome to the group, {member.mention}!")

