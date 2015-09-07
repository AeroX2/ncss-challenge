#!/bin/env python3

words = []
with open("words.txt") as f:
    for line in f:
        words.append(line.strip())

words = sorted(words, key=lambda x: x[::-1])
for word in words:
    print(word)
