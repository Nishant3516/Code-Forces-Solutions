n = int(input())

data = input().split()

ans = [0] * n

for i in range(n):
    p = int(data[i])
    ans[p - 1] = i+1

print(" ".join(map(str, ans)))
