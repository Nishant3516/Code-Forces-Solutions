def minimize(values):
    minV=2**31-1
    a=values[0]
    b=values[1]
    for c in range(a, b+1):
        diff=(c-a)+(b-c)
        if diff<minV:
            minV=diff
    return minV
            

N=int(input())
for _ in range(N):
    case=list(map(int,input().split()))
    print(minimize(case))