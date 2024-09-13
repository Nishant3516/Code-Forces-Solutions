n=int(input())
count=0
while n>0:
    if n>=5:
        count+=n//5
        n%=5
    elif n>=4:
        count+=n//4
        n%=4
    elif n>=3:
        count+=n//3
        n%=3
    elif n>=2:
        count+=n//2
        n%=2
    else:
        count+=n//1
        n%=1
print(count)