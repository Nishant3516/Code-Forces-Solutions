n = int(input())
for _ in range(n):
    values = list(map(int, input().split()))
    count = 0
    for i in range(1, 4):
        if values[i] > values[0]:
            count += 1
    print(count)
