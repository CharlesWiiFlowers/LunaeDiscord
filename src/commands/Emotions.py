import nextcord
from nextcord.ext import commands
import requests
import random
import json

def getName(interaction: nextcord.Interaction):
    if interaction.user.nick is not None:
        return interaction.user.nick
    else:
        return interaction.user.name

def apiReturn(category):
    #Deleted: random.randint(0,1) == 1 and 
    if category != "cringe" and category != "yeet" and category != "smug":
        resp = requests.get(f'https://api.otakugifs.xyz/gif?reaction={category}')
        data = json.loads(resp.text)
        return data["url"]
    else:
        resp = requests.get(url=f'https://api.waifu.pics/sfw/{category}')
        data = json.loads(resp.text)
        return data["url"]
    
def emoji(cat: str):
    with open("src/data/emojis.json") as file:
        data = json.load(file)

        data1 = list(data[cat])

        return data1[random.randint(0, len(data1) - 1)]
    
def categorias():
    with open("src/data/category.json", encoding='utf-8') as file:
        data = json.load(file)
    lista = list(data["Emotions"].keys())
    return {lista:lista for (lista, lista) in zip(lista, lista)}

#Get the text in category.json, codified
def text(cat, interaction: nextcord.Interaction):
    with open("src/data/category.json", encoding='utf-8') as file:
        data = json.load(file)

    #Get the file in the corresponsive CATegory
    msg = list(data["Emotions"][cat])

    msgF: str = msg[random.randint(0, len(msg) - 1)]

    msgF = msgF.replace("{NAME}", getName(interaction=interaction))

    with open("src/data/emojis.json", encoding='utf-8') as file:
        dataE = json.load(file)

    fixedDataE = list(dataE.keys())

    for x in fixedDataE:
        y = "{" + x + "}"
        msgF = msgF.replace(y, emoji(x))

    return msgF


class Emotions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description="¿Cómo te sientes? Exprésalo <3")
    async def emotion(self, interaction: nextcord.Interaction, categoria: str = nextcord.SlashOption(
        name='categoria', description='Elige tu emoción', choices=categorias(), required=True
    )):
        embed = nextcord.Embed(description=text(cat=categoria, interaction=interaction), color=interaction.user.colour)
        embed.set_image(url=apiReturn(category=categoria))

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Emotions(bot=bot))