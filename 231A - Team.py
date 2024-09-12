def team(values):
    countV = 0
    for i in values:
        if i.count(1) >= 2:
            countV += 1
    return countV


N = int(input())
cases = []
for _ in range(N):
    cases.append(list(map(int, input().split())))
print(team(cases))
