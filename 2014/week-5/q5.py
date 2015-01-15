#!/usr/bin/python3
import re
import copy

def flipArray(arr):
	a = copy.deepcopy(arr)
	n = len(a)
	for i in range(n):
		for j in range(i+1,n):
			a[i][j],a[j][i] = a[j][i],a[i][j]
	return a

#Printer
def printJewels(jewels):
	for y in reversed(range(len(jewels[0]))):
		line = ""
		for x in range(len(jewels)):
			line += jewels[x][y] + " "
		print(line.strip())

#Solver
def matchJewels(jewels,vertical):
	score = 0
	remove = []
	r = re.compile(r"([^?])\1\1(\1+)?")
	for x in enumerate(jewels):
		for match in r.finditer("".join(x[1])):
			for y in range(match.start(),match.end()):
				if vertical: 
					remove.append((x[0],y))
				else: 
					remove.append((y,x[0]))
			score += 10 + 10 * (match.end() - match.start() - 3)
	return score,remove

def removeJewels(jewels, new_jewels, remove):
	for position in remove:
		jewels[position[0]][position[1]] = ""
    #Dont ask
	for x in jewels:
		while "" in x:
			x.append(new_jewels.pop())
			x.remove("")

def solveJewels(jewels, new_jewels, score):
	scoreMultiplyer = 1
	while True:
		scoreV, removeV = matchJewels(jewels,True)
		scoreH, removeH = matchJewels(flipArray(jewels),False)

		#print(removeV, removeH)
		remove = set(removeV + removeH)
		if not remove:
			break

		#print(remove)
		removeJewels(jewels, new_jewels, remove)
		score += (scoreV + scoreH) * scoreMultiplyer 
		scoreMultiplyer += 1
	return jewels,score

def checkMove(jewels, move):
	try:
		x1,y1,x2,y2 = map(int,move.split())
		#Out of bounds
		if min(x1,x2) < 0: return False
		if min(y1,y2) < 0: return False
		if max(x1,x2) >= len(jewels): return False
		if max(y1,y2) >= len(jewels[0]): return False
		
		#Not touching or diagonal
		if abs(x1-x2) > 1 or abs(y1-y2) > 1: return False
		if abs(x1-x2) == abs(y1-y2): return False
	except:
		return False

	temp = jewels[x1][y1]
	jewels[x1][y1] = jewels[x2][y2]
	jewels[x2][y2] = temp

	_, removeV = matchJewels(jewels,True)
	_, removeH = matchJewels(flipArray(jewels),False)

	remove = set(removeV + removeH)
	if remove:
		return True
	else:
		temp = jewels[x1][y1]
		jewels[x1][y1] = jewels[x2][y2]
		jewels[x2][y2] = temp
		return False

#Loading
jewels_file = open("jewels.txt").read().strip()
jewels_array = [[],[],[],[],[],[],[],[]]

#Setup
column = 0
for jewel in jewels_file[:64]:
	jewels_array[column].append(jewel)
	column = (column + 1) % 8

new_jewels = []
for jewel in reversed(jewels_file[64:]):
	new_jewels.append(jewel)

score = 0
printJewels(jewels_array)
print("Score = 0")
move = input("Move: ")
while move:
	if (not checkMove(jewels_array, move)):
		print("Invalid move")
	else:
		jewels_array, score = solveJewels(jewels_array, new_jewels, score)
		printJewels(jewels_array)
		print("Score = " + str(score))
	move = input("Move: ")

#jewels_array,score = solveJewels(jewels_array,score)
