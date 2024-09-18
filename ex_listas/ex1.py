"""
Faça um algoritmo que lê 10 valores para uma variável do 
tipo lista de nome x e mostre os 10 valores armazenados.
"""
#primeira abordagem
#L = [0,0,0,0,0,0,0,0,0,0]
#for i in range(10):
#    L[i] = int(input(f"Informe valor {i}:"))

#segunda abordagem
L = []   #cria lista vazia
for i in range(5):
    n = int(input(f"Informe num {i}:"))
    L.append(n)
#apresentacao - 1
#for i in range(10):
#    print(L[i])
#apresentacao - 2
for elem in L:
    print(elem)