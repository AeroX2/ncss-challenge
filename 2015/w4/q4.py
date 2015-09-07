#!/bin/env python3

def intersect(a,b,c,d):
    t1 = ((a[0]-c[0])*(d[1]-c[1])-(a[1]-c[1])*(d[0]-c[0]))*((b[0]-c[0])*(d[1]-c[1])-(b[1]-c[1])*(d[0]-c[0]))
    t2 = ((c[0]-a[0])*(b[1]-a[1])-(c[1]-a[1])*(b[0]-a[0]))*((d[0]-a[0])*(b[1]-a[1])-(d[1]-a[1])*(b[0]-a[0]))
    return t1 <= 0 and t2 <= 0

def overlap(a,b,c,d):
    return min(c[0],d[0]) <= max(a[0],b[0]) and min(a[0],b[0]) <= max(c[0],d[0]) and min(c[1],d[1]) <= max(a[1],b[1]) and min(a[1],b[1]) <= max(c[1],d[1])

commandos_i = input("Enter commandos: ")
turrets_i = input("Enter turrets: ")
base_i = input("Enter base: ")

#commandos_i = "1,5 2,0 4,1 5,2 5,4"
#turrets_i = "0,2 2,4"
#base_i = "4,3 4,2 3,2 3,1 1,3"

commandos = []
if commandos_i:
    for i in commandos_i.split(" "):
        i = i.split(",")
        commandos.append((int(i[0]),int(i[1])))
turrets = []
if turrets_i:
    for i in turrets_i.split(" "):
        i = i.split(",")
        turrets.append((int(i[0]),int(i[1])))
base = []
if base_i:
    for i in base_i.split(" "):
        i = i.split(",")
        base.append((int(i[0]),int(i[1])))

hits = set()
for commando in commandos:
    can_be_shot = False
    for turret in turrets:
        cannot_be_shot = False
        for base_coord in enumerate(base):
            #print(base_coord[1],base[base_coord[0]-1],turret,commando)
            if intersect(base_coord[1],base[base_coord[0]-1],turret,commando) and overlap(base_coord[1],base[base_coord[0]-1],turret,commando):
                cannot_be_shot = True
                break
        if not cannot_be_shot:
            can_be_shot = True
            break
    if not can_be_shot:
        hits.add(commando)


for hit in hits:
    print(str(hit[0])+","+str(hit[1]))
