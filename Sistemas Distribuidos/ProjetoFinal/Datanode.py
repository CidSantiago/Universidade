# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:48:04 2017

@author: Cid Santiago & Alef Carneiro
"""

### A SER IMPLEMENTADO ###
# Tratamentos de exceção
##########################

import xmlrpc.server, xmlrpc.client
import os

def createFile(name):
    try:
        file = open('DB' + str(porta) + '/' + str(name) + '.txt','r')
        file.close()
        return False
    
    except FileNotFoundError as e:
        file = open('DB' + str(porta) + '/' + str(name) + '.txt','w')
        file.close()
        return True
    
def updateFile(data, name):
    try:
        with open('DB' + str(porta) + '/' + str(name) + '.txt','a') as handle:
            handle.write(data)
            handle.close()
        return True
    
    except FileNotFoundError as e:
        return False

def deleteFile(name):
    try:
        os.remove('DB' + str(porta) + '/' + str(name))
        return True
    except:
        return False
    
def readFile(name):
    try:
        with open('DB' + str(porta) + '/' + str(name) + '.txt', "r") as handle:
            data = handle.read()
        return data
    except FileNotFoundError as e:
        return False

global porta    
porta = input('Digite a porta que deseja utilizar:\n')

try:
    os.mkdir("DB" + str(porta))
except:
    print("Pasta já existente!:)\n")
# Recebendo informações do proxy
end_proxy = input("Digite o endereço do servidor proxy (http://<ip>:<porta>): ")
proxy = xmlrpc.client.ServerProxy(end_proxy)

# Registrando datanode no namenode
proxy.dnRegister(porta)

server = xmlrpc.server.SimpleXMLRPCServer(('localhost',int(porta)))
print('Datanode ' + str(porta) + ' ativo na porta ' + str(porta) + '...\n')

server.register_function(createFile,'createFile')
server.register_function(updateFile,'updateFile')
server.register_function(deleteFile,'deleteFile')
server.register_function(readFile,'readFile')
server.serve_forever()
