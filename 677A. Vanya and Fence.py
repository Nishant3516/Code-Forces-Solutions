n, h=list(map(int,input().split()))
values=list(map(int,input().split()))

width=0
for i in values:
    if i>h:
        width+=2
    else:
        width+=1
print(width)