# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:28:38 2016

@author: Caio Cid Santiago
"""
def f(x):
    return ((x)**3)- 7*((x)**2)+ 8*(x) - 0.35

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
    
def GoldenSection(f,a,b,tol):
    an = a
    bn = b
    i = 1
    k = (1 + 5**0.5)/2
    yns = (an + bn*k)/(k+1)
    zns = (an*k + bn)/(k+1)
    if abs(f(yns))<abs(f(zns)):
        xns = yns
    else:
        xns = zns
    while abs(f(xns))>tol :
        if f(an)*f(xns) < 0:
            bn = xns
        else:
            an = xns
        yns = (an + bn*k)/(k+1)
        zns = (an*k + bn)/(k+1)
        if abs(f(yns))<abs(f(zns)):
            xns = yns
        else:
            xns = zns
        i = i + 1
    return xns,i

raizbs, iteraçõesbs = Bissection(f,-2,1,0.0000000001)
raizgbs, iteraçõesgbs = GoldenSection(f,-2,1,0.0000000001)


print ("Raiz Bisseção: ",raizbs)
print ("Iterações Bisseção: ",iteraçõesbs)
print ("Raiz GoldenSection: ",raizgbs)
print ("Iterações GoldenSection: ",iteraçõesgbs)


#x^3−7x^2+8x−0,35