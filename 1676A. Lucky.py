n = int(input())
for _ in range(n):
    val = input()
    print("YES" if sum(list(map(int, val[:3]))) == sum(
        list(map(int, val[3:]))) else "NO")
