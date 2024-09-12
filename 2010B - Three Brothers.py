def brothers(values):
    for i in range(1, 4):
        if i not in values:
            return i


arrived = list(map(int, input().split()))
print(brothers(arrived))
