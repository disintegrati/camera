import serial
import time
arduino = serial.Serial("/dev/ttyACM2", 9600)
while True:
          print arduino.readline()
	  x = arduino.readline()
	  if "1" in x:
		print "ricevo"
time.sleep(1)
