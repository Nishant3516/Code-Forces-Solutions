def getIndexMax(values, operations):
    res=[]
    for op in operations:
        sign=op[0]
        op[1]=int(op[1])
        op[2]=int(op[2])
        if sign=='+':
            for i in range(len(values)):
                if op[1]<=values[i] and values[i]<=op[2]:
                    values[i]+=1
        else:
            for i in range(len(values)):
                if op[1]<=values[i] and values[i]<=op[2]:
                    values[i]-=1
        res.append(max(values))
    return res


N=int(input())
for _ in range(N):
    n, m =list(map(int, input().split()))
    values =list(map(int, input().split()))
    operations=[]
    # res=[]
    for i in range(m):
        operations.append(list(map(str, input().split())))
    res=getIndexMax(values, operations)
    for i in res:
        print(i, end=' ')
