#This was created using the following tutorial as a reference:
#https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

class myClient(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')

    async def on_message(self, message):
        #Check if the message is from itself
        if message.author == client.user:
            return

        #Make this case insensitive
        if message.clean_content == "!mock":
            response = message.reference
            print(response)
            #if response:
                #await message.channel.send(response)

client = myClient()
client.run(TOKEN)
