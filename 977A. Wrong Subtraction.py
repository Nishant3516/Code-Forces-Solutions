n,k = map(int, input().split())
while k>0:
    last=n%10
    if last>0:
        n-=1
    else:
        n//=10
    k-=1
print(n)