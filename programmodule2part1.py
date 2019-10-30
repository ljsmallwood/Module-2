import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1 = 11 

GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)

while True: # Run forever
	GPIO.output(pin1, GPIO.HIGH)
	sleep(1)
	GPIO.output(pin1, GPIO.LOW)
	sleep(1)


