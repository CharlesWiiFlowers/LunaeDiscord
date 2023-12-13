import os
from dotenv import load_dotenv

load_dotenv()

def Token():
    return os.getenv('TOKEN')

def guild():
    return os.getenv('GUILD')

def keytts():
    return os.getenv('KEY_TEXT_TO_SPEECH')

def keyHostTTS():
    return os.getenv('KEY_TTS_HOST')