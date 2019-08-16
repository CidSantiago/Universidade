# -*- coding: utf-8 -*-msg
"""
Created on Thu Sep 21 16:31:06 2017

@author: Cid Santiago
"""

import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:7890/')

print('Calculadora RPC de Distribuidos :D')
a,b = input('Digite os números desejados:\n').split()
a = float(a)
b = float(b)

print('Operações')
print('1) Soma')
print('2) Subtração')
print('3) Multiplicação')
print('4) Divisão')

selection = input('Selecione a opção desejada:\n')

if selection == '1':
    msg = proxy.soma(a,b)
    print('O resultado da Soma é '+str(msg))

elif selection == '2':
    msg = proxy.sub(a,b)
    print('O resultado da Subtração é '+str(msg))
    
elif selection == '3':
    msg = proxy.mult(a,b)
    print('O resultado da Multiplicação é '+str(msg))

elif selection == '4':
    msg = proxy.div(a,b)
    print('O resultado da Divisão é '+str(msg))

