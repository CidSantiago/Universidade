# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:48:53 2017

@author: Cid Santiago
"""

import socket
serverName = '192.168.1.101'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')

clientSocket.sendto(message.encode('ascii'),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('ascii'))
clientSocket.close()