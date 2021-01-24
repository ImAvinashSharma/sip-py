import os 
from playsound import playsound
import time
def th(n):
    for i in range(1,n):
        playsound('train_horn.mp3')
        time.sleep(0.7)