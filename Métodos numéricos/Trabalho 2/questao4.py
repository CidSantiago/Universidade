# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 14:20:21 2016

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

def GaussMod(x):
    ab = x
    
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
    
def splines(x,y,t):
    
    def f(a,x,y,i,t):
        termo1 = (a[i]/(6*(x[i+1]-x[i])))*((x[i+1] - t)**3)
        termo2 = (a[i+1]/(6*(x[i+1]-x[i])))*((t - x[i])**3)
        termo3 = ((y[i]/(x[i+1]-x[i])) - ((a[i]*(x[i+1]-x[i]))/6)) * (x[i+1] - t)
        termo4 = ((y[i+1]/(x[i+1]-x[i])) - ((a[i+1]*(x[i+1]-x[i]))/6)) * (t - x[i])
        return termo1 + termo2 + termo3 + termo4
    
    n = len(x)
    a = np.zeros(n)
    a[0] = 0
    a[n-1] = 0
    
    matriz = np.zeros((n-2,n-1))
    matriz[0][0] = 2*((x[1] - x[0])+(x[2] - x[1]))
    matriz[0][1] = (x[2] - x[1])
    matriz[0][len(matriz[0])-1] = 6* (((y[2]-y[1])/(x[2]-x[1]))-((y[1] - y[0])/(x[1] - x[0])))
    
    for i in range(1,n-3):
        matriz[i][i-1] = (x[i+1] - x[i])
        matriz[i][i] = 2*((x[i+1] - x[i])+(x[i+2] - x[i+1]))
        matriz[i][i+1] = (x[i+2] - x[i+1])
        matriz[i][len(matriz[i])-1] = 6* (((y[i+2]-y[i+1])/(x[i+2]-x[i+1]))-((y[i+1] - y[i])/(x[i+1] - x[i]))) 
        
    matriz[n-3][n-4] = (x[n-2] - x[n-3])
    matriz[n-3][n-3] = 2*((x[n-2] - x[n-3])+(x[n-1] - x[n-2]))
    matriz[n-3][len(matriz[n-3])-1] = 6* (((y[n-1]-y[n-2])/(x[n-1]-x[n-2]))-((y[n-2] - y[n-3])/(x[n-2] - x[n-3]))) 
    
    temp = GaussMod(matriz)
    
    for i in range(1,n-1):
        a[i] = temp[i-1]
    
    for j in range(0,len(t)):
        for i in range(0,n-1):
            if t[j]<=x[i+1] and t[j]>=x[i]:
                return f(a,x,y,i,t)
    

#Variaveis
f_c = 2e9 # Frequência do sistema é de 2 GHz
v = 3/3.6 # Velocidade do móvel de 3 km/h (pedestre)
L = 20    # O canal possui 20 multi-percursos
t = np.arange(0,121,20.)

g = Jakes(t, f_c, v, L)

tpol = np.arange(0,121,1.)

plt.figure(1)
plt.plot(t, g, 'ro', label = ' g($t$) ')
plt.plot(tpol, splines(t,g,tpol), 'b-', label = 'Splines' )
plt.legend()
plt.grid()
plt.xlabel('$t$ (em ms)')
plt.title('Gráfico da Interpolação Splines')
plt.show()
        