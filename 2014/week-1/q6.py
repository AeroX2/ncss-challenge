#!/usr/bin/python

def count_collisions(text, keypad):
	numbers = []
	collisions = 0
	for word in text.lower().split():
		number = ""
		for letter in word:
			number += str(keypad[letter])
		numbers.append(int(number))
	for number in set(numbers):
		if (numbers.count(number) > 1):
			collisions += numbers.count(number)
	return collisions
			
			
# Helper function to build a keypad mapping from a list of strings.
def make_mapping(l):
	mapping = {}
	for i in range(len(l)):
		for letter in l[i]:
			mapping[letter] = i
	return mapping

mapping = make_mapping('  abc def ghi jkl mno pqrs tuv wxyz'.split())
print('This should be 4:', count_collisions('In a brief aside the bride cried', mapping))

mapping = make_mapping('  aei ou bcgh jkl mnd pqrs tfv wxyz'.split())
print('This should be 0:', count_collisions('In a brief aside the bride cried', mapping))
