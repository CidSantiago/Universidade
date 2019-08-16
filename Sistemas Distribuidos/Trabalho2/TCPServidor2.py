# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 11:55:08 2017

@author: Cid Santiago
"""
import socket, pickle, threading,sys

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

#Função a ser utilizada na thread. Nessa função, é passado o socket como parâ-
#metro. Ela recebe uma mensagem do cliente, como o objeto serializado e traduz
#de volta para o objeto normal. Depois, com uma trava, ela escreve no arquivo 
#a operação realizada. Por fim, ela retorna o resultado para o cliente e termi-
#na a conexão.
def conexao(conectionSocket, addr):
    req = conectionSocket.recv(1024)
    loadReq = pickle.loads(req)
    result = loadReq.resultado()
    with lock:
        log = open('log.txt','a')
        log.write('[%s][%s]\n'%(loadReq,addr[0]))
        log.close()
    conectionSocket.send(result.encode('utf-8'))
    conectionSocket.close()

#Inicialização das variáveis.
serverPort = int(sys.argv[1])
lock = threading.Lock()
threads = []

#Configurando e inicializando o socket.
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen()

print ('The server is ready to receive')

#Laço infinito do socket servidor. Nesse laço, quando o servidor recebe uma co-
#nexão, ele inicializa uma thread com a função especificada a cima e executa
#ela.
while True:
    connectionSocket, addr = serverSocket.accept()
    threads.append(threading.Thread(target = conexao,
                                    args=(connectionSocket,addr)))
    threads[len(threads)-1].start()