n = input()
if n == '{}':
    print(0)
else:
    l = n[1:-1].split(", ")
    print(len(set(l)))
