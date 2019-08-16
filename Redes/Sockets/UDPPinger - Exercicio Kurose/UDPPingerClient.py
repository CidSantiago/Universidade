# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 19:12:56 2017

@author: Cid Santiago
"""

import socket,time
serverName = input('Digite o IP do servidor\n')
serverPort = 20000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSocket.settimeout(1)

nping = 0

while(nping<10):
    nping += 1
    message = 'Ping: '+str(nping)+' Tempo: '+str(time.time())
    RTTi = time.time()
    clientSocket.sendto(message.encode('ascii'),(serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        modifiedMessage = modifiedMessage.decode('ascii')
        RTT = (time.time() - RTTi)
        print('\nReply: '+serverAddress[0]+"\nMsg: "+modifiedMessage)
        print('RTT: '+str(RTT))
    except:
        print('\nPackage Timeout')
        continue

clientSocket.close()