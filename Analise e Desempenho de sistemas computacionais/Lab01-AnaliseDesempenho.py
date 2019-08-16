"""
Lab01 - Analise e desempenho de redes e sistemas computacionais

Aluno: Caio Cid Santiago Barbosa    Mat: 378596
"""


#Questao1
#item a
from numpy import random    #Importada a biblioteca Random da NumPy
random.seed(1013)    #Definida uma seed para deixar os resultados do rand iguais, independente de quando e onde seja executado
n = random.randint(100,high=501) #Executada a função randint de acordo com os seus parâmentros

print("\n",n) #Exibindo o valor achado de n (300).

#item b
vetor = 23 * random.randint(1,high=501,size=n) #Vetor gerado multiplicando pela idade(23) pelo vetor de numeros aleatorios [1,501)

#item c
print("\n",vetor)

#Questão 2
#Item a
import numpy as np

print("\nQuantidade de Elementos = ",len(vetor))
print("\nMédia = ",np.mean(vetor))
print("\nMediana = ",np.median(vetor))
print("\nVariancia = ",np.var(vetor))

#Item b
from matplotlib import pyplot as plt #Importanto a biblioteca de plots, baseada no matlab
plt.hist(vetor) #função para plotar histograma
plt.show() #mostrar plot

#Item C
#
#Dado nosso vetor, como a média e a mediana possuem valores próximos, qualquer 
#uma das duas, ou até as duas, poderiam ser usadas. Nos dados do item a, o valor
#que mais chama atenção é a alta variância, que indicia que os dados estão bem 
#espalhados entre si. Essa informação é evidenciada pelo histograma, que mostra 
#uma distribuição bastante irregular e dispersa