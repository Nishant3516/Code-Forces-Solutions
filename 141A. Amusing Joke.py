def getCount(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0)+1
    return d


guest = input()
residence = input()
letter = input()
a = getCount(residence+guest)
b = getCount(letter)
print("YES" if a == b else "NO")
