n = int(input())

values = list(map(int, input().split()))
sereja = []
dima = []

temp = values
count = 1
left = 0
right = len(values)-1
while left <= right:
    if values[left] < values[right]:
        if count & 1 == 1:
            sereja.append(values[right])
        else:
            dima.append(values[right])
        right -= 1
    else:
        if count & 1 == 1:
            sereja.append(values[left])
        else:
            dima.append(values[left])
        left += 1

    count += 1

print(sum(sereja), sum(dima))
