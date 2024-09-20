n = int(input())
values = list(map(int, input().split()))

count = 0

max = values[0]
min = values[0]
for i in range(n):
    if values[i] > max:
        max = values[i]
        count += 1
    if values[i] < min:
        min = values[i]
        count += 1
print(count)
