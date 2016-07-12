import RPi.GPIO as GPIO
from time import sleep as sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

def pressButton():
    GPIO.output(8, 0)
    sleep(1)
    GPIO.output(8, 1)
    sleep(1)
    GPIO.output(8, 0)

pressButton()
