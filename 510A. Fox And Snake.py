a, b = list(map(int, input().split()))

temp = 0
for i in range(a):
    if i & 1 == 0:
        print("#"*b)
    else:
        if temp == 0:
            print("."*(b-1)+"#")
            temp = 1
        else:
            print("#"+"."*(b-1))
            temp = 0
