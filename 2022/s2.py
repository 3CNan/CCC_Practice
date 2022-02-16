X = int(input())
Same, Sepa, Place = [], [], []
count = 0
for i in range(X):
    p1, p2 = input().split()
    Same.append([p1, p2])
Y = int(input())
for i in range(Y):
    p1, p2 = input().split()
    Sepa.append([p1, p2])
G = int(input())
for i in range(G):
    p1, p2, p3 = input().split()
    Place.append([p1, p2, p3])
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
# END
