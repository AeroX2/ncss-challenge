#!/bin/env python3
import re

usernames = {}
with open("handles.txt") as f:
    for line in f.readlines():
        line = line.strip()
        first_space = line.index(" ")
        usernames[line[:first_space].lower()] = line[first_space+1:]

line = input("Line: ")
while line:
    lines.append(line)
    line = input("Line: ")

for line in lines:
    output = ""
    for word in re.split("(\s)",line):
        match = re.match(r'^@([a-zA-Z0-9_]+)$',word)
        if match and len(word) <= 16:
            word = usernames[match.group(1).lower()] if match.group(1).lower() in usernames else "UNKNOWN_HANDLE"
        output += word
    print(output)

