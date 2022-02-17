from collections import Counter
N = int(input())
friends, final = [], []
for i in range(N - 1):
    friends.append(list(map(int, input().split())))
friends.sort()
P = input()
No = [i+1 for i in range(len(P)) if P[i] == "N"]
print(P, No)
C = list(map(int, input().split()))
pre_p, person_dict, temp_list = -1, {}, []
for i in range(1, N):
    for f in friends:
        if i in f:
            person_dict[i] = [j for f in friends if i in f for j in f if j != i]
a = [j for i in No for j in range(1, N) if i in person_dict[j]]
while bool(No) is not False:
    most = Counter(a).most_common(1)
    print(most)
    for i in person_dict[most[0][0]]:
        if i in No:
            No.remove(i)
    final.append(most[0][0])
    a = [num for num in a if num != most[0][0]]
total = 0
for i in final:
    total += C[i-1]
print(total)
# Just a try, cannot work at all. Q∆Q
# END
