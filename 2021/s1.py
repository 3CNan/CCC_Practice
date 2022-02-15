N = int(input())
H = input().split()
W = input().split()
area = 0
for i in range(N):
    area += (int(H[i]) + int(H[i+1])) * int(W[i]) / 2
print(area)
# 15/15
# END
