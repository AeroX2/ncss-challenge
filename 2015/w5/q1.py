#!/bin/env python3

def move(start,stop,step,ytrue,z):
    global crossword
    number = 0
    fine = False
    for i in range(start,stop,step):
        char = crossword[z][i]
        if char == "#":
            break
        elif char == " ":
            fine = True
            crossword[z][i] = "%"
        elif char == "%":
            fine = True
        else:
            crossword[z][i] = "%"

        number += 1
    return number,fine

crossword = []
with open("crossword.txt") as f:
    for line in f.readlines():
        crossword.append([])
        for char in line.strip("\n"):
            crossword[-1].append(char)

old_crossword = [row[:] for row in crossword]
crossword = [list(row) for row in zip(*crossword)]
blub = []
for x1 in enumerate(crossword):
    for y1 in enumerate(x1[1]):
        if y1[1] not in ["#","%"]:
            down = 0
            y = y1[0]
            x = x1[0]

            c = crossword[x][y] in ["%"," "]
            crossword[x][y] = "%"
            a,b = move(y+1,len(crossword[0]),1,True,x)
            if b or c:
                down += a
            if down > 0:
                down += 1
                blub.append((y,x,down))

crossword = old_crossword
blub2 = []
for y1 in enumerate(crossword):
    for x1 in enumerate(y1[1]):
        if x1[1] not in ["#","%"]:
            across = 0
            y = y1[0]
            x = x1[0]

            c = crossword[y][x] in ["%"," "]
            crossword[y][x] = "%"
            a,b = move(x+1,len(crossword[0]),1,False,y)
            if b or c:
                across += a
            if across > 0:
                across += 1
                blub2.append((y,x,across))

for i in blub:
    print("({},{}) down, {} letters.".format(i[0],i[1],i[2]))
for i in blub2:
    print("({},{}) across, {} letters.".format(i[0],i[1],i[2]))
