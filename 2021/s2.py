M = int(input())
N = int(input())
K = int(input())
C, R = [], []
for i in range(K):
    choice = input()
    if "C" in choice:
        if choice[2:] in C:
            C.remove(choice[2:])
        else:
            C.append(choice[2:])
    else:
        if choice[2:] in R:
            R.remove(choice[2:])
        else:
            R.append(choice[2:])
cell = (M*len(C) + N*len(R)) - 2 * len(C) * (len(R))
print(cell)
# 10/15
# END
