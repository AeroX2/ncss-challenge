#!/usr/bin/python3
import re

tags = {}
input_file = open("input.html").read().rstrip()

matches = [x.lower() for x in re.findall(r"<(\w+)(?:\s+[\s\S]*?)?\/*>",input_file)]
final_string = ""
max_num = 0
for match in set(matches):
	print(match + " " + str(matches.count(match)))
