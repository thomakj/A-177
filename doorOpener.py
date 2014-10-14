#!/usr/bin/etc python

# Import some necessary libraries.
import socket
import time
import os

kristian = "88:32:9B:62:85:F0"
thomas = "64:A3:CB:77:1E:27"
orjan = "34:23:BA:93:54:D5"


#Kristian, Orjan, Thomas
signals = [-999,-999,-999]


while 1==1:
    openDoor = 0;

    inputFile = open('output-01.csv')
    for line in inputFile.read().splitlines():
        if kristian in line:
            var = line.split(' ')[5]
	    signalStrength = var[:(len(var)-1)]
            signalStrength = int(float(signalStrength))
	    print ("Kristian: " + str(signalStrength))
            if (signalStrength > signals[0] and signalStrength < -55 and signalStrength > -70):
	        print "open for Kristian"
                openDoor = 1
            signals[0] = signalStrength
        if thomas in line:
            var = line.split(' ')[5]
	    signalStrength = var[:(len(var)-1)]
            signalStrength = int(float(signalStrength))
	    print ("Thomas: " + str(signalStrength))
            if (signalStrength > signals[2] and signalStrength < -60 and signalStrength > -75):
	        print "open for Thomas"
                openDoor = 1
            signals[2] = signalStrength
        if orjan in line:
            var = line.split(' ')[5]
	    signalStrength = var[:(len(var)-1)]
            signalStrength = int(float(signalStrength))
	    print ("Orjan: " + str(signalStrength))
            if (signalStrength > signals[1] and signalStrength < -55 and signalStrength > -70):
	        print "open for Orjan"
                openDoor = 1
            signals[1] = signalStrength
    if openDoor == 1:
        os.system('java -jar doorOpener.jar')
    inputFile.close
    time.sleep(1)












while 1: # Be careful with these! it might send you to an infinite loop
    ircmsg = ircsock.recv(2048) # receive data from the server
    ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
    print(ircmsg) # Here we print what's coming from the server

    if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
        hello()

    if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
        ping()
