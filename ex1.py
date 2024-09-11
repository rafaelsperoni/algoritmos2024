import numpy as np

N = 5

vetor = np.zeros(N)

for i in range(N):
    vetor[i] = float(input(f"Informe o valor para a posição {i}: "))

for i in range(N):
    print(f"Posição {i} vale: ", vetor[i])