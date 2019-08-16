# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:23:26 2016

@author: Caio Cid Santiago
"""
import struct

def NumToIEEE754 (num,tipo):

    if tipo == 32:
        
        # Transformar o numero nos pacotes de bytes alocados na memoria
        packed = struct.pack('!f', num)
    
        # Converte os Unicodes em binarios
        bbins = [bin(i) for i in packed]
    
        # Retirar os '0b' que aparecem nos valores após a conversão em binario
        bins = [s.replace('0b', '') for s in bbins]

        # Preenche os binarios com 0 para completarem os 8 bits:
        fullbins = [s.rjust(8, '0') for s in bins]
   
        # Nesse laço, verificamos se o numero é positivo ou negativo para acrescentarmos o bit de sinal
        if num >= 0:
            return ''.join(fullbins)
        else:
            fullbins[0].replace('0','1')
            return ''.join(fullbins)
 
    elif tipo == 64:
       
        # Transformar o numero nos pacotes de bytes alocados na memoria
        packed = struct.pack('!d', num)
    
        # Converte os Unicodes em binarios
        bbins = [bin(i) for i in packed]
    
        # Retirar os '0b' que aparecem nos valores após a conversão em binario
        bins = [s.replace('0b', '') for s in bbins]

        # Preenche os binarios com 0 para completarem os 8 bits:
        fullbins = [s.rjust(8, '0') for s in bins]
   
        # Nesse laço, verificamos se o numero é positivo ou negativo para acrescentarmos o bit de sinal
        if num >= 0:
            return ''.join(fullbins)
        else:
            fullbins[0].replace('0','1')
            return ''.join(fullbins)
    
    else:
        return 'Erro! Quantidade de bits não identificada!'
        
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
