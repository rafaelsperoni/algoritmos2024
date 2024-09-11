"""
Faça um algoritmo que lê 5 valores para
 uma variável do tipo vetor e determine 
o somatório de todos os valores armazenados no vetor.
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

print(f"A soma de x é {soma}")
#print(f"A soma de x é {x.sum()}")