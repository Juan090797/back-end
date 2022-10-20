from fileinput import filename
from gtts import gTTS
import os

tts = gTTS(text='Federico la potona',lang='es')
filename = 'hello.mp3'
tts.save(filename)
os.system(f"start {filename}")