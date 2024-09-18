import math
n = int(input())
for _ in range(n):
    candies = int(input())
    if candies < 3:
        print(0)
    else:
        print(math.ceil(candies / 2) - 1)
