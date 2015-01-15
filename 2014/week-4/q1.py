#!/usr/bin/python3
import re

def stripVowels(s):
	return re.sub("[aeiouAEIOU]","",s)

line = input("Line: ")
lines = []
while line:
	lines.append(line)
	line = input("Line: ")

no_vowels_words = set()
words = []
for line in lines:
	for word in re.split("[\s.,;-]",line):
		if len(word) >= 4:
			no_vowels_words.add(stripVowels(word))
			words.append(word)

final_strings = {}
for no_vowel_word in no_vowels_words:
	for word in words:
		no_vowel_word = no_vowel_word.lower()
		word = word.lower()
		if no_vowel_word == stripVowels(word):
			if no_vowel_word in final_strings.keys():
				final_strings[no_vowel_word].add(word)
			else:
				final_strings[no_vowel_word] = set([word])
for key in list(final_strings.keys()):
	if len(final_strings[key]) >= 2:
		print(" ".join(sorted(final_strings[key])))
