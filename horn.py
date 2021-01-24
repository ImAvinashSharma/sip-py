import os 
from playsound import playsound
import time
try:
    def th(n):
        for i in range(1,n):
            playsound('train_horn.mp3')
            time.sleep(0.7)
except:
    print("An exception occurred")