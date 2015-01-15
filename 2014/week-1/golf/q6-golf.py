def count_collisions(t,k):
	x,y=[],0
	for w in t.lower().split():
		z=""
		for l in w:
			z+=str(k[l])
		x+=[int(z)]
	for z in set(x):
		if (x.count(z)>1):
			y+=x.count(z)
	return y
