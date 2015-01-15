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
def solveJewels(jewels,vertical):
	score = 0
	remove = []
	#print("FIX REGEX")
	r = re.compile(r"([^?])\1\1(\1+)?")
	for x in enumerate(jewels):
		for match in r.finditer("".join(x[1])):
			for y in range(match.start(),match.end()):
				#print("Vertical: " + str(vertical))
				if vertical: 
					remove.append((x[0],y))
				else: 
					remove.append((y,x[0]))
			score += 10 + 10 * (match.end() - match.start() - 3)
	return score,remove

def removeJewels(jewels, remove):
	#print(remove)
	for position in remove:
		#print(jewels[position[0]])
		jewels[position[0]][position[1]] = ""
		jewels[position[0]].append("?")
    #Dont ask
	for x in jewels:
		while "" in x:
			x.remove("")
#Loading
jewels_file = open("jewels.txt").read().strip()
jewels = [[],[],[],[],[],[],[],[]]

#Setup
column = 0
for jewel in jewels_file:
	jewels[column].append(jewel)
	column = (column + 1) % 8
#print(jewels)
score = 0
printJewels(jewels)
print("Score = 0")

while True:
	scoreV, removeV = solveJewels(jewels,True)
	scoreH, removeH = solveJewels(flipArray(jewels),False)

	#print(removeV, removeH)
	remove = set(removeV + removeH)
	if not remove:
		break

	#print(remove)
	removeJewels(jewels, remove)
	score += scoreV + scoreH

printJewels(jewels)
print("Score = " + str(score))
