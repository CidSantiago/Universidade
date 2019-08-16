# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:15:14 2016

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
    
def Gauss(a,b):
    ab = np.zeros((len(a),len(a[0])+1))
    
    for i in range(0,len(ab)):
        ab[i] = np.append(a[i],b[i])
        #ab[i].append(b[i])
    
    #Escalonacao  
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

#Variaveis
f_c = 2e9 # Frequência do sistema é de 2 GHz
v = 3/3.6 # Velocidade do móvel de 3 km/h (pedestre)
L = 20    # O canal possui 20 multi-percursos
grau = 4

# Gera as amostras do canal
t = np.array([0,20,40,60,80])
g = Jakes(t, f_c, v, L)

x = np.zeros((len(t),grau+1))
for i in range(0,len(x)):
    for j in range(0, grau+1):
        x[i][j] = t[i]**j

pol = Gauss(x,g)

tpol = np.arange(0,81,1)
plt.plot(t, g, 'ro', label = ' g(t) ')
plt.plot(tpol, (pol[4]*tpol**4 + pol[3]*tpol**3 + pol[2]*tpol**2 + pol[1]*tpol**1 + pol[0]*tpol**0), 'b-', label = 'Polinomio interpolador' )
plt.legend()
plt.grid()
plt.xlabel('$t$ (em $ms$)')
plt.title('Gráfico do polinômio interpolador')
plt.show()
