#!/usr/bin/python3

holes_file = [x.rstrip() for x in open("holes.txt")]
balls_file = [x.rstrip() for x in open("balls.txt")]
hole_sizes = [int(x.split(" ")[0]) for x in holes_file]
hole_capacity = [int(x.split(" ")[1]) for x in holes_file]
final_balls = []
for ball in balls_file:
	ball_size = int(ball.split(" ")[0])
	ball_label = ball.split(" ")[1]
	made_it = True
	for hole in range(len(hole_sizes)):
		if ball_size <= hole_sizes[hole] and hole_capacity[hole] > 0:
			hole_capacity[hole] -= 1
			made_it = False
			break
	if (made_it):
		final_balls.append(ball_label)
if (final_balls):
	print("The bucket contains: " + (", ".join(final_balls)) + ".")
else:
	print("The bucket contains no balls.")
	
