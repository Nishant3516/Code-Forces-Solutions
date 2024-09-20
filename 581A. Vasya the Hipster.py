r, b = list(map(int, input().split()))

count = 0
while r > 0 and b > 0:
    r -= 1
    b -= 1
    count += 1
print(count, r//2 + b//2)
