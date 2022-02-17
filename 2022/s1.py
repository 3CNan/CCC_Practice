num = int(input())
count = 0
start = False
if num % 2 == 1 and num != 5:
    num -= 5
while num > 0:
    if start is True:
        num -= 5
    res = num % 4
    if res == 0 and num >= 0:
        count += 1
    start = True
print(count)
# 15/15
# END
