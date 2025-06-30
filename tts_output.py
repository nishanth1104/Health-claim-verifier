from gtts import gTTS
import os

def speak_text(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("start response.mp3") 
