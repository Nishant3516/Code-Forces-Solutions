n = int(input())
pents = []
for _ in range(n):
    pents.append(input())

total = 0

for pent in pents:
    if pent == "Tetrahedron":
        total += 4
    elif pent == "Cube":
        total += 6
    elif pent == "Octahedron":
        total += 8
    elif pent == "Dodecahedron":
        total += 12
    elif pent == "Icosahedron":
        total += 20
print(total)
