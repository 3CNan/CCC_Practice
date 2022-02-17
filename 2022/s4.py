import itertools
N, C = input().split()
points = list(map(int, input().split()))
ans = []
for comb in itertools.combinations(points, 3):
    if comb[0] != comb[1] and comb[1] != comb[2] and comb[0] != comb[2]:
        comb = list(comb)
        comb.sort()
        if abs(comb[0] - comb[1]) >= int(C) / 2 or int(C) - abs(comb[0] - comb[2]) >= int(C) / 2 or abs(comb[1] - comb[2]) >= int(C) / 2:
            pass
        else:
            ans.append(comb)
print(len(ans))
# 3/15
# END
