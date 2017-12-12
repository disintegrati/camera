import serial
import time
import os
arduino = serial.Serial("/dev/ttyACM0", 9600)
while True:
#          print arduino.readline()
	  x = arduino.readline()
	  if "1" in x:
		print "ricevo"
		os.system("sh /home/Desktop/camera/raspi/video2.sh")
		print "finito"
time.sleep(1)
