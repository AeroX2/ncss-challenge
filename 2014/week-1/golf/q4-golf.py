#!/usr/bin/python
import math
lines = [line.rstrip() for line in open("draw.txt").readlines()]
z = [[team.split(",")[0] for team  in lines]]
sr = [[score.split(",")[1] for score in lines]]
input_x = input()
input_y = input()
while (len(z[-1]) != 1):
	teams_left = []
	scores_left = []
	for team in range(0,len(z[-1])-1,2):
		x = z[-1][team]
		y = z[-1][team+1]
		x_score = sr[-1][team]
		y_score = sr[-1][team+1]
		if x_score < y_score:
			teams_left.append(x)
			scores_left.append(x_score)
		else:
			teams_left.append(y)
			scores_left.append(y_score)
	z.append(teams_left)
	sr.append(scores_left)

cr,rp = 0,0
for q in z:
	cr += 1
	if (input_x in q or input_y in q):
		try:
			if (math.floor(q.index(input_x)/2) == math.floor(q.index(input_y)/2)):
				rp = cr
		except:
			pass
if (rp > 0):
	print("Round " + str(rp))
else:
	print("Did not play")
