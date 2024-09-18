L1 = []
L2 = []
R = []
for i in range(5):
    L1.append(int(input(f"valor {i} de L1:")))

for i in range(5):
    L2.append(int(input(f"valor {i} de L2:")))

for i in range(5):
    R.append(L1[i]+L2[i])

print(R)