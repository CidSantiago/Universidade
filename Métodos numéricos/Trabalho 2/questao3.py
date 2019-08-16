# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:16:07 2016

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

def interpNewton(x,y,t):
    
    N = len(x)
    a = np.zeros(N)
    f = np.zeros((N,N))
    
    for i in range (0,N):
        f[0][i] = y[i]
    
    for i in range(0,N-1):
            f[1][i] = (y[i+1] - y[i])/(x[i+1] - x[i])  
            
    for i in range(2,N):
        for j in range(0,N-i):
                f[i][j] = (f[i-1][j+1] - f[i-1][j]) / (x[i+j] - x[j])
    
    for i in range(0,N):
        a[i] = f[i][0]
      
    Yint = a[0]
    xn = 1
    for i in range(1,N):
        xn = xn*(t - x[i-1])
        Yint = Yint + a[i]*xn

    return Yint

#Variaveis
f_c = 2e9 # Frequência do sistema é de 2 GHz
v = 3/3.6 # Velocidade do móvel de 3 km/h (pedestre)
L = 20    # O canal possui 20 multi-percursos
t = np.arange(0,121,20)

g = Jakes(t, f_c, v, L)

tpol = np.arange(0,121,1.)

plt.figure(1)
plt.plot(t, g, 'ro', label = ' g($t$) ')
plt.plot(tpol, interpNewton(t,g,tpol), 'b-', label = 'Polinomio de Newton' )
plt.legend()
plt.grid()
plt.xlabel('$t$ (em ms)')
plt.title('Gráfico da Interpolação Polinomial de Newton')
plt.show()