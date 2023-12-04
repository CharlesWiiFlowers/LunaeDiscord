import nextcord
import requests
import json
import random
from nextcord.ext import commands

GUILD = 1053810487982297234

def apodo(interaction, member):
    if interaction.user.nick is None:
        name = interaction.user.name
    else:
        name = interaction.user.nick
    if member.nick is None:
        name1 = member.name
    else:
        name1 = member.nick
    return (name, name1)

def asciiEmoji():
    num = random.randint(0,3)

    match num:
        case 0:
            return "7w7"
        case 1:
            return "UwU"
        case 2:
            return "OwO"
        case 3:
            return "nya∼"



class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Dale un beso a alguien')
    async def kiss(self, interaction: nextcord.Interaction, member: nextcord.Member):

        user, user1 = apodo(interaction=interaction, member=member)

        resp = requests.get('https://api.otakugifs.xyz/gif?reaction=kiss')
        
        data = json.loads(resp.text)

        if member is None:
            member = interaction.user

        embed = nextcord.Embed(description=f'**{user}** le dio un beso a **{user1}** {asciiEmoji()}',
                               color=interaction.user.colour)
        embed.set_image(url=data["url"])

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Actions(bot))