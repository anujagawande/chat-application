Simple Python Chat Application 

~Supports multiple clients~

Prerequisites:

1. Install Python 2.7.15 (Since Python's latest versions are not backward compatible, this code wouldnt work 
as expected in any later versions of python 2.7.15)

2. Make sure localhost is configured. Usually in mac and windows it must be default and work fine. If the below outputs are coming then configurations are required. 

ex:

a. The below python execution must return some value

import socket
socket.gethostbyname('localhost')


Output:
'127.0.0.1'

b. ping localhost in command prompt should succeed

Note: Both the client and Server must run in the same machine

How to execute the program:
1. First run the server.py
		>>>python Server.py
		
	Make sure the following message is displayed: 
	Chat Server is up and running. Clients can establish connection now
	Server Details: Host -XXXXX port -XXXX
	
2. Now start clients
	>>>python Client.py
	
	The following message will be displayed in this format:
	Connected to XXXXX
	Welcome to this chatroom, 61_Client1!
	List of available Clients are : ['61_Client1']
	
3. To start one more client just repeat the step 2
	>>>python Client.py
	Connected to XXXXXX
	Welcome to this chatroom, 41_Client2!
	List of available Clients are : ['61_Client1', '41_Client2']

4. Likewise open as many as client you want

5. Send message:
	To send a message to client, then type the messages in the below formats from any client:

   Format: your Message --ClientID
Ex:

To send message to a client use its ID in this format:
Hi --41_Client2


To send message to multiple clients use their IDs in this format:
Hi --41_Client2 --61_Client1

To send message to all the connected clients use their IDs in this format:
Hi --ALL

6. For client to exit from the server, just type the below:
.exit
