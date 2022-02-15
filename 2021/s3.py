N = int(input())
friends = []
all_times = []
for i in range(N):
    P, W, D = input().split()
    friends.append([int(P), int(W), int(D)])
friends.sort()
for i in range(friends[0][0], friends[-1][0]):
    time = 0
    for friend in friends:
        if abs(friend[0] - i) > friend[2]:
            time += (abs(friend[0] - i) - friend[2]) * friend[1]
    all_times.append(time)
if bool(all_times) is False:
    print(0)
else:
    print(min(all_times))
# 4/15
# END
