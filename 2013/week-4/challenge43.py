# Enter your code for "Pac Man (I)" here.
from collections import deque

def find_ghosts(file_text):
	length = len(file_text[0])
	ghosts = []

	for line in range(len(file_text)):
		for character in range(len(file_text[line])):
			if file_text[line][character] == "G":
				ghosts.append((character,line))
			elif file_text[line][character] == "P":
				pacman = (character,line)
	return ghosts, pacman, length

def get_directions(ghost, file_text):
	directions = []
	stuff = ["."," ","P","G"]

	if file_text[ghost[1] - 1][ghost[0]] in stuff: directions.append((ghost[0],ghost[1] - 1)) 
	if file_text[ghost[1]][ghost[0] - 1] in stuff: directions.append((ghost[0] - 1,ghost[1]))
	if file_text[ghost[1] + 1][ghost[0]] in stuff: directions.append((ghost[0],ghost[1] + 1))
	if file_text[ghost[1]][ghost[0] + 1] in stuff: directions.append((ghost[0] + 1,ghost[1]))

	return directions

def move_ghosts(ghosts, pacman, length, file_text):
	all_ghost_paths = []
	for ghost in ghosts:
		node1 = ghost
		node2 = pacman
		paths = deque()
		paths.append([node1])
		
		while (paths):
			current_path = paths.popleft()
			#print(current_path)
			if (current_path[-1] == node2):
				all_ghost_paths.append(current_path)
				break
			for direction in get_directions(current_path[-1], file_text):
				if (direction not in current_path):
					new_path = list(current_path)
					new_path.append(direction)
					paths.append(new_path)
	return all_ghost_paths

def draw(ghosts, ghost_paths, file_text):
	output = []

	for i in range(len(file_text)):
		output.append([])
		for ii in file_text[i]:
			output[i].append(ii)

	for path in range(len(ghost_paths)):
		x = ghosts[path][0]
		y = ghosts[path][1]
		newx = ghost_paths[path][1][0]
		newy = ghost_paths[path][1][1]
		output[y][x] = " "
		output[newy][newx] = "G"

	for i in output:
		print("".join(i))

file = open("maze.txt")
file_text = file.read().strip().split("\n")

ghosts, pacman, length = find_ghosts(file_text)
ghost_paths = move_ghosts(ghosts, pacman, length, file_text)
draw(ghosts, ghost_paths, file_text)
