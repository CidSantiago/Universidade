# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 17:31:31 2016

@author: Caio Cid Santiago
"""
import scipy.optimize as scpo

def r(t):
    return 100*(1+(3.90802*(10**-3))*t-(0.580195*(10**-6))*(t**2)) - 200


def Bissection(f,a,b,tol):
    an = a
    bn = b
    i = 1
    xns = (an + bn)/2
    
    while abs(f(xns))>tol:
        if f(an)*f(xns) < 0:
            bn = xns
        else:
            an = xns
        i = i + 1
        xns = (an + bn)/2
    return xns,i
    
bis,ite = Bissection(r,250,270,0.001)
solv = scpo.fsolve(r,260)

print("\nIterações: ",ite)
print("Resultado pela Bisseção: ", bis)
print("Resultado pela fsolve(): ", float(solv) ) 