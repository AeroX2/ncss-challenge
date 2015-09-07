#!/bin/env python3
import re

lines = []
with open("atotc.txt") as f:
    lines = f.readlines()

quotes = []
for line in lines:
    quotes.append(re.findall('"(.+)"', line))

print(quotes)
for quote in quotes:
    if quote is None: continue
    for subquote in quote:
        print(subquote)
