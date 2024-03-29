# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 18:31:35 2017

@author: Cid Santiago
"""

#We will need the following module to generate randomized lost packets

import random, socket

#Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 20000))

while (True):
    # Generate random number in the range of 0 to 10
    rand = random.randint(0,10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    message = message.decode('ascii')
    # Capitalize the message from the client
    message = message.upper()
    #If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    
    # Otherwise, the server responds
    serverSocket.sendto(message.encode('ascii'), address)