n=int(input())
track=[]
for _ in range(n):
    track.extend(list(map(int,input().split())))

maxCapacity=0
currentCapacity=0
for i in range(1,len(track)):
    if i&1==1:
        currentCapacity+=track[i]
    else:
        currentCapacity-=track[i]
    maxCapacity=max(maxCapacity,currentCapacity)
print(maxCapacity)