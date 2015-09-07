#!/bin/env python3

import re

with open("code.py", "r", newline="\n") as f:
    lines = f.read()

output = []
matches = re.finditer(r'(.*?)(\w+)[ \t]*(\\\n)*[ \t]*=[ \t]*(\\\n)*[ \t]*{',lines)
for match in matches:
    open_quote = False
    comment = False
    for char in match.group(1):
        if char == "#":
            if not open_quote:
                comment = True
        elif char in ['"',"'"]:
            open_quote = not open_quote
    #print(match.group(1))
    #print(match.group(2))
    if not comment and not open_quote:
        output.append(match.group(2))

for i in output:
    print(i)
