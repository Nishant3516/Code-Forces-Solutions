n = int(input())

if n == 1:
    print("I hate it", end="")
else:
    print("I hate that", end="")

for i in range(2, n):
    if i % 2 == 1:
        print(" I hate that", end="")
    else:
        print(" I love that", end="")

if n % 2 == 0 and n > 1:
    print(" I love it", end="")
elif n > 1:
    print(" I hate it", end="")
