import nextcord
from nextcord.ext import commands

GUILD = 1053810487982297234
    
class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Despídete!!')
    async def chao(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Chaoooo!!")

    @nextcord.slash_command(description='Saluda!')
    async def hola(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'Holaaa {interaction.user.nick}')

    @nextcord.slash_command(description='Muestra el avatar de un usuario')
    async def avatar(self, interaction: nextcord.Interaction, member: nextcord.Member):

        if member is None:
            member = interaction.user

        embed = nextcord.Embed(title=f'Avatar de {member.name}', color=interaction.user.colour)
        embed.set_footer(text=f'Usuario: {member.id}')
        embed.set_image(url=member.avatar.with_format("png").with_size(1024).url)

        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(description='Mando un mensaje por ti')
    async def message(self, interaction: nextcord.Interaction, mensaje: str):
        embed = nextcord.Embed(description=mensaje, color=interaction.user.colour)
        embed.set_footer(text=f'{interaction.user.name} y {self.bot.user.name}')
        await interaction.send(embed=embed)

def setup(bot):
    bot.add_cog(Slash(bot))