#!/usr/bin/python
#----------------------------------------------------------------------------------------
#I used Open source Zigbee example and python DB Connection example. -> Googled :)
#I used Raspberry pi 3 B+, Raspbian Stretch, Xbee S1 module + SparkFun Requlated board
#I used GPIO 14, 15 (RX, TX) and 5V GPIO pin(3.3v was less power)
#This is use Zigbee Module and use Serial Communication, So Bluetooth Serial block first!
#I use to IOT Device, projcet - Zigb'all
#Send to Arduino Zigbee module and Send from Raspberry pi Server
#Thinks! :)
#https://github.com/bckim9489
#"CommIT Embedded Team of KMU" 
#----------------------------------------------------------------------------------------
import sys
import serial
import MySQLdb #<- require MySQLdb, install plz!
#-----------------------------------------
#							Database_connect
#-----------------------------------------
#TODO "better then use ORM, but we are busy..." .by bckim // 18th May 2019

para_mac = sys.argv[1]
para_name = sys.argv[2]
#'para_mac', 'para_name' is use php served parameter
sql = "SELECT func FROM user_set \
			 WHERE mac ='"+para_mac+"' \
			 AND name ='"+para_name+"'"

db = MySQLdb.connect(host="localhost", \
		user ="root", \
		passwd="1q2w3e4r", \
		db="db")

cur = db.cursor()
cur.execute(sql)
for row in cur.fetchall():	
	func = row[0]
	
#-----------------------------------------
#							main_function()
#-----------------------------------------
if __name__ == '__main__':
#xbee = serial.Serial('/dev/ttyAMA0', 9600)
	xbee = serial.Serial()
	xbee.port = '/dev/ttyAMA0' #This was a bluetooth port, and I disabled bluetooth
	xbee.baudrate = 9600
	xbee.timeout = 1
	xbee.writeTimeout = 1
	xbee.open()
	string = 'Hello Raspberry Pi XBee'
	print "%s" % string
	command = func
	print command
	print "Send!"
	xbee.write(command)
	print "isLisening..."
	while True:
		data = xbee.readline()
		print data
		if data == 'A':
			break
	xbee.close()
