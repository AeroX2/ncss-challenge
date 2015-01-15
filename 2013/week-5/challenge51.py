from collections import deque

def cleanup(text):
	max_length = 0
	for line in text:
		max_length = max([len(line),max_length])

	text.reverse()
	text.append("." * max_length)
	text.reverse()
	text.append("." * max_length)
	for line in range(len(text)):
		text[line] = text[line].ljust(max_length,"&") + "&"
	return text

def get_coords(file_text):
	coords = []
	for line in range(len(file_text)):
		coords.append([])
		for column in range(len(file_text[line])):
			coords[line].append(file_text[line][column])
	return coords

def get_directions(current, coords):
	directions = []

	if coords[current[1]][current[0] - 1] == "%": directions.append((current[0] - 1,current[1])) 
	if coords[current[1]][current[0] + 1] == "%": directions.append((current[0] + 1,current[1]))
	if coords[current[1] - 1][current[0]] == "%": directions.append((current[0],current[1] - 1))
	if coords[current[1] + 1][current[0]] == "%": directions.append((current[0],current[1] + 1))
	if coords[current[1] - 1][current[0] - 1] == "%": directions.append((current[0] - 1,current[1] - 1)) 
	if coords[current[1] + 1][current[0] + 1] == "%": directions.append((current[0] + 1,current[1] + 1))
	if coords[current[1] - 1][current[0] + 1] == "%": directions.append((current[0] + 1,current[1] - 1))
	if coords[current[1] + 1][current[0] - 1] == "%": directions.append((current[0] - 1,current[1] + 1))

	return directions

def get_and_remove_patch(coords, node):
	queue = deque()
	queue.append(node)
	while queue:
		current_node = queue.popleft()
		if (coords[current_node[1]][current_node[0]] == "%"):
			coords[current_node[1]][current_node[0]] = "."
			for direction in get_directions(current_node, coords):
				queue.append(direction)

def find_patches(coords):
	patches = 0
	line = 0
	while (line < len(coords)):
		if ("%" in coords[line]):
			x = coords[line].index("%")
			y = line

			get_and_remove_patch(coords, (x,y))
			patches += 1
		else:
			line += 1
	return patches

file_text = open("patches.txt").read().strip().split("\n")
file_text = cleanup(file_text)
coords = get_coords(file_text)
amount_of_patches = find_patches(coords)

print(str(amount_of_patches) + (" patch" if amount_of_patches == 1 else " patches"))
