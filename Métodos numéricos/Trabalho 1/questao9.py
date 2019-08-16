# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:45:52 2016

@author: Caio Cid Santiago
"""

def f(x):
    return ((x)**3)- 7*((x)**2)+ 8*(x) - 0.35

def deriv(f,x,delta):
    return (f(x + delta*x) - f(x)) / delta*x

def ModifiedSecant(f,x,delta,tol):
    i = 1
    xns = x - (f(x)/deriv(f,x,delta))
    while abs(f(xns))>tol :
        xns = xns - (f(xns)/deriv(f,xns,delta))
        i = i + 1
    return xns,i

raiz,iterações = ModifiedSecant(f,0.05,0.000001,0.00000001)
print("Raiz da função: ",raiz)
print("Iterações: ",iterações)