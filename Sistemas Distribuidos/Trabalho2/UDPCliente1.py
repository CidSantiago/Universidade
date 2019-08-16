# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 08:54:35 2017

@author: Cid Santiago
"""

import socket, sys

#Inicializando as variáveis.
serverIP = str(sys.argv[1])
serverPort = int(sys.argv[2])
message = str(sys.argv[3])

#Configurando o socket.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)

#Enviando a messagem para ser invertida
clientSocket.sendto(message.encode('ascii'),(serverIP, serverPort))

#Tenta receber a mensagem invertida. Se não for recebida, ou seja, o tempo de 
#timeout expirar, entra no except e informa o erro.
try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode('ascii'))
except:
    print('Timeout')
    
clientSocket.close()