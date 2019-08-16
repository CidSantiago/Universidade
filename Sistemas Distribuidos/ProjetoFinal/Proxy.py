# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 03:47:24 2017

@author: Cid Santiago & Alef Carneiro
"""

### A SER IMPLEMENTADO ###
# Retorno para sucesso e para falha
# Tratamentos de falha
##########################

import xmlrpc.client, xmlrpc.server

def createFile(name):
    dn=[]; flag = []
    end_dn = str(nn.getFileDN(name))
    dn.append(xmlrpc.client.ServerProxy("http://localhost:" + str(end_dn[0])))
    dn.append(xmlrpc.client.ServerProxy("http://localhost:" + str(end_dn[1])))
    flag.append(dn[0].createFile(name))
    flag.append(dn[1].createFile(name))
    
    if flag[0] and flag[1]:
        return True
    else:
        return False

def updateFile(arg, name):
    dn=[]; flag = []
    end_dn = str(nn.getFileDN(name))
    dn.append(xmlrpc.client.ServerProxy("http://localhost:" + str(end_dn[0])))
    dn.append(xmlrpc.client.ServerProxy("http://localhost:" + str(end_dn[1])))

    flag.append(dn[0].updateFile(arg, name))
    flag.append(dn[1].updateFile(arg, name))
    
    if flag[0] and flag[1]:
        return True
    else:
        return False

def deleteFile(name):
    dn =[]; flag = []
    end_dn = str(nn.getFileDN(name))
    dn.append(xmlrpc.client.ServerProxy("http://localhost:" + str(end_dn[0])))
    dn.append(xmlrpc.client.ServerProxy("http://localhost:" + str(end_dn[1])))
    
    flag.append(dn[0].deleteFile(name))
    flag.append(dn[1].deleteFile(name))
    
    if flag[0] and flag[1]:
        return True
    else:
        return False


# Registra o DN no NN
def dnRegister(porta):
    if nn.dnRegister(porta):
        return True
    else:
        return False

def readFile(name):
    end_dn = str(nn.getFileDN(name))
    dn = xmlrpc.client.ServerProxy("http://localhost:" + end_dn[0])
    try:
        data = dn.readFile(name)
        return data
    except:
        try:
            dn = xmlrpc.client.ServerProxy("http://localhost:" + end_dn[1])
            data = dn.readFile(name)
            return data
        except:
            return False

# Configurando proxy
porta = input('Digite a porta que deseja utilizar:\n')

# Recebendo configurações do namenode
end_nn = input("Digite o endereço do servidor namenode (http://<ip>:<porta>): ")
global nn
nn = xmlrpc.client.ServerProxy(end_nn)

# Iniciando servidor
proxy = xmlrpc.server.SimpleXMLRPCServer(('localhost', int(porta)))
print('Proxy ativo na porta ' + str(porta) + '...\n')

# Registrando funções
proxy.register_function(createFile, 'createFile')
proxy.register_function(deleteFile, 'deleteFile')
proxy.register_function(updateFile, 'updateFile')
proxy.register_function(readFile, 'readFile')
proxy.register_function(dnRegister, 'dnRegister')
proxy.serve_forever()