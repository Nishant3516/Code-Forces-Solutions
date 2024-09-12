def bitOperation(operations):
    x=0
    for i in operations:
        if i[0]=='+' or i[-1]=='+':
            x+=1
        else:
            x-=1
    return x

N = int(input())
operations=[]
for _ in range(N):
    operations.append(input())
print(bitOperation(operations))
