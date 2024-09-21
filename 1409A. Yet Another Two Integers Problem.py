n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    if a == b:
        print(0)
    else:
        res = abs(b - a) // 10
        print(res + (1 if abs(b - a) % 10 != 0 else 0))
