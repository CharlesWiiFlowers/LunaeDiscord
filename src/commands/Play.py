import nextcord
from nextcord.ext import commands
import getThings as gt
import pytube

GUILD = gt.guild()

def search(name: str, vc):
    #Get the searched music
    music = pytube.Search(name)
    video = music.results[0] #The first recommendation

    #Get URL
    stream = video.streams.filter(only_audio=True).first()
    url = stream.url

    FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn',
        }
    
    vc.play(nextcord.FFmpegPCMAudio(source=url, **FFMPEG_OPTIONS))

    return video.title

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(description='Reproduce musica con esto!!')
    async def play(self, interaction: nextcord.Interaction, name: str, vc: nextcord.VoiceChannel):
        if vc is None:
            await interaction.response.send_message(content="Give me a valid vc!!")

        voiceChat = await vc.connect()

        await interaction.response.send_message(content=f"Playing {search(name=name, vc=voiceChat)} on {vc.name}")

def setup(bot):
    bot.add_cog(Play(bot=bot))