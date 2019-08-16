# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:03:21 2016

@author: Caio Cid Santiago
"""

import numpy as np
import matplotlib.pyplot as plt

def Jakes(t, f_c, v, L):
    # f_c é dada em Hertz
    # v é dada em m/s
    # c é 3 x 10^8 m/s
    c = 3e8;
    # Gera as fases aleatórias entre [0, 2*pi]
    Phi = np.pi * np.random.random(L);
    phi = np.pi * np.random.random(L);
    # Calcula o máximo desvio Doppler
    f_D = v*f_c/c
    # Calcula g usando uma python list comprehension
    g = np.array( [ np.abs((1/np.sqrt(L))*np.sum(np.exp(1j*(2*np.pi*f_D*np.cos(Phi)*x + phi))))**2 for x in t ] )
    return g

# Implemente sua solução aqui acompanhada de um exemplo de uso.
#
# Observação: Quando rodado no sistema operacional Linux, a função funcionou perfeitamente. 
# Porém, no Windowns 10.1, o polinômio de terceira ordem exibe resultados muito semelhantes 
# ao de segunda ordem, apesar de gerar 4 coeficientes distintos.
# 
def GaussMod(x): #Gauss recebendo matriz estendida => AB
    ab = x
    
    #Escalonamento  
    for j in range(0, len(ab[0])-1):
        for i in range(j+1,len(ab)):
            m = ab[i][j]/ab[j][j]
            for p in range(0,len(ab[i])):
                ab[i][p] = ab[i][p] - m*ab[j][p]
    
    #Substituicao
    x = np.zeros(len(ab))    
    
    for i in range(len(ab)-1,-1,-1):
        x[i] = ab[i][len(ab[i])-1]/ab[i][i]
        for j in range(0,len(x)):
            if i!=j:
                x[i] = x[i] - ((ab[i][j]*x[j])/ab[i][i])
    
    return x

def regressao(x,y,ordem):
    
    matrizest = np.zeros((ordem+1,ordem+2))
        
    for i in range(0,len(matrizest)):
        for j in range(0,len(matrizest[i]-1)):
            matrizest[i][j] = np.sum(x**(i+j))
        matrizest[i][len(matrizest[i])-1] = np.sum((x**i)*y)
    
    return matrizest


#Variaveis
f_c = 2e9 # Frequência do sistema é de 2 GHz
v = 3/3.6 # Velocidade do móvel de 3 km/h (pedestre)
L = 20    # O canal possui 20 multi-percursos
t = np.array([0,10,20,30,40])

g = Jakes(t, f_c, v, L)

primeira = GaussMod(regressao(t,g,1))
segunda = GaussMod(regressao(t,g,2))
terceira = GaussMod(regressao(t,g,3))

polyprimeira = np.polyfit(t,g,1)
polysegunda = np.polyfit(t,g,2)
polyterceira = np.polyfit(t,g,3)

tpol = np.arange(0,41,1)

#print(segunda)
#print(polysegunda)
#print(terceira)
#print(polyterceira)

plt.figure(4)
plt.plot(t, g, 'ro', label = ' g($t$) ')
plt.plot(tpol, (primeira[1]*tpol**1 + primeira[0]*tpol**0), 'b-', label = 'Polinomio de Primeira ordem' )
plt.plot(tpol, (polyprimeira[0]*tpol**1 + polyprimeira[1]*tpol**0) , 'g^', label = 'Polyfit de Primeira Ordem') 
plt.legend()
plt.grid()
plt.xlabel('$t$ (em ms)')
plt.title('Gráfico da Regressão Polinomial de Primeira Ordem')
plt.show()

plt.figure(5)
plt.plot(t, g, 'ro', label = ' g($t$) ')
plt.plot(tpol, (segunda[2]*tpol**2 + segunda[1]*tpol**1 + segunda[0]*tpol**0), 'b-', label = 'Polinomio de Segunda Ordem' )
plt.plot(tpol, (polysegunda[0]*tpol**2 + polysegunda[1]*tpol**1 + polysegunda[2]*tpol**0), 'g^', label = 'Polyfit de Segunda Ordem' )
plt.legend()
plt.grid()
plt.xlabel('$t$ (em ms)')
plt.title('Gráfico da Regressão Polinomial de Segunda Ordem')
plt.show()

plt.figure(6)
plt.plot(t, g, 'ro', label = ' g($t$) ')
plt.plot(tpol, (terceira[3]*(tpol**3.) + terceira[2]*(tpol**2.) + terceira[1]*(tpol**1.) + terceira[0]*(tpol**0.)), 'b-', label = 'Polinomio de Terceira de ordem' )
plt.plot(tpol, (polyterceira[0]*(tpol**3.) + polyterceira[1]*(tpol**2.) + polyterceira[2]*(tpol**1.) + polyterceira[3]*(tpol**0.)), 'g^', label = 'Polyfit de Terceira de ordem' )
plt.legend()
plt.grid()
plt.xlabel('$t$ (em ms)')
plt.title('Gráfico da Regressão Polinomial de Terceira Ordem')
plt.show()
