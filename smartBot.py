# Import some necessary libraries.
import socket

# Some basic variables used to configure the bot
server = "irc.inet.tele.dk" # Server
channel = "#A-177" # Channel
botnick = "SmartBot" # Your bots nick

kristian = "88:32:9B:62:85:F0"
thomas = "64:A3:CB:77:1E:27"
orjan = "34:23:BA:93:54:D5"

def getTimeStamps():
    inputFile = open('output-01.csv')
    sendmsg("The timestamp is when they were last seen")
    sendmsg("")
    for line in inputFile.read().splitlines():
        if kristian in line:
            sendmsg("Kristian: " + line.split(',')[2])
        elif thomas in line:
            sendmsg("Thomas: " + line.split(',')[2])
        elif orjan in line:
            sendmsg("Orjan: " + line.split(',')[2])


def ping(): # This is our first function! It will respond to server Pings.
    ircsock.send("PONG :pingis\n")

def sendmsg(msg): # This is the send message function, it simply sends messages to the channel.
    ircsock.send("PRIVMSG " + channel + " :" + msg + "\n")

def joinchan(chan): # This function is used to join channels.
    ircsock.send("JOIN " + chan + "\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
    ircsock.send("PRIVMSG " + channel + " :Hello!\n")

def inOffice():
    getTimeStamps()



ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This bot is a result of a tutoral covered on http://shellium.org/wiki.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
    ircmsg = ircsock.recv(2048) # receive data from the server
    ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
    print(ircmsg) # Here we print what's coming from the server

    if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
        hello()

    if ircmsg.find(":In "+ botnick) != -1:
        inOffice()

    if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
        ping()
