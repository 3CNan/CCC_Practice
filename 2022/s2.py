X = int(input())
Same, Sepa, Place = [], [], []
count = 0
for i in range(X):
    Same.append(list(input().split()))
Y = int(input())
for i in range(Y):
    Sepa.append(list(input().split()))
G = int(input())
for i in range(G):
    Place.append(list(input().split()))
for i in Same:
    for j in Place:
        if (i[0] not in j and i[1] in j) or (i[0] in j and i[1] not in j):
            count += 1
            break
for i in Sepa:
    for j in Place:
        if i[0] in j and i[1] in j:
            count += 1
            break
print(count)
# 8/15
# END
