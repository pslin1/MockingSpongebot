import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

class myClient(discord.Client):
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

client = myClient()
client.run(TOKEN)
