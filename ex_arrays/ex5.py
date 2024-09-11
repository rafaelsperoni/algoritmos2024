"""
Faça um algoritmo que lê 5 valores
 para uma variável do tipo vetor e
 determine a posicao do maior e 
 e a posicao do menor valor
 armazenado no vetor.
"""

import numpy as np
N = 5
x = np.zeros(N)
#leitura dos valores
for i in range(N):
    x[i] = float(input(f"Informe valor {i}: "))

for i in range(N):
    if i == 0:
        maior = x[i]
        posMaior = i
        menor = x[i]
        posMenor = i
    else:
        if x[i] > maior:
            maior = x[i]
            posMaior = i
        if x[i] < menor:
            menor = x[i]
            posMenor = i

print(f"A posicao do maior valor: {posMaior}")
print(f"O posicao do menor valor: {posMenor}")
#faz o mesmo, usando as funções da biblioteca
print(f"O maior valor: {x.argmax()}")
print(f"O menor valor: {x.argmin()}")