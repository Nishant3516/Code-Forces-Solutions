n = int(input())
for _ in range(n):
    x = int(input())
    values = list(map(int, input().split()))
    print(list(values.index(i)+1 for i in values if values.count(i) == 1)[0])
