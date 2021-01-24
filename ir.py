import RPi.GPIO as GPIO
import time
sensor = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
def ir():
    try:
    while True:
        if GPIO.input(sensor):
            while GPIO.input(sensor):
                return True
        else:
            return False
    except KeyboardInterrupt:
        GPIO.cleanup()