def form_teams(n, skills):
    programmers = []
    mathematicians = []
    athletes = []

    for i in range(n):
        if skills[i] == 1:
            programmers.append(i + 1)
        elif skills[i] == 2:
            mathematicians.append(i + 1)
        elif skills[i] == 3:
            athletes.append(i + 1)

    max_teams = min(len(programmers), len(mathematicians), len(athletes))

    teams = []

    for i in range(max_teams):
        team = (programmers[i], mathematicians[i], athletes[i])
        teams.append(team)

    print(max_teams)
    for team in teams:
        print(*team)


n = int(input())
skills = list(map(int, input().split()))

form_teams(n, skills)
