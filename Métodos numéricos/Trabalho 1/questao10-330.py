# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:07:08 2016

@author: Caio Cid Santiago
"""
import scipy.optimize as scpo
import math

def g(x):
    p = (1.6022 * (10**-19))/(1.3806*(10**-23)*297)
    return 0.5 - (math.log(1 + p*x)/p)

def f(x):
    p = (1.6022 * (10**-19))/(1.3806*(10**-23)*297)
    return math.exp(p*x)*(1+(p*x)) - math.exp(p*0.5)

def PontoFixo(f,g,x,tol):
    i = 1
    xns = g(x)
    while abs(f(xns))>tol:
        xns = g(xns)
        i = i + 1
    return xns,i
    
real = float(scpo.fsolve(f,0.5))    
resPF, itPF = PontoFixo(f,g,0.5,0.001)

print("\nNumero de iterações: ",itPF)
print("Valor do Ponto fixo: ",resPF)
print("Valor fsolve()     : ", real)