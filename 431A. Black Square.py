a1, a2, a3, a4 = list(map(int, input().split()))
s = input()

d = {1: a1, 2: a2, 3: a3, 4: a4}

sumV = 0
for i in s:
    sumV += d[int(i)]
print(sumV)
