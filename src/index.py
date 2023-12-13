import nextcord
import os
import getThings as gt
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='?')

TESTING_GUILD_ID = gt.guild()
TOKEN = gt.Token()

@bot.event
async def on_ready():

    activity = nextcord.Activity(type=nextcord.ActivityType.watching, name="Especial Navideño!! 🎄")
    await bot.change_presence(status=nextcord.Status.online, activity=activity)
    print(f'We have logged in as {bot.user} \n*****Hello World*****')


for file in os.listdir("./src/commands"):
    if file.endswith(".py"):
        bot.load_extension(f"commands.{file[:-3]}")

for file in os.listdir("./src/messages"):
    if file.endswith(".py"):
        bot.load_extension(f"messages.{file[:-3]}")

bot.run(TOKEN)