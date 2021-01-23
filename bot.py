#This was created using the following tutorial as a reference:
#https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python

import os
import random
import math
import discord

from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime

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

    #Insert elements from response into index_array
    index_array = []
    for i in range(0,len(response)-1):
        index_array.append(i)

    #The number of letters to capitalize in the word
    cap_number = math.ceil(len(response)*0.55)

    random.seed(datetime.now())
    #indexes from response for letters that are to be capitalized
    capital_index =random.sample(index_array, k=cap_number)

    response_list = list(response.lower())
    for index in capital_index:
        #https://www.w3schools.com/python/ref_string_capitalize.asp
        response_list[index] = response[index].upper()

    response = ''.join(response_list)

    if response:
        await ctx.send(response)

bot.run(TOKEN)
