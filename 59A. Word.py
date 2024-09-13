inp=input()
lowerCount, upperCount=0,0
for i in inp:
    if i.islower():
        lowerCount+=1
    else:
        upperCount+=1

if lowerCount>=upperCount:
    print(inp.lower())
else:
    print(inp.upper())