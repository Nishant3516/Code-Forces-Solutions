N=int(input())
inp=input()
count=0
for i in range(1,N):
    if inp[i]==inp[i-1]:
        count+=1
print(count)