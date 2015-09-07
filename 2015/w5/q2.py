#!/bin/env python3
def recurse(cartridges,money,paper,brought):
    new_paper = paper
    new_brought = brought
    for c in enumerate(cartridges):
        if money-c[1][1] >= 0:
            x,y = recurse(cartridges,money-c[1][1],paper+c[1][2],brought+[c[1]])
            if x > new_paper:
                new_paper = x
                new_brought = y
    return new_paper, new_brought

budget = int(input("Budget: "))

cartridges = []
cartridge = input("Cartridge: ")
while cartridge:
    x = cartridge.split(" ")
    cartridges.append([x[0],int(x[1]),int(x[2])])
    cartridge = input("Cartridge: ")

#testing = """HP 80 2401
#Acme 20 11
#Canon 40 1200
#MSY 30 50"""
#for line in testing.split("\n"):
#    cartridges.append(line.split(" "))

paper, brought = recurse(cartridges,budget,0,[])
money = 0
for b in brought:
    money += b[1]
print("Best option is {} page(s) costing {}:".format(paper,money))
final = []
for cartridge in cartridges:
    count = 0
    for item in brought:
        if item == cartridge:
            count += 1
    final.append((cartridge[0],count))
for i in sorted(final,key=lambda r: (-r[1],r[0])):
    print(i[0],i[1])
