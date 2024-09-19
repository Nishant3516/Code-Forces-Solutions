values = list(map(int, input().split()))
values.sort()
print(values[-1]-values[0])
