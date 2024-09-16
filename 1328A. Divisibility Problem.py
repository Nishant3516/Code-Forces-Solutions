n = int(input())

for _ in range(n):
    a, b = list(map(int, input().split()))
    if a % b == 0:
        print(0)
    else:
        quot = a//b
        print((quot+1)*b - a)
