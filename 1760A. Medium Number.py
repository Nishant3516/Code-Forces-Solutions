n = int(input())
for _ in range(n):
    values = list(map(int, input().split()))

    print(sorted(values)[1])
