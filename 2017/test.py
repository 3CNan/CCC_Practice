N = int(input())
Ls = input().split()
total_height, final_length, final_height = 0, 1, 1
if N % 2 == 0:
    L = []
    for i in Ls:
        L.append(int(i))
        total_height += int(i)
    L.sort()
    low = L[:int(len(L) / 2)]
    high = L[int(len(L) / 2):]
    print(low, high)
    pos_height = int(total_height / N * 2)
    for i in low:
        for j in high:
            if i + j == pos_height:
                final_length = int(len(L) / 2)
                break
            else:
                final_height = N * (N - 1) / 2
if N % 2 != 0:
    final_height = N * (N-1) / 2
print(final_length, int(final_height))
# 8
# 20 30 40 10 30 20 15 35
# 6
# 1 10 100 1000 2000 3000
# END
