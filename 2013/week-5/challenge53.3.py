# Enter your code for "Pac Man (II)" here.
from collections import deque
import copy

def find_ghosts(board):
	new_length = len(board[0])
	new_ghosts = []

	for line in range(len(board)):
		for character in range(len(board[line])):
			if board[line][character] == "G":
				new_ghosts.append((character,line))
			elif board[line][character] == "P":
				new_pacman = (character,line)
	return new_ghosts, new_pacman, new_length

def get_directions(ghost, board):
	directions = []
	stuff = ["."," ","P","G"]
	
	if board[ghost[1] - 1][ghost[0]] in stuff: directions.append((ghost[0],ghost[1] - 1)) 
	if board[ghost[1]][ghost[0] - 1] in stuff: directions.append((ghost[0] - 1,ghost[1]))
	if board[ghost[1]][ghost[0] + 1] in stuff: directions.append((ghost[0] + 1,ghost[1]))
	if board[ghost[1] + 1][ghost[0]] in stuff: directions.append((ghost[0],ghost[1] + 1))

	return directions

def move_pacman(command, pacman, oldpacman, board):
	new_board = board
	new_pacman = pacman
	new_old_pacman = oldpacman
	new_points = points
	stuff = ["."," "]
	
	if (command == "U"):
		if (new_board[pacman[1]-1][pacman[0]] in stuff):                        
			new_old_pacman = (pacman[0],pacman[1])
			new_pacman = (pacman[0],pacman[1]-1) 
	elif (command == "D"):
		if (new_board[pacman[1]+1][pacman[0]] in stuff):                        
			new_old_pacman = (pacman[0],pacman[1])
			new_pacman = (pacman[0],pacman[1]+1)
	elif (command == "L"):
		if (new_board[pacman[1]][pacman[0]-1] in stuff):                        
			new_old_pacman = (pacman[0],pacman[1])
			new_pacman = (pacman[0]-1,pacman[1]) 
	elif (command == "R"):
		if (new_board[pacman[1]][pacman[0]+1] in stuff):                        
			new_old_pacman = (pacman[0],pacman[1])
			new_pacman = (pacman[0]+1,pacman[1]) 
	return new_pacman, new_old_pacman

def move_ghosts(ghosts, oldghosts, pacman, length, board):
	all_ghost_paths = []
	new_ghosts = copy.deepcopy(ghosts)
	new_oldghosts = copy.deepcopy(oldghosts)
	new_board = board
	
	for ghost in ghosts:
		node1 = ghost
		node2 = pacman
		paths = deque()
		paths.append([node1])
		
		while (paths):
			current_path = paths.popleft()
			if (current_path[-1] == node2):
				all_ghost_paths.append(current_path)
				break

			for direction in get_directions(current_path[-1], board):
				if (direction not in current_path):
					new_path = list(current_path)
					new_path.append(direction)
					paths.append(new_path)
	
	for path in range(len(all_ghost_paths)):
		oldghosts[path] = all_ghost_paths[path][0]
		new_ghosts[path] = all_ghost_paths[path][1]        
        
	return (new_ghosts, oldghosts)

def create_board(file_text):
	output = []
	for i in range(len(file_text)):
		output.append([])
		for ii in file_text[i]:
			output[i].append(ii)
	return output
        

def draw(board,point):
	print("Points: " + str(points))
	for i in board:
		print("".join(i))

def update(oldpacman, pacman, oldghosts, ghosts, ghost_dot, points, board):
	newboard = board
	newpoints = points
	
	newboard[oldpacman[1]][oldpacman[0]] = " "
	if (newboard[pacman[1]][pacman[0]] == "."):
		newpoints += 1
	newboard[pacman[1]][pacman[0]] = "P"

	while (len(oldghosts) != len(ghost_dot)):
		oldghosts.pop()
		ghosts.pop()
		
	for ghost in range(len(oldghosts)):
		if (ghost_dot[ghost]):
			newboard[oldghosts[ghost][1]][oldghosts[ghost][0]] = "."
		else:
			newboard[oldghosts[ghost][1]][oldghosts[ghost][0]] = " "

	ghost_dot = []
	for ghost in ghosts:
		if (newboard[ghost[1]][ghost[0]] == "."):
			ghost_dot.append(True)
		else:
			ghost_dot.append(False)
		if (newboard[ghost[1]][ghost[0]] == "G"):
			ghost_dot.pop()
			newboard[ghost[1]][ghost[0]] = "G"
		else:
			newboard[ghost[1]][ghost[0]] = "G"

	return newboard, newpoints, ghost_dot

file = open("maze.txt")
file_text = file.read().strip().split("\n")
commands = input("Commands: ")

board = create_board(file_text)
ghosts, pacman, length = find_ghosts(file_text)

died = False
win = False
points = 0

ghost_dot = []
oldghosts = ghosts
oldpacman = pacman
for i in ghosts:
	ghost_dot.append(False)

for command in commands.strip().split(" "):
    #Check win
    win = True
    for line in board:
        if "." in line:
            win = False
    if (win):
        print("You won!")
        draw(board,points)
        break

    if (command != ""):
        if (command != "O"):
            #oldghosts,oldpacman,length = find_ghosts(board)
            ghosts,oldghosts = move_ghosts(ghosts, oldghosts, pacman, length, board)
            pacman,oldpacman = move_pacman(command, pacman, oldpacman, board)
            board,points,ghost_dot = update(oldpacman, pacman, oldghosts, ghosts, ghost_dot, points, board)
        else:
            draw(board,points)
            
    win = True
	for line in board:
        if "." in line:
            win = False
	for dot in ghost_dots:
		if (dot):
			win = False
    if (win):
        print("You won!")
        draw(board,points)
        break
        
    #Check dies
    for ghost in ghosts:
        if (ghost == pacman):
            print("You died!")
            draw(board,points)
            died = True
    if (died):
        break
                
if (not died and not win):
        draw(board,points)
