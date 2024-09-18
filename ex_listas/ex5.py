L1 = []
L2 = []
R = []
N = 5
for i in range(N):
    L1.append(int(input(f"valor {i} de L1:")))

for i in range(N):
    L2.append(int(input(f"valor {i} de L2:")))
#primeira abordagem
for i in range(N):
    R.append(L1[i])
for i in range(N):
    R.append(L2[i])
#segunda abordagem 
for elem in L1:
    R.append(elem)
for elem in L2:
    R.append(elem)


print(R)