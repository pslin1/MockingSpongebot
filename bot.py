#This was created using the following tutorial as a reference:
#https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python

import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

#Things to check:
#if quoted text is string
#If command is part of a reply
@bot.command(name='mock')
async def mock(ctx):

    msgID =ctx.message.reference.message_id
    #https://stackoverflow.com/questions/61851174/how-to-get-message-by-id-discord-py
    #Credit: diggy (https://stackoverflow.com/users/7808223/diggy)
    msg = await ctx.fetch_message(msgID)

    response = msg.clean_content

    for letter in response:

    if response:
        await ctx.send(response)

bot.run(TOKEN)
