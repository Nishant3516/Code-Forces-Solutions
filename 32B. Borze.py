x = input()

res = ""
d = {".": '0', "-.": '1', "--": '2'}

temp = ""

for i in x:
    if temp in d.keys():
        res += d[temp]
        temp = i
    else:
        temp += i
if temp:
    res += d[temp]
print(res)
