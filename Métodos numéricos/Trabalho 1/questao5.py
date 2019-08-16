# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 14:34:58 2016

@author: Caio Cid Santiago
"""

#Função para arredondar o valor para 3 algarismos significativos
def round3(x):
    return float(format(x,'.3g'))

#Primeira funçao completa, sem manipulações. Arredondada para 3 algarismos significativos.
def pcomp3(x):
    result = round3(round3(x*x)*x)
    result = round3(result+ round3(round3(x*x)*-7))
    result = round3(result + round3(8*x))
    result = round3(result - 0.35)
    return result

#Segunda funçao completa, COM manipulações. Arredondada para 3 algarismos significativos
def pmani3(x):
    result = round3(round3(round3(round3(round3(x-7)*x)+8)*x)-0.35)
    return result


valorreal = (1.37**3) -7*(1.37**2) + 8*1.37 - 0.35

print("\nResultado do cálculo do polinomio que não foi manipulado: "+str(pcomp3(1.37)))
print("\nErro Relativo Absoluto do polinomio que não foi manipulado: "+str(abs((pcomp3(1.37)-valorreal)/valorreal)))
print("\nResultado do cálculo do polinomio que FOI manipulado: "+str(pmani3(1.37)))
print("\nErro Relativo Absoluto do polinomio que FOI manipulado: "+str(abs((pmani3(1.37)-valorreal)/valorreal)))
