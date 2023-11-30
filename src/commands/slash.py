import discord as ds
from discord.ext import commands
from discord.app_commands import tree

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tree = tree.Tree(bot)
        self.tree.command(name='Hola', description='Salúdame!!', guild=ds.Object(id=804412974709604373))(self.hola)

    async def hola(self, interaction):
        await interaction.response.send_message(f'Holaa {interaction.user.name}')

def setup(bot):
    bot.add_cog(Slash(bot))
    bot.sync()