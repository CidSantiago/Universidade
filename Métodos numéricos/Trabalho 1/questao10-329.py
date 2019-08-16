# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:09:18 2016

@author: Caio Cid Santiago
"""
import math
import scipy.optimize as scpo

def f(x):
    return (24/(((140**2)+(((2*math.pi*x)*260*(10**-3)) - (1/((2*math.pi*x)*25*(10**-6))))**2)**0.5) - 0.15)
  
def Secant(f,x1,x2,tol):
    i = 1
    xns = x2 - ((f(x2)*(x2-x1))/(f(x2)-f(x1)))
    xtmp = x2
    while abs(f(xns))>tol :
        tmp = xns        
        xns = xns - ((f(xns)*(xns-xtmp))/(f(xns)-f(xtmp)))
        xtmp = tmp        
        i = i + 1
    return xns,i

real = float(scpo.fsolve(f,40))
raiz, iterações = Secant(f,30,50,0.0001) 
print("Raiz da função:              ",raiz)
print("Iterações:                   ",iterações)
print("Raiz calculada com fsolve(): ",real)