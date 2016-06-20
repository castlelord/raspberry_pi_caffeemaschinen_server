import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(8, 1)
sleep(1)
GPIO.output(8, 0)

