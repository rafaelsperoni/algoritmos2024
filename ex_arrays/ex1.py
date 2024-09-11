"""
Faça um algoritmo que lê 10 valores para
uma variável do tipo vetor de nome x e 
mostra os 10 valores armazenados na estrutura.
"""
import numpy as np
N = 10
x = np.zeros(N)
#leitura dos valores
for i in range(N):
    x[i] = float(input(f"Informe valor {i}: "))

#exibição dos valores
for i in range(N):
    print(f"O valor na posicao {i} é {x[i]}")
