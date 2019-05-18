#!/usr/bin/python
import sys
import serial

if __name__ == '__main__':
#xbee = serial.Serial('/dev/ttyAMA0', 9600)
	xbee = serial.Serial()
	xbee.port = '/dev/ttyAMA0'
	xbee.baudrate = 9600
	xbee.timeout = 1
	xbee.writeTimeout = 1
	xbee.open()
	string = 'Hello Raspberry Pi XBee'
	print "%s" % string
#tes = "S180"
	command = sys.argv[1]
	print command 
	print "Send!"
	xbee.write(command)
	xbee.close()
