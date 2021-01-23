#This was created using the following tutorial as a reference:
#https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python

import os

import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

# class myClient(discord.Client):
#     async def on_ready(self):
#         print(f'{client.user} has connected to Discord!')
#
#     async def on_message(self, message):
#         #Check if the message is from itself
#         if message.author == client.user:
#             return
#
#         #Make this case insensitive
#         if message.clean_content == "!mock":
#             response = message.reference
#             print(response)
#             #if response:
#                 #await message.channel.send(response)
#
# client = myClient()
# client.run(TOKEN)

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

    if response:
        await ctx.send(response)
    #print (ctx.message.reference.message_id)

bot.run(TOKEN)
