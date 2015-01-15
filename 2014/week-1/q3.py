#!/usr/bin/python3

number_lines = int(input("Number of lines: "))
start_line = input("Start line: ")

grid = [character for character in start_line]
if number_lines != 0: print(start_line)

for line in range(number_lines-1):
	current_string = ""
	for x in enumerate(grid):
		left = x[0]-1
		right = x[0]+1 if x[0] != len(grid)-1 else 0
		if (grid[left] == "*" and grid[right] == "*"):
			current_string += "."
		elif (grid[left] == "*" or grid[right] == "*"):
			current_string += "*"
		else:
			current_string += "."
	print(current_string)
	grid = current_string
