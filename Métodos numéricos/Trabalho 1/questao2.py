# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:19:33 2016

@author: Caio Cid Santiago
"""

def NumToIEEE754(num,tipo):
    
    if tipo != 32 and tipo != 64:
        return 'Tipo invalido!'
        
    #Verificando se é positivo ou negativo
    if num>=0:
        numlocal = num
        sinal = '0'
    else:
        numlocal = -num
        sinal = '1'
    
    #Descobrindo o exponte e a mantissa     
    exp = 0
    if numlocal>=2:            
        while numlocal>=2:
            numlocal = numlocal/2
            exp = exp + 1
        mantissadec = numlocal - 1
    elif numlocal<2 and numlocal>=1:
        mantissadec = numlocal - 1
    else:
        while numlocal<1:
            numlocal = numlocal*2
            exp = exp - 1
        mantissadec = numlocal - 1
        
    #Convertendo a mantissa para binário
    mantissabit = ''
    if mantissadec == 0:
        mantissabit = '0'
    else:
        if tipo == 32:
            while mantissadec!=1 and len(mantissabit)<23 :
                mantissadec = mantissadec * 2
                if mantissadec>=1:
                    mantissabit = mantissabit+'1'
                    mantissadec = mantissadec-1
                else:
                    mantissabit = mantissabit+'0'
        else:
            while mantissadec!=1 and len(mantissabit)<52 :
                mantissadec = mantissadec * 2
                if mantissadec>=1:
                    mantissabit = mantissabit+'1'
                    mantissadec = mantissadec-1
                else:
                    mantissabit = mantissabit+'0'

    #Convertendo o expoente pra binario e concatenando o resultado
    if tipo == 32:
        expbin = bin(exp+127).replace('0b','')
        ieee754 = sinal+str(expbin).rjust(8,'0')+str(mantissabit).ljust(23,'0')
        return ieee754
    else:
        expbin = bin(exp+1023).replace('0b','')
        ieee754 = sinal+str(expbin).rjust(11,'0')+str(mantissabit).ljust(52,'0')
        return ieee754

a = NumToIEEE754 (-1,32)
b = NumToIEEE754 (-1,64)
c = NumToIEEE754 (-354.46512,32)
d = NumToIEEE754 (-354.46512,64)
e = NumToIEEE754 (256.175,32)
f = NumToIEEE754 (256.175,64)
g = NumToIEEE754 (1.45135,64)
h = NumToIEEE754 (1.45,32)
i = NumToIEEE754 (1, 50)

print ('Numero -1, 32 bits: \n'+a)
print ('Numero -1, 64 bits: \n'+b)
print ('Numero -354.46512, 32 bits: \n'+c)
print ('Numero -354.46512, 64 bits: \n'+d)
print ('Numero 256.175, 32 bits: \n'+e)
print ('Numero 256.175, 64 bits: \n'+f)
print ('Numero 1.45135, 64 bits: \n'+g)
print ('Numero 1.45, 32 bits: \n'+h)
print ('Caso de teste para segundo argumento diferente de 32 ou 64:\n'+i)