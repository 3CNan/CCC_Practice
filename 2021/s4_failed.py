N, W, D = input().split()
AB, S, XY = [], [], []
for i in range(int(W)):
    A, B = input().split()
    AB.append([int(A), int(B)])
s = list(input().split())
for i in s:
    S.append(int(i))
for i in range(int(D)):
    X, Y = input().split()
    XY.append([int(X), int(Y)])
for i in range(int(D)):
    S[XY[i][0] - 1], S[XY[i][1] - 1] = S[XY[i][1] - 1], S[XY[i][0] - 1]
    sub_dis = S.index(max(S)) - S.index(min(S))
    road = S[S.index(min(S)):S.index(max(S)) + 1]
    for walkway in AB:
        if road.count(walkway[1]) != 0 and road.count(walkway[0]) != 0:
            if road.index(walkway[1]) - road.index(walkway[0]) > 1:
                road = road[:road.index(walkway[0])+1] + road[road.index(walkway[1]):]
    print(len(road) - 1)
# END
