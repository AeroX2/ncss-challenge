#!/usr/bin/python3
import math

lines = [line.rstrip() for line in open("draw.txt").readlines()]
team_rounds = [[team.split(",")[0] for team  in lines]]
score_rounds = [[score.split(",")[1] for score in lines]]

input_team_1 = input("Team 1: ")
input_team_2 = input("Team 2: ")

while (len(team_rounds[-1]) != 1):
	teams_left = []
	scores_left = []
	for team in range(0,len(team_rounds[-1])-1,2):
		team_1 = team_rounds[-1][team]
		team_2 = team_rounds[-1][team+1]
		team_1_score = score_rounds[-1][team]
		team_2_score = score_rounds[-1][team+1]
		if team_1_score < team_2_score:
			teams_left.append(team_1)
			scores_left.append(team_1_score)
		else:
			teams_left.append(team_2)
			scores_left.append(team_2_score)
	team_rounds.append(teams_left)
	score_rounds.append(scores_left)

current_round = 0
round_played = 0
print(team_rounds)
for team_round in team_rounds:
	current_round += 1
	if (input_team_1 in team_round or input_team_2 in team_round):
		try:
			if (math.floor(team_round.index(input_team_1)/2) == math.floor(team_round.index(input_team_2)/2)):
				round_played = current_round
		except:
			pass
if (round_played > 0):
	print("Round " + str(round_played))
else:
	print("Did not play")
