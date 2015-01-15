#!/usr/bin/python
x=int(input())
y=input()
i=[u for u in y]
if x!=0: print(y)
for line in range(x-1):
	c=""
	for x in enumerate(i):
		left=x[0]-1
		right=x[0]+1 if x[0] != len(i)-1 else 0
		if (i[left] == "*" and i[right] == "*"):
			c+="."
		elif (i[left] == "*" or i[right] == "*"):
			c+="*"
		else:
			c+="."
	print(c)
	i=c
