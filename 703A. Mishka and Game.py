t = int(input())
values = []
m, c, draw = 0, 0, 0
for _ in range(t):
    values.append(list(map(int, input().split())))

for value in values:
    a = value[0]
    b = value[1]
    if a > b:
        m += 1
    elif b > a:
        c += 1
    else:
        draw += 1

if m == c or draw == t:
    print("Friendship is magic!^^")
elif m > c:
    print("Mishka")
else:
    print("Chris")
