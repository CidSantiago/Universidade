# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 19:43:06 2016

@author: Caio Cid Santiago
"""
import math

def mcl(x,i):
    return (((-1)**i)*(x**(2*i)))/(math.factorial(2*i))

def CosMaclaurin8(x):
    real = math.cos(x)
    i = 0
    calc = 0
    while float(format(calc,'.8g')) != float(format(real,'.8g')):
        calc = calc + mcl(x,i)
        i = i+1
        print(calc)
    return i
        
print("\nNumero de iterações: ",CosMaclaurin8(0.3*math.pi))