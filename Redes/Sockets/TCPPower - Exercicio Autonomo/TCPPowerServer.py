# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:08:46 2017

@author: Cid Santiago
"""

import socket
serverPort = 13000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while (1):
    connectionSocket, addr = serverSocket.accept()
    Number = connectionSocket.recv(1024)
    Number = float(Number.decode('ascii'))
    message = '\nDigite agora a potencia.'
    connectionSocket.send(message.encode('ascii'))
    Power = connectionSocket.recv(1024)
    Power = float(Power.decode('ascii'))
    result = pow(Number,Power)
    message = '\nSeu resultado eh:'+str(result)
    connectionSocket.send(message.encode('ascii'))
    connectionSocket.close()