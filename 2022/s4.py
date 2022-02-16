import itertools
N, C = input().split()
points = list(map(int, input().split()))
triplets, ans = [], []
for comb in itertools.combinations(points, 3):
    if comb[0] != comb[1] and comb[1] != comb[2] and comb[0] != comb[2]:
        comb = list(comb)
        comb.sort()
        dis1 = abs(comb[0] - comb[1])
        dis2 = int(C) - abs(comb[0] - comb[2])
        dis3 = abs(comb[1] - comb[2])
        if dis1 + dis2 > dis3 and dis1 + dis3 > dis2 and dis2 + dis3 > dis1:
            ans.append(comb)
print(len(ans))
# END
