n = int(input())
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    if max(a, b, c) == c:
        print("+")
    else:
        print("-")
