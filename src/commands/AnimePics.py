import nextcord
import requests
import json
import random
from nextcord.ext import commands

categories = {"waifu": "waifu", "neko": "neko", "bully": "bully",
              "cuddle": "cuddle", "cry": "cry", "hug": "hug","kiss": "kiss",
              "lick": "lick", "pat": "pat","bonk": "bonk", "smile": "smile",
              "wave": "wave", "highfive": "highfive", "handhold": "handhold", "bite": "bite",
              "glomp": "glomp", "slap": "slap", "kill": "kill", "kick": "kick", "happy": "happy",
              "poke": "poke", "dance": "dance", "cringe": "cringe"}

categories1 = {"waifu": "waifu", "neko": "neko", "trap": "trap", "blowjob": "blowjob"}

GUILD = 1053810487982297234

def getAnimePics(category, type):
    resp = requests.get(url=f'https://api.waifu.pics/{type}/{category}')
    data = json.loads(resp.text)

    return data["url"]

class AnimePics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Te doy una imagen según la categoría que elijas (SFW)')
    async def animepic(self, interaction: nextcord.Interaction, categoria: str = nextcord.SlashOption(name='categoria', description='Escoge uno', choices=categories, required=True)):
        embed = nextcord.Embed(color=interaction.user.colour)
        embed.set_image(url=getAnimePics(categoria, 'sfw'))

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(guild_ids=[GUILD],description='Te doy una imagen según la categoría que elijas (NSFW)')
    async def animepicextra(self, interaction: nextcord.Interaction, categoria: str = nextcord.SlashOption(name='categoria', description='Escoge uno', choices=categories1, required=True)):
        embed = nextcord.Embed(color=interaction.user.colour)
        embed.set_image(url=getAnimePics(categoria, 'nsfw'))

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(AnimePics(bot))