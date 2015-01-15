#!/usr/bin/python3
import re

def count(s):
	#print(s.groups())
	if (s.group(1).lower() in tags.keys()):
		tags[s.group(1).lower()] += 1
	else:
		tags[s.group(1).lower()] = 1
	return s.group(2)

tags = {}
input_file = open("input.html").read().rstrip()
#print(input_file)
while re.search(r"<(\w+)(?:\s+.*?)?>([\s\S]*?)<\/\1>",input_file) or re.search(r"<((\w+))(\s+.*)?\/>",input_file):
	input_file = re.sub(r"<(\w+)(?:\s+.*?)?>([\s\S]*?)<\/\1>",count,input_file)
	input_file = re.sub(r"<((\w+))(\s+.*)?\/>",count,input_file)
	#print(input_file)
#print(tags)

max_keys = [""]
max_nums = [0]
for key in tags.keys():
	if tags[key] > max_nums[0]:
		max_keys = [key]
		max_nums = [tags[key]]
	elif tags[key] == max_nums[0] and len(key) > len(max_keys[0]):
		max_keys = [key]
		max_nums = [tags[key]]
	elif tags[key] == max_nums[0] and len(key) == len(max_keys[0]):
		max_keys.append(key)		
		max_nums.append(tags[key])
for key in enumerate(max_keys):
	print(key[1],max_nums[key[0]])
