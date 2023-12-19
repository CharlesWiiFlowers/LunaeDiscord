import nextcord
import requests
import json
import random
import getThings as gt
from nextcord.ext import commands

GUILD = gt.guild()

def apodo(interaction: nextcord.Interaction, member: nextcord.Member):
    if interaction.user.nick is None:
        name = interaction.user.name
    else:
        name = interaction.user.nick
    if member.nick is None:
        name1 = member.name
    else:
        name1 = member.nick
    return name, name1

def asciiEmoji(react):
    with open("src/data/emojis.json", encoding='utf-8') as file:
        data = json.load(file)
    data1 = list(data[react])
    return data1[random.randint(0, len(data1) - 1)]
        
def getReaction(react):
    if react != "kill" or react != "airkiss" or react != "angrystare":
        resp = requests.get(f'https://api.waifu.pics/sfw/{react}')
        data = json.loads(resp.text)
        return data["url"]
    else:
        resp = requests.get(f'https://api.otakugifs.xyz/gif?reaction={react}')
        data = json.loads(resp.text)
        return data["url"]

def categories():
    with open("src/data/category.json") as file:
        data: dict = json.load(file)

    data1 = list(data["Actions"].keys())
    return {lista:lista for (lista, lista) in zip(data1, data1)}

def text(user: str, user1: str, cat: str):
    with open("src/data/category.json", encoding='utf-8') as file:
        data: dict = json.load(file)

    lista = list(data["Actions"][cat])

    listaF: str = lista[random.randint(0, len(lista) - 1)]

    #Replace names of users
    listaF = listaF.replace("{NAME}", user)
    listaF = listaF.replace("{NAME1}", user1)

    #Replace emojis
    with open("src/data/emojis.json", encoding='utf-8') as file:
        dataE: dict = json.load(file)
    dataList = list(dataE.keys())

    for x in dataList:
        y = "{" + x + "}"
        listaF = listaF.replace(y, asciiEmoji(x))

    return listaF

class Actions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Quieres hacer algo?? Hazlo con este comando!! ;)', guild_ids=[int(GUILD)])
    async def action(self, interaction: nextcord.Interaction, member: nextcord.Member, categoria: str = nextcord.SlashOption(description="Qué acción harás?", choices= categories(), required= True, name="categoria")):

        user, user1 = apodo(interaction=interaction, member=member)
        embed = nextcord.Embed(color=interaction.user.colour, description=text(user=user, user1=user1, cat=categoria))
        embed.set_image(url=getReaction(categoria))
        
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Actions(bot))