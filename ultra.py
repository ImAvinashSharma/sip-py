from servo import Main
import time
import RPi.GPIO as GPIO
from horn import th
from ir import ir
GPIO. setmode (GPIO. BOARD)
trig = 11
echo = 13
GPIO. setup (echo, GPIO .IN)
GPIO. setup (trig, GPIO. OUT)
try:
    ang=30
    while True:
        GPIO.output (trig, True)
        time.sleep (0.00001)
        GPIO.output (trig, False)
        while GPIO.input(echo) == 0:
            pass
            start = time. time ()
        while GPIO.input(echo) == 1:
            pass
            end = time. time ()
        distance = int(((end - start) * 34300) / 2)
        print("distance:", distance, "cm")
        if distance <=500 and ir():
            th(7)
            while ang>30:
                if ang >=180 and ang<0:
                    break
                Main(ang=ang-5)
        elif distance >=500 and distance <=1900:
            th(2)
            while ang<=100:
                Main(ang=ang+5)
                if ang >=180 and ang<0:
                    break
        else:
            while ang<=160:
                if ang >=180 and ang<0:
                    break
                Main(ang=ang+5)
        time.sleep (0.5)
except KeyboardInterrupt:
    GPIO.cleanup()