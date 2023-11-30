import nextcord
import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TESTING_GUILD_ID = 804412974709604373
TOKEN = os.getenv('TOKEN')

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} \n*****Hello World*****')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run(TOKEN)