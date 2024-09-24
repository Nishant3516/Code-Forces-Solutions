t = int(input())
for _ in range(t):
    s = input()
    if s[:2] == "bc" or s[:2] == "ca":
        print("NO")
    else:
        print("YES")
