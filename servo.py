import RPi.GPIO as GPIO
from time import sleep
from multiprocessing import Process
import sys
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm=GPIO.PWM(11, 50)
pwm.start(30)
duty = 0
def SetAngle1(angle):
    global duty
    duty= angle/18+2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    GPIO.output(3, False)

def SetAngle2(angle):
    angle = 180 - angle
    global duty
    duty = angle/18+2
    GPIO.output(11,True)
    pwm.ChangeDutyCycle(duty)
    GPIO.output(11, False)
def Main(ang):
    if __name__=='__main__':
        p1 = Process(target=SetAngle1(ang))
        p1.start()
        p2 = Process(target=SetAngle2(ang))
        p2.start()
pwm.stop()
GPIO.cleanup()