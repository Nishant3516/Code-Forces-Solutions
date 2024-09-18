n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if list(set(a[1:]+b[1:])) == list(range(1, n+1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
