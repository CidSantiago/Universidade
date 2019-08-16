# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 12:36:35 2017

@author: Cid Santiago
"""

import threading, numpy, multiprocessing

## Matrizes de teste

M1 = [[1,2,3],[4,5,6],[7,8,9],[11,23,7]]
M2 = [[10,19,18,7],[17,16,15,7],[14,13,12,7]]

#M1 = [[0, 7, 9],[7,5,3],[2,1,2],[2,4,2]]
#M2 = [[4,6,8],[3,5,5],[1,3,5]]

#M1 = [[3,5,7]]
#M2 = [[0,7],[9,3],[0,1]]

#Inicializando a Matriz resultado (MR), o contador global de threads 
#ativas(active), o numero máximo de threads permitidas(maxRunning), a variável
#de trava para evitar condição de corrida(Lock) e uma lista de threads(threads) 
MR = numpy.zeros((len(M1),len(M2[0])))
active = 0
maxRunning = 2*multiprocessing.cpu_count()
lock = threading.Lock()
threads = []

#Função que será utilizada na thread.
def element (linha, coluna):
    global active
    with lock:
        active += 1
    for i in range(len(M1[0])):
        MR[linha][coluna] += M1[linha][i]*M2[i][coluna]
    with lock:
        active -= 1
  
for i in range(len(M1)):
    for j in range(len(M2[0])):
        while True:
#       Esse laço seria utilizado para apagar as threads inativas na lista de
#       threads. Como foi enfatizada a utilização das apenas das primitivas 
#       ensinadas em sala, o codigo foi comentado apenas para consulta.
#            if len(threads)>0:
#                if threads[len(threads)-1].is_alive()== False:
#                    del threads[len(threads)-1]
           
#           Laço com verificação da quantidade de threads ativas rodando no
#           momento. Se a condição não for satisfeita, ele continuará rodando
#           dentro do while até conseguir entrar nesse laço
            if (active<maxRunning):
                threads.append(threading.Thread(target = element, args = (i,j)))
                threads[len(threads)-1].start()
                break

threads[0].join()
print(MR)
        