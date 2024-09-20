k, r = list(map(int, input().split()))
count = 0
while True:
    count += 1
    if (k*count) % 10 == 0 or (k*count) % 10 == r:
        break
print(count)
