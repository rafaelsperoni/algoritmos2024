"""
Faça um algoritmo que lê 5 valores
 para uma variável do tipo vetor
 e determine a média de todos os
 valores armazenados no vetor.
"""
import numpy as np
N = 5
x = np.zeros(N)
#leitura dos valores
for i in range(N):
    x[i] = float(input(f"Informe valor {i}: "))

soma = 0
for i in range (N):
    soma = soma + x[i]

media = soma / N
print(f"A media de x é {media}")

#print(f"A soma de x é {x.mean()}")