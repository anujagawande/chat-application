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
from thread import *

clientIDsList = {}
chatMessage = ''
destinationClientId = ''

s = socket.socket()
host = socket.gethostbyname('localhost')
port = 12221
s.bind((host, port))
s.listen(10)

"""request from the client to get connection are processed here
    using socket's method 'accept' to accept the connection"""


def acceptConnection(host, port):
    conn, addr = s.accept()
    """Generating a clientID (creating random number from 1 to 101 and appending with 'Client'count
    Adding new client in-to clientIDsList"""
    clientID = str(random.randint(1, 101)) + "_Client" + str(len(clientIDsList) + 1)
    clientIDsList[clientID] = conn
    # Sending welcome message and list of available clients for chatting to the connected client
    sendMessage("Welcome to this chatroom, " + clientID + "!\n", conn)
    broadcast(clientID + " joined the chatroom.\n", conn)
    broadcast("Updated list of available Clients are : " + str(clientIDsList.keys()),conn)
    sendMessage("List of available Clients are : " + str(clientIDsList.keys()),conn)

    return conn, addr, clientID


def disconnectConnection(connection, clientID):
    """Request from the client to exit from the chat session using '.exit'
    Remove the clientID from clientIDsList and notify all the available clients"""
    if clientID in clientIDsList:
        clientIDsList.pop(clientID)
        messageToBroadcast = "Client '" + clientID + "' exited from the Chat server"
        print messageToBroadcast
        broadcast(messageToBroadcast, connection)
        broadcast("\n", connection)
        broadcast("\n", connection)
        broadcast("Updated list of available Clients are : " + str(clientIDsList.keys()), connection)
        #Display updated list of clients after someone leaves

def broadcast(message, connection):
    for clientID, conn in clientIDsList.iteritems():
        if (conn != connection):
            try:
                conn.send(message)
            except:
                conn.close()


def sendMessage(chatMessage, clientID):
    # Using the socket's method 'send' to send the message to the client
    clientID.send(chatMessage)


def clientthread(conn, addr, clientID):
    while True:
        try:
            message = conn.recv(2048)
            if message:
                if (message.strip() == ".exit"):
                    disconnectConnection(conn, clientID)
                else:
                    msg = message.split('--')
                    if (len(msg) < 2):
                        sendMessage("**********************************\nUsage: Message [--destinationClientID] ", conn)
                        sendMessage("Ex: To send a message to the client '55_Client1':   Hi Client --55_Client1 \n",
                                    conn)
                        sendMessage(
                            "To send a broadcast message to all the connected clients, use this format:   Message --ALL \n",
                            conn)
                    else:
                        message_to_send = "<" + clientID + "> " + msg[0]
                        for i in range(1, len(msg)):
                            toClientID = msg[i].strip()

                            if toClientID == 'ALL':
                                # Send message to all connnected clients
                                broadcast(message_to_send, conn)
                            else:
                                if toClientID in clientIDsList:
                                    # if the client tries to send message to itself
                                    if toClientID == clientID:
                                        sendMessage(
                                            "You cannot send message to yourself. Please enter valid available clientID",
                                            conn)
                                    else:
                                        # Send the message to the destination Client
                                        toClient = clientIDsList[toClientID]
                                        sendMessage(message_to_send, toClient)
                                else:
                                    # Send error message to the From Client when the destination Client is unavailable
                                    sendMessage(
                                        "Client '" + toClientID + "' is unavailable for the chat/not connected to the Server",
                                        conn)
                                    sendMessage("List of available Clients are : " + str(clientIDsList.keys()), conn)

            else:
                """message may have no content if the connection 
                is broken, in this case we remove the connection"""
                disconnectConnection(conn, clientID)

        except:
            continue


if __name__ == '__main__':
    print "Chat Server is up and running. Clients can establish connection now"
    print "Server Details: Host -" + str(host) + " port -" + str(port)

    while True:
        conn, addr, clientID = acceptConnection(host, port)
        print "New client '" + clientID + "' is connected to the Chat server"
        # creates an individual thread for every client that connects
        start_new_thread(clientthread, (conn, addr, clientID))

