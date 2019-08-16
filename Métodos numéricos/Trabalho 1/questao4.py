# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 17:56:31 2016

@author: Caio Cid Santiago
"""

import math

def expt1(x,N):
    
    result = 0
    if N==1:
        result = 1
        ErroRelativoReal = abs((math.exp(-5) - result)/math.exp(-5))
        return result , ErroRelativoReal
    elif N<=0:
        return 'Nao é possivel calcular sem variaveis!'
    else:
        result = 1
        ErroRelativoReal = [abs((math.exp(-5) - result)/math.exp(-5))]
        for i in range(1,N):
            result = result+ x**i/math.factorial(i)
            ErroRelativoReal.append(abs((math.exp(-5) - result)/math.exp(-5)))
        return result, repr(ErroRelativoReal)

def expt2(x,N):
    
    result = 0
    if N==1:
        result = 1
        ErroRelativoReal = abs((math.exp(-5) - result)/math.exp(-5))
        return result , ErroRelativoReal
    elif N<=0:
        return 'Nao é possivel calcular sem variaveis!'
    else:
        result = 1
        temp = 1
        ErroRelativoReal = [abs((math.exp(-5) - result)/math.exp(-5))]
        for i in range(1,N):
            temp = temp + abs(x**i/math.factorial(i))
            ErroRelativoReal.append(abs((math.exp(-5) - (temp**-1))/math.exp(-5)))
        result = temp**-1
        return result, repr(ErroRelativoReal)

    
a,b = expt1(-5,39)
print('Metodo 1:\n')
print('Valor: \n',a)
print('Erros Relativos Reais:\n',b)

c,d = expt2(-5,35)
print('\nMetodo 2:\n')
print('Valor: \n',c)
print('Erros Relativos Reais:\n',d)

#2.136883067284701e-13
#2.574557912391206e-16