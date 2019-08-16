# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 15:12:02 2017

@author: Cid Santiago
"""

import socket

serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')

while (1):
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode('ascii')
    modifiedMessage = modifiedMessage.upper()
    modifiedMessage = modifiedMessage.encode('ascii')
    serverSocket.sendto(modifiedMessage, clientAddress)