def osumania(values):
    res=[i.index("#")+1 for i in values]
    return res[::-1]
            

N=int(input())
for _ in range(N):
    length=int(input())
    cases=[]
    for _ in range(length):
        cases.append(input())
    res=osumania(cases)
    for i in res:
        print(i,end=" ")