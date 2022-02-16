N = int(input())
swift = input().split()
Swf, Smp, K = [], [], [0]
day_swf, day_smp = 0, 0
for i in swift:
    Swf.append(int(i))
semaphores = input().split()
for i in semaphores:
    Smp.append(int(i))
for i in range(N):
    day_swf += Swf[i]
    day_smp += Smp[i]
    if day_swf == day_smp:
        K.append(i+1)
print(max(K))
# 15/15
# END
