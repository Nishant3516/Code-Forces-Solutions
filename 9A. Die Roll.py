y, w = list(map(int, input().split()))

d = max(y, w)

probability = ["", "1/1", "5/6", "2/3", "1/2", "1/3", "1/6"]
print(probability[d])
