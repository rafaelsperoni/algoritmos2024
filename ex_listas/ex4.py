L1 = []
L2 = []
R = []
N = 5
for i in range(N):
    L1.append(int(input(f"valor {i} de L1:")))

for i in range(N):
    L2.append(int(input(f"valor {i} de L2:")))

for i in range(N):
    R.append(L1[i]*L2[N-1-i])


print(R)