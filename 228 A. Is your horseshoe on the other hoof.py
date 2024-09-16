values = list(map(int, input().split()))

d = {i: values.count(i) for i in values}
count = 0
for i in d.values():
    if i > 1:
        count += i-1
if count == 0:
    print(0)
else:
    print(count)
