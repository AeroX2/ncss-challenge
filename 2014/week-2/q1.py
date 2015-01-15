#!/usr/bin/python3
line = input("Line: ")
while line:
	vicinals = []
	nonvicinals = []
	for word in line.split():
		vicinal = True
		for letter in word.lower():
			beforechr = chr(ord(letter)-1) if ord(letter)-1 != 96 else "z"
			nextchr = chr(ord(letter)+1) if ord(letter)+1 != 123 else "a"
			if (beforechr not in word.lower() and nextchr not in word.lower()):
				vicinal = False
		if (vicinal):
			vicinals.append(word)
					
	for word in line.split():
		nonvicinal = True
		for letter in word.lower():
			beforechr = chr(ord(letter)-1) if ord(letter)-1 != 96 else "z"
			nextchr = chr(ord(letter)+1) if ord(letter)+1 != 123 else "a"
			if (beforechr in word.lower() or nextchr in word.lower()):
				nonvicinal = False
		if (nonvicinal):
			nonvicinals.append(word)

	if (vicinals):
		print("Vicinals: " + " ".join(vicinals))
	if (nonvicinals):
		print("Non-vicinals: " + " ".join(nonvicinals))
	line = input("Line: ")
