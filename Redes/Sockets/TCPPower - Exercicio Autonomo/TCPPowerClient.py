# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:28:45 2017

@author: Cid Santiago
"""

import socket

serverName = input('Digite o IP do servidor\n')
serverPort = 13000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

arg = input('Coloque seu número:')
clientSocket.send(arg.encode('ascii'))
message = clientSocket.recv(1024)
arg = input(message.decode('ascii'))
clientSocket.send(arg.encode('ascii'))
message = clientSocket.recv(1024)
print ('From Server:'+message.decode('ascii'))
clientSocket.close()