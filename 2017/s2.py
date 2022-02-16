N = int(input())
measurements = input().split()
data = []
for i in measurements:
    data.append(int(i))
data.sort()
if N % 2 == 0:
    low = data[:int(N / 2)]
    high = data[int(N / 2):]
else:
    low = data[:int(N / 2) + 1]
    high = data[int(N / 2) + 1:]
low.reverse()
order = ""
for i in range(len(high)):
    order += str(low[i]) + " " + str(high[i]) + " "
if N % 2 == 1:
    order += str(low[-1])
print(order.strip())
# 15/15
# END
