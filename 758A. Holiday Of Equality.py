n = int(input())
values = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    maxV = max(values)
    sumV = 0
    for i in values:
        sumV += maxV-i
    print(sumV)
