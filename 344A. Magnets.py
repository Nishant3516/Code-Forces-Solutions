n = int(input())
values = []
for i in range(n):
    values.append(list(map(int, input().split())))

groups = 1
for i in range(n-1):
    if values[i][0] != values[i+1][0]:
        groups += 1
print(groups)
