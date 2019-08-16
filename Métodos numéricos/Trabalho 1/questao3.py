# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:17:39 2016

@author: Caio Cid Santiago
"""

def epsilon():
    e = 1
    while (1!= 1 + e):
        e = e/2
    return e*2
    
print("Epsilon da máquina: ",epsilon())