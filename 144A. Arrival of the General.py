n = int(input())
values = list(map(int, input().split()))

maxValue = -float('inf')
minValue = float('inf')
maxIndex = 0
minIndex = 0

for i in range(n):
    x = values[i]
    if x > maxValue:
        maxValue = x
        maxIndex = i
    if x <= minValue:
        minValue = x
        minIndex = i

if maxIndex > minIndex:
    print(maxIndex-1 + n-minIndex-1)
else:
    print(maxIndex-1 + n-minIndex)
