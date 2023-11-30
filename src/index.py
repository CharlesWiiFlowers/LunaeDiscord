import nextcord
import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='?')

TESTING_GUILD_ID = 1053810487982297234
TOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} \n*****Hello World*****')

bot.load_extension('commands.Slash')
bot.run(TOKEN)