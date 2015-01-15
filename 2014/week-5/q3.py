#!/usr/bin/python3
from collections import deque

def load_array(room_text):
	array = []
	for line in room_text:
		array.append([])
		for character in line:
			array[-1].append(character)
	return array

def cleanup(room):
	room.insert(0, ["b"] * len(room[0]))
	room.append(["b"] * len(room[0]))
	for i in room:
		i.insert(0, "b")
		i.append("b")
	return room

def find_snake(room):
	x,y = -1,-1
	for line in enumerate(room):
		if "^" in line[1]:
			x = line[1].index("^")
			y = line[0] + 1
		elif "v" in line[1]:
			x = line[1].index("v")
			y = line[0] - 1
		elif "<" in line[1]:
			x = line[1].index("<") + 1
			y = line[0]
		elif ">" in line[1]:
			x = line[1].index(">") - 1
			y = line[0]
	return (x,y)

def get_directions(room, current):
	directions = []

	if room[current[1]][current[0] - 1] == "X": directions.append((current[0] - 1,current[1])) 
	if room[current[1]][current[0] + 1] == "X": directions.append((current[0] + 1,current[1]))
	if room[current[1] - 1][current[0]] == "X": directions.append((current[0],current[1] - 1))
	if room[current[1] + 1][current[0]] == "X": directions.append((current[0],current[1] + 1))

	return directions

def eradicate_python(room, node):
	snake_length = 1
	queue = deque()
	queue.append(node)
	while queue:
		current_node = queue.popleft()
		if (room[current_node[1]][current_node[0]] == "X"):
			room[current_node[1]][current_node[0]] = "."
			snake_length += 1
			for direction in get_directions(room, current_node):
				queue.append(direction)
	return snake_length

file_text = open("room.txt").read().strip().split("\n")
room_array = load_array(file_text)
room_array = cleanup(room_array)
snake_head = find_snake(room_array)

if (snake_head[0] != -1):
	#Snake
	print(eradicate_python(room_array, snake_head))
else:
	#No snake
	print("0")
