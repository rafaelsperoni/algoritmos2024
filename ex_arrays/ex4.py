"""
Faça um algoritmo que lê 5 valores
 para uma variável do tipo vetor e
 determine o maior e o menor valor
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
        menor = x[i]
    else:
        if x[i] > maior:
            maior = x[i]
        if x[i] < menor:
            menor = x[i]

print(f"O maior valor: {maior}")
print(f"O menor valor: {menor}")
#print(f"O maior valor: {x.max()}")
#print(f"O menor valor: {x.min()}")