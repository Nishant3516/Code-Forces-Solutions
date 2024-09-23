n = int(input())
for _ in range(n):
    s = input()
    length = len(s)
    if length == 2:
        print(s)
    else:
        res = ""
        for i in range(0, length, 2):
            # print(i)
            res += s[i]
        res += s[-1]
        print(res)
