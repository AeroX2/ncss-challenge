#!/usr/bin/python

divisions = int(input("Divisions: "))
divisible_by = []
for i in range(divisions):
	divisible_by.append(int(input("Divisible by: ")))

number_of_beats = int(input("Number of beats to print: "))
for i in range(1,number_of_beats+1):
	temp_string = str(i)+":"
	for ii in divisible_by:
		if i % ii == 0:
			temp_string += "X"
		else:
			temp_string += " "
	print(temp_string.rjust(divisions + len(str(number_of_beats)) + 1))
	
