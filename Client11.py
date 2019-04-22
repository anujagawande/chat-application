"""
Note:
Compatible Version: Python 2.7.15

Since Python's latest versions are not backward compatible, this code wouldnt work
as expected in any later versions of python 2.7.15

Both Client and Server will have to run on the same machine

"""
import socket
import random
import sys
from threading import Thread

clientID = ''
chatMessage = ''

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 12221


print 'Connected to', host

def connect(host,port):
    """Call the server to get connection and receive the clientID which was sent by Server
    using socket's method 'connect'"""
    s.connect((host, port))
    print s.recv(1024)
    print s.recv(1024)

def sendMessage():
    #Using the socket's method 'send' to send the message to the server.
    while True:
        z = raw_input("")
        s.send(z)
        #s.send(z)
        if(z.strip() == ".exit"):
            print "<<<<<<<Chat Session Ended>>>>>>"
            sys.exit(0)
            s.close()

def receiveMessage():
    #using the socket's method 'recv' to receive message from the server
    while True:
         receivedMessage = s.recv(1024)
         if not receivedMessage: sys.exit(0)
         print receivedMessage


if __name__ == '__main__':
    connect(host,port)
    """Using thread for receiveMessage and ChatMessage methods since this would allow the client
     to receive and send messages at the same time"""
    receiveMsgThread = Thread(target=receiveMessage)
    receiveMsgThread.start()
    sendMsgThread = Thread(target=sendMessage)
    sendMsgThread.start()
