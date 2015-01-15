f = open("commentary.txt")
text = f.read()

teams = {}
team1 = text.split()[0]
team2 = text.split()[2]


teams[team1] = 0
teams[team2] = 0

for line in text.split("\n")[1:]:
    teams[line.split()[0]] += 1 

if teams[team1] > teams[team2]:
    print(team1 + " " + str(teams[team1]))
    print(team2 + " " + str(teams[team2]))
else:
    print(team2 + " " + str(teams[team2]))
    print(team1 + " " + str(teams[team1]))
