#!/usr/bin/etc python

# Import some necessary libraries.
import socket
import time
import os

 
# Some basic variables used to configure the bot
server = "irc.inet.tele.dk" # Server
channel = "#A-177" # Channel
botnick = "dumbBot" # Your bots nick


kristian = "88:32:9B:62:85:F0"
thomas = "64:A3:CB:77:1E:27"
orjan = "34:23:BA:93:54:D5"


#Kristian, Orjan, Thomas
signals = [-999,-999,-999]

def ping(): # This is our first function! It will respond to server Pings.
    ircsock.send("PONG :pingis\n")
 
def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
    ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): # This function is used to join channels.
    ircsock.send("JOIN "+ chan +"\n")
 
def nearby(name):
    # Her kan du putte inn det som skal skrives ut og sette det inn i:
    ircsock.send("PRIVMSG"+ channel + name + " is nearby office\n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot
joinchan(channel) # Join the channel using the functions we previously defined

while 1==1:
    openDoor = 0;
    #ircmsg = ircsock.recv(2048) # receive data from the server
    #ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks. 
    #if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    #ping()
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
                #nearby("Kristian")
            signals[0] = signalStrength
        if thomas in line:
            var = line.split(' ')[5]
	    signalStrength = var[:(len(var)-1)]
            signalStrength = int(float(signalStrength))
	    print ("Thomas: " + str(signalStrength))
            if (signalStrength > signals[2] and signalStrength < -65 and signalStrength > -75):
	        print "open for Thomas"
                openDoor = 1
                #nearby("Thomas")
            signals[2] = signalStrength
        if orjan in line:
            var = line.split(' ')[5]
	    signalStrength = var[:(len(var)-1)]
            signalStrength = int(float(signalStrength))
	    print ("Orjan: " + str(signalStrength))
            if (signalStrength > signals[1] and signalStrength < -65 and signalStrength > -75):
	        print "open for Orjan"
                openDoor = 1
                #nearby("Orjan")
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


	    


