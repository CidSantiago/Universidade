# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:45:22 2017

@author: cidsa
"""

import socket
serverPort = 13000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while (1):
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    sentence = sentence.decode('ascii')
    capitalizedSentence = sentence.upper()
    capitalizedSentence = capitalizedSentence.encode('ascii')
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()