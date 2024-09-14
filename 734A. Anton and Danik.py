n=int(input())
inp=input()
if inp.count("A")>inp.count("D"):
    print("Anton")
elif inp.count("A")<inp.count("D"):
    print("Danik")
else:
    print("Friendship")