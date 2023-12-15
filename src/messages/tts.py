import nextcord
import requests
import io
from io import BytesIO
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
import getThings as gt

KEY_TTS = gt.keytts()
LANGUAGE = "es-mx"

def ttspeech(text):
    resp = requests.get(f"http://api.voicerss.org/?key={KEY_TTS}&hl={LANGUAGE}&src={text}")
    
    with open("temp.mp3", "wb") as file:
        file.write(resp.content)

    return "temp.mp3"

class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def on_message(self, message: nextcord.Message):

        if message.author == self.bot.user:
            return
        
        if message.content[0:1] == self.bot.command_prefix:
            if (message.author.voice == None):
                await message.channel.send("No puedes llamarme porque no estás en un canal de voz!!")

            else:
                vc = message.author.voice.channel
                vclt = await vc.connect()

                source = ttspeech(message.content.removeprefix(self.bot.command_prefix))

                src = FFmpegPCMAudio(source)

                vclt.play(src, after=lambda e: src.cleanup)

def setup(bot):
    bot.add_cog(tts(bot))