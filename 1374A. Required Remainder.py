t = int(input())
for _ in range(t):
    x, y, n = list(map(int, input().split()))
    extra = (n-y) % x
    print((n-extra))
