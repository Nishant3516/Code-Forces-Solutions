n=int(input())
while True:
    n+=1
    if len(set(str(n)))==4:
        break
print(n)