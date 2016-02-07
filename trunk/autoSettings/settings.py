#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, sys, os
import re
import serial.tools.list_ports
import time

#updated as of 2-6-2015 cureent settings.
#head start at back right of cutting bed.
output_list = ['$0=10','$1=255','$2=0','$3=0','$4=0','$5=0',
		'$6=0','$10=3','$11=0.010','$12=0.002','$13=0',
		'$20=0','$21=0','$22=0','$23=0','$24=25.000',
		'$25=500.000','$26=250','$27=1.000','$100=400.00',
		'$101=400.000','$102=400.00','$110=500.000',
		'$111=5000.000','$112=500.000','$120=20.000',
		'$121=20.000','$122=10.000','$130=220.000',
		'$131=55.000','$133=200.000']

recieved_settings = []

VER = "A2 ParraPortCNC Settings default config"
ret = "\r"
temp = ""
counter = 0



def checkFile():
	#check if our settings file is available if not create it.
	#this may be rundundant.
	global sfile 
	if os.path.isfile("settings.dat"):
		print "settings file exits"
	else:
		print "file does not exist"
		response = raw_input("Create default settings file? :")
		if response == 'y' or response == 'Y':
			sfile = open("settings.dat","w")
			for index in output_list:
				sfile.write(str(index)+"\n")
		else:
			print "Settings file not created.\n"
		return

def readSettings():
	#read the settings from the micro.
	global recieved_settings
	inst.write('$$\r')
	counter = 0
	ref = 1
	while ref == 1:
		time.sleep(.1)
		temp = inst.readline()
		print temp + "\n"	
		recieved_settings.append(temp)
		if temp.find('OK'):
			counter += 1
		if counter == 32:
			ref = 0
		
		
def saveRecievedSettings():
	#save the settings from the micro.
	rfile = open("recievedSettings","w")
	for index in recieved_settings:
		if not temp.find("Grbl"):
			rfile.write(str(index) + "\n")

def compareSettings():
	#compare our settings verses whats on the device.
	print "foo"			

def connectDevice():
	#connect to device.
	global inst 
	inst = serial.Serial('/dev/ttyUSB0','115200',timeout=10)

def sendDefaultSettings():
	#send default settings to ParraPortCNC
	#array of settings here.
	for index in output_list:
		inst.write(index+'\r')
		temp = inst.readline()
		if temp.find('OK'):
			print "Setting recieved.\n"
		else:
			print "Nope.\n"
		time.sleep(.1)
		

print VER
print ret

#check to see if our settings file is there. if not create default.
checkFile()
time.sleep(1)
#connect to the micro
connectDevice()

#This kick starts the serial, no indea. just a horible coder..
inst.write('$$\r')
response = inst.readline()

#check to see if its actualy our controller.
if response.find('Grbl'):
	print "---------"
	print "Connected"
	print "---------\n"
else:
	print "Device not found\n"

#ask if the micro is there.
#inst.write('$$\r')
readSettings()
saveRecievedSettings()
#while 1:

	#read in the serial data
#	temp =  inst.readline()
	#time to buffer
#	time.sleep(.1)
#	print temp
#	time.sleep(.1)
	
	#check to see if we are done processing.
#	if temp.find('OK'):
#		counter += 1
#		if counter == 32:
			#sendDefaultSettings()
#			break


