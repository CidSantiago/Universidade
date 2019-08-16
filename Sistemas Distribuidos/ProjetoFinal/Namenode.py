# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 04:22:41 2017

@author: Cid Santiago & Alef Carneiro
"""

### A SER IMPLEMENTADO ###
# Retorno para sucesso e para falha
# Tratamentos de falha
##########################

import xmlrpc.server
from hashlib import sha256

def dnRegister(porta):
    try:	
        fdatanodes = open('datanodes.txt', 'a')
        fdatanodes.write(str(porta) + '\n')
        fdatanodes.close()
        datanodes.append(int(porta))
        return True
    except FileNotFoundError as e:
        return False

def getFileDN(name):
    name_cript = sha256(name.encode('utf-8')).hexdigest()
    numberdn = len(datanodes)
    dn_number = int(name_cript, 16) % numberdn 
    
    if numberdn == (dn_number + 1):
        return [datanodes[dn_number], datanodes[0]]
    else:
        return [datanodes[dn_number], datanodes[dn_number+1]]

# Configurando namenode
porta = input('Digite a porta que deseja utilizar:\n')

# Iniciando servidor
nn = xmlrpc.server.SimpleXMLRPCServer(('localhost', int(porta)))
print('Namenode ativo na porta ' + str(porta) + '...\n')

# Iniciando lista com datanodes
global datanodes
datanodes = []

try:
	fdatanodes = open('datanodes.txt', 'r')
	linha = fdatanodes.read()
	while linha != '':
		datanodes.append(int(linha))
	del linha
except FileNotFoundError as e:
	fdatanodes = open('datanodes.txt', 'w')

fdatanodes.close()

# Registrando funções
nn.register_function(dnRegister, 'dnRegister')
nn.register_function(getFileDN, 'getFileDN')
nn.serve_forever()