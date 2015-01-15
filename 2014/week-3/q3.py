#!/usr/bin/python3
import re

frequencies_file = [x.rstrip() for x in open("frequencies.txt")]
frequencies = [x.split(" ")[1] for x in frequencies_file]
frequencies_word = [x.split(" ")[0] for x in frequencies_file]
frequencies = [x[1] for x in sorted(zip(frequencies,frequencies_word), key=lambda x:-int(x[0]))]

numpad = ["(a|b|c)","(d|e|f)","(g|h|i)",
          "(j|k|l)","(m|n|o)","(p|q|r|s)",  
          "(t|u|v)","(w|x|y|z)",]

final_string = ""
numbers = input("Message: ").split(" ")
for number in numbers:
	regex_string = ""
	for character in number.rstrip("*"):
		regex_string += numpad[int(character)-2]
	regex_string += "$"

	temp_frequencies = []
	for word in frequencies:
		if re.match(regex_string,word):
			temp_frequencies.append(word)

	if len(temp_frequencies):
		final_string += temp_frequencies[number.count("*") % len(temp_frequencies)] + " "
	else:
		for character in enumerate(regex_string):
			if character[1] == "(":
				final_string += regex_string[character[0] + 1]
		final_string += " "
print(final_string.rstrip())
