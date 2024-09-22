n = int(input())
for _ in range(n):
    val = int(input())
    if val <= 1399:
        print("Division 4")
    elif val <= 1599:
        print("Division 3")
    elif val <= 1899:
        print("Division 2")
    else:
        print("Division 1")
