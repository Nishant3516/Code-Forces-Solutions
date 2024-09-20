x1, x2, x3, x4 = list(map(int, input().split()))

x = [x1, x2, x3, x4]
x.sort()
a = x[3] - x[0]
b = x[3] - x[1]
c = x[3] - x[2]
print(a, b, c)
