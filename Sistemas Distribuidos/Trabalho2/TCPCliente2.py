# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 13:51:41 2017

@author: Cid Santiago
"""

import socket,pickle,sys

#Classe responsável por transportar os numeros e executar as operações
class Requisiçao:
    #Construtor da classe
    def __init__(self, numero1, numero2, operacao):
        self.Num1 = numero1
        self.Num2 = numero2
        self.Operacao = str(operacao)
    
    #Representação da classe quando chamada.    
    def __repr__(self):
        return "%s %s %s"\
        %(self.Num1, self.Num2, self.Operacao)
    
    #Metodo que executa as operações das classes.
    def resultado(self):
        if self.Operacao == 'soma':
            return (self.Num1 + self.Num2)
        elif self.Operacao == 'sub':
            return (self.Num1 - self.Num2)
        elif self.Operacao == 'div':
            return (self.Num1 / self.Num2)
        elif self.Operacao == 'multi':
            return (self.Num1 * self.Num2)
        else:
            return 'Operação invalida'

#Inicialização das variáveis
serverName = str(sys.argv[1])
serverPort = int(sys.argv[2])
num1 = float(sys.argv[3])
num2 = float(sys.argv[4])
op = str(sys.argv[5])

#Criando o Objeto da classe requisição
requisicao = Requisiçao(num1,num2,op)

#Criando o socket, configurando o timeout e conectando com o servidor.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.settimeout(5)
clientSocket.connect((serverName,serverPort))

#Enviando o objeto serializado pelo pacote pickle, recebendo uma string com o 
#resultado de volta, e imprimindo na tela o resultado recebido do servidor.
clientSocket.send(pickle.dumps(requisicao))
result = clientSocket.recv(1024)
result = result.decode('utf-8')
print ('From Server:'+result)

#Fechando o socket do cliente.
clientSocket.close()