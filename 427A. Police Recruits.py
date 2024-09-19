n = int(input())
values = list(map(int, input().split()))
maxMin = 0
curr = 0
for i in values:
    if i == -1:
        if curr == 0:
            maxMin -= 1
        else:
            curr -= 1
    else:
        curr += i
print(abs(maxMin))
