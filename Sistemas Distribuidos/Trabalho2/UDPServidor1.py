# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 08:32:09 2017

@author: Cid Santiago
"""

import socket,threading,sys

#Função que será utilizada com a thread. Nessa função, ela recebe uma messagem
#e inverte ela utilizando da variável global 'modified sentence'. Como é uma
#variável global, quando modificamos ela utilizamos uma trava, para não gerar
#condição de corrida.
def invertSentence(sentence):
    global modifiedSentence
    #Dentro da trava, a sentença está sendo invertida e codificada para poder 
    #ser enviada.
    with lock:
        modifiedSentence = sentence[::-1]
        invertedSentence = modifiedSentence.encode('ascii')
    serverSocket.sendto(invertedSentence, clientAddress)

#iniciaçização de variáveis.
lock = threading.Lock()
modifiedSentence = ''
threads = []
serverPort = int(sys.argv[1])

#Configurando o socket.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ('The server is ready to receive')

#Laço infinito do servidor. Nesse laço, ele recebe uma mensagem de um cliente,
#inicializa uma thread assim que a recebe e a executa.
while (1):
    message, clientAddress = serverSocket.recvfrom(2048)
    threads.append(threading.Thread(target=invertSentence, 
                                    args=(message.decode('ascii'),)))
    threads[len(threads)-1].start()
