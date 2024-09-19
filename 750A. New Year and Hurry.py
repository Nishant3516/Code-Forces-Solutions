n, k = list(map(int, input().split()))

timeLeft = 240-k

count = 1
while timeLeft//(5*count) != 0:
    timeLeft -= 5*count
    count += 1
    if count > n:
        break
print(count-1)
