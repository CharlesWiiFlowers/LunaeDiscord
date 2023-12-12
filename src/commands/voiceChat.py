import nextcord
import requests
from nextcord.ext import commands

GUILD = 1053810487982297234

class voiceChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Úneme a un canal de voz!')
    async def join(self, interaction: nextcord.Interaction):
        if(interaction.user.voice == None):
            await interaction.response.send_message("No estás en un chat de voz!!")
        else:
            await interaction.user.voice.channel.connect(timeout=10)
            await interaction.response.send_message("Me conecté al chat de voz!!")
            
def setup(bot):
    bot.add_cog(voiceChat(bot=bot))