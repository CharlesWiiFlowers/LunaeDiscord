import os
import discord as ds
from discord import app_commands
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN=os.getenv('TOKEN')

intents = ds.Intents.default()
intents.message_content = True
intents.bans = True
client = ds.Client(intents=intents)
tree = app_commands.CommandTree(client)
bot = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    #await tree.sync(guild=ds.Object(id=804412974709604373))

    for file in os.listdir('./src/commands'):
        if file.endswith('.py'):
            await bot.load_extension(f'commands.{file[:-3]}')
    
    print(f'Hello World! We have logged in as {client.user}')

if __name__ == '__main__':
    client.run(TOKEN)