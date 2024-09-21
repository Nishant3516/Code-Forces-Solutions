n = int(input())
for _ in range(n):
    x = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, len(a)):
        if a[i]-a[i-1] > 1:
            print("NO")
            break
    else:
        print("YES")
