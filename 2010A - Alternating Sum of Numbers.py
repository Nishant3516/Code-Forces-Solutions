def alternateSum(values):
    sumV=0
    for index, value in enumerate(values):
        if index&1==0:
            sumV+=value
        else:
            sumV-=value
    return sumV

N=int(input())
for i in range(N):
    length=int(input())
    case=list(map(int,input().split()))
    print(alternateSum(case))