from gtts import gTTS
import time
import os 
from playsound import playsound
def tts(speech):
    mytext = speech
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("output.mp3")
    for i in range(0,3):
        playsound('output.mp3')
        time.sleep(0.7)
