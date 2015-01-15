from time import sleep
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
	if file_text[ghost[1] + 1][ghost[0]] in stuff: directions.append((ghost[0],ghost[1] + 1))
	if file_text[ghost[1]][ghost[0] - 1] in stuff: directions.append((ghost[0] - 1,ghost[1]))
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

def draw(ghosts, ghost_paths, file_text, pacman):
	output = []

	for i in range(len(file_text)):
		output.append([])
		for ii in file_text[i]:
			output[i].append(ii)
	
	max_array = 0
	for i in range(len(ghost_paths)):
		if (len(ghost_paths[i]) > max_array):
			max_array = len(ghost_paths[i])

	for i in ghost_paths:
		while len(i) < max_array:
			i.append(pacman)
	
	blub = 1
	remove = []
	while (ghosts):
		for path in range(len(ghost_paths)):
			x = ghosts[path][0]
			y = ghosts[path][1]
			newx = ghost_paths[path][blub][0]
			newy = ghost_paths[path][blub][1]
			output[y][x] = " "
			output[newy][newx] = "G"
			ghosts[path] = ghost_paths[path][blub] 
			
			if (ghosts[path][0] == pacman[0] and ghosts[path][1] == pacman[1]):
				remove.append(path)
		
		for iii in remove:
			ghost_paths.pop(iii)
			ghosts.pop(iii)
		remove = []
		blub += 1

		for ii in output:
			print("".join(ii))
		sleep(0.5)

file = open("maze.txt")
file_text = file.read().strip().split("\n")

ghosts, pacman, length = find_ghosts(file_text)
ghost_paths = move_ghosts(ghosts, pacman, length, file_text)
draw(ghosts, ghost_paths, file_text, pacman)
