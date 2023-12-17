import nextcord
import requests
import json
import random
import getThings as gt
from nextcord.ext import commands

categories = {"waifu": "waifu", "neko": "neko", "bully": "bully",
              "cuddle": "cuddle", "cry": "cry", "hug": "hug","kiss": "kiss",
              "lick": "lick", "shinobu": "shinobu","megumin": "megumin", "smile": "smile",
              "blush": "blush", "highfive": "highfive", "handhold": "handhold", "bite": "bite",
              "smug": "smug", "awoo": "awoo", "kill": "kill", "kick": "kick", "happy": "happy",
              "wink": "wink", "nom": "nom", "yeet": "yeet"}

categories1 = {"waifu": "waifu", "neko": "neko", "trap": "trap", "blowjob": "blowjob"}

GUILD = gt.guild()

def getAnimePics(category, type):
    resp = requests.get(url=f'https://api.waifu.pics/{type}/{category}')
    data = json.loads(resp.text)

    return data["url"]

def action(category, name, name2):
    match category:
        case "waifu":
            return (f"**{name}** ha usado **{category}**")
        case "neko":
            return (f"**{name}** ha usado **{category}**")
        case "bully":
            return (f"**{name}** hace bullyng!!")
        case "cuddle":
            return (f"**{name}** se acurruca")
        case "cry":
            return (f"**{name}** se puso a llorar T_T")
        case "hug":
            return (f"**{name}** se da un abrazo a sí mismo")
        case "kiss":
            return (f"**{name}** está romántico consigo mismo KISS UWU")
        case "lick":
            return (f"**{name}** está lamiéndose")
        case "pat":
            return (f"**{name}** se hace pat pat")
        case "bonk":
            return (f"**{name}** BONK!")
        case "smile":
            return (f"**{name}** está sonriendo!")
        case "blush":
            return (f"**{name}** se sonrojó!")
        case "highfive":
            return (f"Eso es!! **{name}** chocó manos con Lunae!")
        case "handhold":
            return (f"Puedes tomarte de la mano solo? **{name}**?")
        case "bite":
            return (f"AUCH! No me muerdas >:C")
        case "glomp":
            return (f" Gracias por el abrazo de OSO **{name}**!!")
        case "slap":
            return (f"No me abofetees **{name}** BAKA!")
        case "kill":
            return (f"Lunae was slain by **{name}**")
        case "kick":
            return (f"**{name}** pateó a Lunae antes de que lograse decir algo!")
        case "happy":
            return (f"**{name}** está feliz")
        case "poke":
            return (f"**{name}** POKE!")
        case "dance":
            return (f"**{name}** está bailando!!")
        case "cringe":
            return (f"**{name}** siente cringe...")
        
def giveNick(interaction: nextcord.Interaction):
    if interaction.user.nick is None:
        return interaction.user.name
    else:
        return interaction.user.nick

class AnimePics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Te doy una imagen según la categoría que elijas (SFW)')
    async def animepic(self, interaction: nextcord.Interaction, categoria: str = nextcord.SlashOption(name='categoria', description='Escoge uno', choices=categories, required=True)):
        embed = nextcord.Embed(color=interaction.user.colour, description=action(categoria, name=giveNick(interaction=interaction), name2="None"))
        embed.set_image(url=getAnimePics(categoria, 'sfw'))

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(guild_ids=[int(gt.guild())],description='Te doy una imagen según la categoría que elijas (NSFW)')
    async def animepicextra(self, interaction: nextcord.Interaction, categoria: str = nextcord.SlashOption(name='categoria', description='Escoge uno', choices=categories1, required=True)):
        embed = nextcord.Embed(color=interaction.user.colour)
        embed.set_image(url=getAnimePics(categoria, 'nsfw'))

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(AnimePics(bot))