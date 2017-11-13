#!/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True: 
	inputValue = GPIO.input(18)
	if(inputValue == False):
		print("Bottone premuto")
		os.system("sh /home/pi/Desktop/test/video.sh")
	time.sleep(0.3)




