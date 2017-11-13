#!/bin/python
import RPi.GPIO as GPIO
import time
import os
LedPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.output(LedPin, GPIO.HIGH)

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)


def blink():
        t_end = time.time() + 15
        while time.time() < t_end:
                        GPIO.output(LedPin, GPIO.LOW)
                        time.sleep(0.3)
                        GPIO.output(LedPin, GPIO.HIGH)
                        time.sleep(0.3)

def destroy():
        GPIO.output(LedPin, GPIO.LOW)
        GPIO.cleanup()

while True: 
	GPIO.setmode(GPIO.BCM)
	inputValue = GPIO.input(18)
	if(inputValue == False):
		print("Bottone premuto")
		os.system("sh /home/pi/Desktop/camera//video.sh")
		blink()
#		destroy()
	time.sleep(0.3)

 
#if __name__ == '__main__':
#	try:
#		blink()
#	except KeyboardInterrupt:
#		destroy()


