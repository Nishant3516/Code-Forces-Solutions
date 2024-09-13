def getResult(a,b):
    a=a.lower()
    b=b.lower()
    if a<b:
        return -1
    elif a>b:
        return 1
    else:
        return 0


a=input()
b=input()
print(getResult(a,b))