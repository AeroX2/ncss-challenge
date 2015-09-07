#!/bin/env python3

def get_direction(coord1, coord2):
    if coord2[0] - coord1[0] < 0: return 0
    if coord2[0] - coord1[0] > 0: return 2
    if coord2[1] - coord1[1] < 0: return 3
    if coord2[1] - coord1[1] > 0: return 1

def rotate(arr, num):
    newarr = arr.copy()
    for i in range(num):
        newarr.insert(3,newarr.pop(0))
    return newarr

def generate(dice, direction):
    #up, right, down, left, bottom, top
    #Should have created a class that contains this
    new_dice = dice.copy()
    if direction == 1: #Right
        new_dice[1] = dice[4] #right = old top
        new_dice[3] = dice[5] #left = old bottom
        new_dice[4] = dice[3] #top = old left
        new_dice[5] = dice[1] #bottom = old right
    if direction == 3: #Left
        new_dice[1] = dice[5] #right = old bottom
        new_dice[3] = dice[4] #left = old top
        new_dice[4] = dice[1] #top = old right
        new_dice[5] = dice[3] #bottom = old left
    if direction == 0: #Up
        new_dice[0] = dice[4] #up = old top
        new_dice[2] = dice[5] #down = old bottom
        new_dice[4] = dice[2] #bottom = old up
        new_dice[5] = dice[0] #top = old down
    if direction == 2: #Down
        new_dice[0] = dice[5] #up = old bottom
        new_dice[2] = dice[4] #down = old top
        new_dice[4] = dice[0] #bottom = old down
        new_dice[5] = dice[2] #top = old up
    return new_dice



original_dice = {1:[2,4,5,3,6,1], 
                 2:[6,4,1,3,5,2],
                 3:[6,2,1,5,4,3],
                 4:[1,2,6,5,3,4],
                 5:[1,4,6,3,2,5],
                 6:[5,4,2,3,1,6]}

dface = int(input("Downwards-facing face: "))
path_input = input("Path: ")
path = []
if path_input:
    for coord in path_input.split(" "):
        path.append([int(coord[0]),int(coord[2])])

maze = []
with open("maze.txt") as f:
    for line in f.readlines():
        maze.append([])
        for char in line[:-1]:
            maze[-1].append(int(char))

valid = True if path_input else False
if valid:
  if maze[path[0][0]][path[0][1]] != dface:
      valid = False

if (len(path) > 1):
    rotation = 0
    for i in range(4):
        maze_face = maze[path[1][0]][path[1][1]] 
        rotated_dice = rotate(original_dice[dface],rotation)
        dice_face = rotated_dice[get_direction(path[0],path[1])]
        if maze_face == dice_face:
            old_dice = generate(rotated_dice,get_direction(path[0],path[1]))
            break
        rotation += 1
    else:
        valid = False

    if valid:
        lastcoord = path[1]
        for coord in path[2:]:
            direction = get_direction(lastcoord,coord)
            maze_face = maze[coord[0]][coord[1]] 
            if maze_face == old_dice[direction]:
                new_dice = generate(old_dice, direction)
                old_dice = new_dice
            else:
                valid = False
                break
            lastcoord = coord
    
if valid:
    print("Valid path.")
else:
    print("Invalid path.")

