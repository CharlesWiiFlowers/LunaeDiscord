import nextcord
from nextcord.ext import commands

GUILD = 1053810487982297234
    
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[GUILD], description='Despídete!!')
    async def chao(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Chaoooo!!")

    @nextcord.slash_command(description='Saluda!')
    async def hola(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'Holaaa {interaction.user.nick}')
    
def setup(bot):
    bot.add_cog(Slash(bot))