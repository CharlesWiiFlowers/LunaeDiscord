import nextcord
import requests
import json
import random
import getThings as gt
from nextcord.ext import commands

categories = {"waifu": "waifu", "neko": "neko", "shinobu":"shinobu", "megumin": "megumin", "awoo": "awoo"}

categories1 = {"waifu": "waifu", "neko": "neko", "trap": "trap", "blowjob": "blowjob"}

GUILD = gt.guild()

def getAnimePics(category, type):
    resp = requests.get(url=f'https://api.waifu.pics/{type}/{category}')
    data = json.loads(resp.text)

    return data["url"]

def action(category, name):
    return (f"**{name}** ha usado **{category}**")


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
        embed = nextcord.Embed(color=interaction.user.colour, description=action(categoria, name=giveNick(interaction=interaction)))
        embed.set_image(url=getAnimePics(categoria, 'sfw'))

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(guild_ids=[int(gt.guild())],description='Te doy una imagen según la categoría que elijas (NSFW)')
    async def animepicextra(self, interaction: nextcord.Interaction, categoria: str = nextcord.SlashOption(name='categoria', description='Escoge uno', choices=categories1, required=True)):
        embed = nextcord.Embed(color=interaction.user.colour, description=action(category=categoria, name=giveNick(interaction)))
        embed.set_image(url=getAnimePics(categoria, 'nsfw'))

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(AnimePics(bot))