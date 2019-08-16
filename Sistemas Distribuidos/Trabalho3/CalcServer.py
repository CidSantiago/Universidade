# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:10:00 2017

@author: Cid Santiago
"""
import xmlrpc.server,sys

def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

server = xmlrpc.server.SimpleXMLRPCServer(('localhost',7890))
print('Servidor ativo na porta 7890...\n')

server.register_function(soma,'soma')
server.register_function(sub,'sub')
server.register_function(mult,'mult')
server.register_function(div,'div')
server.serve_forever()
