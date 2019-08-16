# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:25:38 2017

@author: cidsa
"""

import threading, time, random

##Exercicio 1
#def print_n_times(value, n, delay):
#    for i in range(n):
#        print(value)
#        time.sleep(delay)
#
#t1 = threading.Thread(target = print_n_times, args = ("T1",4,1))
#t2 = threading.Thread(target = print_n_times, args = ("T2",3,2))
#
#t1.start()
#t2.start()
#
#t1.join()
#t2.join()
#
#print_n_times("oi",3,1)

##Exercicio 2
#array1 = [5, 7, 4, 3, 9, 6, 2, 1, 8]
#array2 = [3, 2, 6, 8, 1, 5, 9, 4, 7]
#shared = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#
#def soma(a,b,shared,i):
#    shared[i] = a + b
#
#for i in range(len(array1)):
#    t1 = threading.Thread(target = soma, args = (array1[i],array2[i],shared,i))    
#
#    t1.start()
#    t1.join()

#Exercicio 3

values = [10,15]

lock = threading.Lock()

def increase(value, i):
    with lock:
        temp = values[i]
        time.sleep(random.random())
        values[i] = temp + value
        
def decrease(value, i):
    with lock:
        temp = values[i]
        time.sleep(random.random())
        values[i] = temp - value
        
t1 = threading.Thread(target = increase, args = (5,0))
t2 = threading.Thread(target = increase, args = (7,1))
t3 = threading.Thread(target = decrease, args = (3,0))
t4 = threading.Thread(target = decrease, args = (8,1))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(values)