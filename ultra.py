from servo import Main
import time
import RPi.GPIO as GPIO
GPIO. setmode (GPIO. BOARD)
trig = 11       # GPIO pin numbers
echo = 13
GPIO. setup (echo, GPIO .IN)
GPIO. setup (trig, GPIO. OUT)
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
    ang=30
    if distance <=100:
        while ang<=30:
            if ang >=180 and ang<0:
                break
            Main(ang=ang-5)
    elif distance <=500 and distance >=101:
        while ang<=120:
            if ang >=180 and ang<0:
                break
            Main(ang=ang-5)
    else:
        while ang<=160:
            if ang >=180 and ang<0:
                break
            Main(ang=ang+5)
    time.sleep (0.5)
GPIO.cleanup()