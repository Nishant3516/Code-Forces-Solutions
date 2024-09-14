n=int(input())
count=0
while n>0:
    last=n%10
    if last == 4 or last==7:
        count+=1
    n//=10

print("YES" if count==4 or count==7 else "NO")