import nextcord
import requests
import json
import random
from nextcord.ext import commands

GUILD = [1053810487982297234,804412974709604373]

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
    num = random.randint(0,5)

    match num:
        case 0:
            return "7w7"
        case 1:
            return "UwU"
        case 2:
            return "OwO"
        case 3:
            return "nya∼"
        case 4:
            return ":'3"
        case 5:
            return "<3"
        
def getReaction(react):
    resp = requests.get(f'https://api.otakugifs.xyz/gif?reaction={react}')
    data = json.loads(resp.text)

    return data["url"]

class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Dale un beso a alguien')
    async def kiss(self, interaction: nextcord.Interaction, member: nextcord.Member):

        user, user1 = apodo(interaction=interaction, member=member)
        embed = nextcord.Embed(description=f'**{user}** le dio un beso a **{user1}** {asciiEmoji()}', color=interaction.user.colour)
        embed.set_image(url=getReaction('kiss'))
        
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(guild_ids=GUILD,description='Dale un abacho a alguien :3')
    async def hug(self, interaction: nextcord.Interaction, member: nextcord.Member):

        user, user1 = apodo(interaction=interaction, member=member)
        embed = nextcord.Embed(description=f'**{user}** le dio un abachito a **{user1}** {asciiEmoji()}', color=interaction.user.colour)
        embed.set_image(url=getReaction('hug'))

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(guild_ids=GUILD,description='Acaricia a alguie ')
    async def nuzzle(self, interaction: nextcord.Interaction, member: nextcord.Member):

        user, user1 = apodo(interaction=interaction, member=member)
        embed = nextcord.Embed(description=f'**{user}** acaricia suavemente **{user1}** {asciiEmoji()}', color=interaction.user.colour)
        embed.set_image(url=getReaction('nuzzle'))

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description='Mira fijamente a alguien')
    async def stare(self, interaction: nextcord.Interaction, member: nextcord.Member):

        user, user1 = apodo(interaction=interaction, member=member)
        embed = nextcord.Embed(description=f'**{user}** mira fijamente a **{user1}** {asciiEmoji()}', color=interaction.user.colour)
        embed.set_image(url=getReaction('stare'))

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Actions(bot))