n = int(input())
for _ in range(n):
    k = int(input())
    res = 1
    i = 1
    while k:
        if i % 3 == 0 or i % 10 == 3:
            i += 1
            continue
        res = i
        k -= 1
        i += 1
    print(res)
