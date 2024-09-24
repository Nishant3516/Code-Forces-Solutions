t = int(input())
for _ in range(t):
    values = list(map(int, input().split()))
    values.sort()

    if sum(values[1:]) >= 10:
        print("YES")
    else:
        print("NO")
