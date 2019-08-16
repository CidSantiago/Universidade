# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:46:48 2016

@author: Caio Cid Santiago
"""
def f(x):
    return ((x)**3)- 7*((x)**2)+ 8*(x) - 0.35

def RegulaFalsi(f,a,b,tol):
    if (f(a)*f(b))>0:
        return print("Impossivel identificar a raiz no intervalo dado!") 
    else:        
        an = a
        bn = b   
        xns = (an*f(bn) - bn*f(an))/(f(bn)-f(an))
        i = 1
        while abs(f(xns))>tol:
            if (f(an)*f(xns))<0:
                bn = xns
            else:
                an = xns
            i = i + 1
            xns = (an*f(bn) - bn*f(an))/(f(bn)-f(an))
        return xns,i
    
def ModifiedRegulaFalsi(f,a,b,tol):
    if (f(a)*f(b))>0:
        return print("Impossivel identificar a raiz no intervalo dado!") 
    else:    
        an = a
        bn = b
        conta = 0
        contb = 0    
        xns = (an*f(bn) - bn*f(an))/(f(bn)-f(an))
        i = 1
        while abs(f(xns))>tol:
            if f(an)*f(xns)<0:
                bn = xns
                conta = conta + 1
                contb = 0
            else:
                an = xns
                contb = contb + 1
                conta = 0
            if conta == 3:
                xns = (an*f(bn) - bn*(f(an)/2))/(f(bn)-(f(an)/2))
                conta = 0
            elif contb == 3:
                xns = (an*(f(bn)/2) - bn*f(an))/((f(bn)/2)-f(an))
                contb = 0
            else:
                xns = (an*f(bn) - bn*f(an))/(f(bn)-f(an))
            i = i + 1
        return xns,i

raizrf, iteraçoesrf = RegulaFalsi(f,-2,1,0.000000001)
raizmrf, iteraçoesmrf = ModifiedRegulaFalsi(f,-2,1,0.000000001)

print ("Raiz Regula Falsi: ",raizrf)
print ("Iterações Regula Falsi: ",iteraçoesrf)
print ("Raiz Regula Falsi Modificado: ",raizmrf)
print ("Iterações Regula Falsi Modificado: ",iteraçoesmrf)

#x^3−7x^2+8x−0,35