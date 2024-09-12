def division(value):
    if value<=3:
        return "NO"
    
    if value%2!=0:
        return "NO"
    
    return "YES" if value%2==0 and value!=2 else "NO"
            

N=int(input())
print(division(N))