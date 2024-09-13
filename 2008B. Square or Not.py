def isBinaryMatrix(n,inp):
    if n == 0:
        return 'No'
    sqrt = int(n ** 0.5)
    if sqrt * sqrt != n:
        return 'No'
    expected = ""
    for j in range(sqrt):
        for i in range(sqrt):
            if i == 0 or i == sqrt - 1 or j == 0 or j == sqrt - 1:
                expected+='1'
            else:
                expected+='0'
    
    return "Yes" if expected==inp else "No"
        
        


N=int(input())
for _ in range(N):
    n=int(input())
    inp=input()
    print(isBinaryMatrix(n,inp))