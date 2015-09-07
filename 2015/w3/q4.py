#!/bin/env python3
import math

puzzle = []
for row in range(9):
    puzzle.append(input('Enter line: '))

for y in range(9):
    seen = {}
    for x in range(9):
        digit = puzzle[y][x]
        if digit in seen:
            if seen[digit]:
                print('duplicate', digit, 'in row', y+1)
                seen[digit] = False
        else:
            seen[digit] = True

for y in range(9):
    seen = {}
    for x in range(9):
        digit = puzzle[x][y]
        if digit in seen:
            if seen[digit]:
                print('duplicate', digit, 'in column', y+1)
                seen[digit] = False
        else:
            seen[digit] = True

grids = [[] for i in range(9)]
for y in range(9):
    for x in range(9):
        grid_y = math.floor(y / 3)
        grid_x = math.floor(x / 3)
        grids[grid_x+grid_y*3].append(puzzle[y][x])

for grid in enumerate(grids):
    seen = {}
    for number in grid[1]:
        if number in seen:
            if seen[number]:
                print('duplicate', number, 'in grid', grid[0]+1)
                seen[number] = False
        else:
            seen[number] = True
