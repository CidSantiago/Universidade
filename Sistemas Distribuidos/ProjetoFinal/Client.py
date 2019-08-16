# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 11:57:26 2017

@author: Cid Santiago & Alef Carneiro
"""

### A SER IMPLEMENTADO ###
# Retorno para sucesso e para falha
# Tratamentos de falha
##########################

import xmlrpc.client

def createFile(name):
    flag = proxy.createFile(name)
    return flag

def updateFile(arg, name):
    flag = proxy.updateFile(arg, name) 
    return flag

def deleteFile(name):
    flag = proxy.deleteFile(name)
    return flag

def readFile(name):
    data = proxy.readFile(name)
    if data != False:
       print(data) 
    else:
        return False

# Recebendo configurações do proxy
end_proxy = input("Digite o endereço do servidor proxy (http://<ip>:<porta>): ")
proxy = xmlrpc.client.ServerProxy(end_proxy)
global proxy

#### MENU ####
try:
    op = -1
    while op != 0:
        print("Escolha uma das opções abaixo:\n")
        print("1) Criar arquivo\n")
        print("2) Atualizar arquivo\n")
        print("3) Ler arquivo\n")
        print("4) Apagar arquivo\n")
        print("0) Sair")

    if op == 0:
        print("\rTchauzinho ;)\n")
        break;
    elif op == 1:
        name = input("Digite o nome do novo arquivo: \n")
        
        if createFile(name):
            print("Operação bem sucedida! :D\n")
        else:
            print("Operação falhou! :(\n")
    elif op == 2:
        name = input("Digite o nome do arquivo a ser atualizado: \n")
        arg = input("Digite o conteúdo do arquivo:\n")
        
        if updateFile(arg, name):
            print("Operação bem sucedida! \n:D")
        else:
            print("Operação falhou! :(\n")         
    elif op == 3:
        name = input("Digite o nome do novo arquivo: \n")
        
        if readFile(name):
            print("Operação bem sucedida! :D\n")
        else:
            print("Operação falhou! :(\n")
    elif op == 4:
        name = input("Digite o nome do novo arquivo: \n")
        
        if deleteFile(name):
            print("Operação bem sucedida! :D\n")
        else:
            print("Operação falhou! :(\n")
            
except KeyboardInterrupt as ki: 
    print("\rTchauzinho ;)\n")