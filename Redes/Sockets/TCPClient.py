# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:32:03 2017

@author: Cid Santiago
"""

import socket
serverName = '192.168.0.18'
serverPort = 13000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode('ascii'))
modifiedSentence = clientSocket.recv(1024)
modifiedSentence = modifiedSentence.decode('ascii')
print ('From Server:'+modifiedSentence)
clientSocket.close()