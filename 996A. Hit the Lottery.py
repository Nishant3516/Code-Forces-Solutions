n = int(input())

bills = 0

d = {100: 0, 20: 0, 10: 0, 5: 0, 1: 0}

for i in d:
    bills += n//i
    n = n % i
print(bills)
