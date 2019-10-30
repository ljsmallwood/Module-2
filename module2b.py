import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1 = 11
pin2 = 13
pinOUT = 15

GPIO.setup(pin1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(pin3, GPIO.OUT, initial = GPIO.LOW)

while True: # Run forever
	GPIO.output(pin1, GPIO.HIGH)
	sleep(1)
	GPIO.output(pin1, GPIO.LOW)

	if GPIO.input(pin1) & GPIO.input(pin2):
		print("11")
		GPIO.output(pin3, GPIO.HIGH)
		sleep(2)
		GPIO.output(pin3, GPIO.LOW)
		sleep(2)
	if GPIO.input(pin1) & !GPIO.input(pin2):
		print("10")
		GPIO.output(pin3, GPIO.HIGH)
		sleep(1)
		GPIO.output(pin3, GPIO.LOW)
		sleep(1)
	if !GPIO.input(pin1) & GPIO.input(pin2):
		print("01")
		GPIO.output(pin3, GPIO.HIGH)
		sleep(1)
	if !GPIO.input(pin1) & !GPIO.input(pin2):
		print("00")
		GPIO.output(pin3, GPIO.LOW)
		sleep(1)
