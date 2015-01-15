def recurse(a,b,s,l):
	if (len(a) <= 0 and len(b) <= 0): 
		l.append(s)
		return
	if (len(a) > 0): recurse(a[1:],b,s+a[0],l)
	if (len(b) > 0): recurse(a,b[1:],s+b[0],l)
	return l

def interleavings(a, b):
	l = recurse(a,b,"",[])
	if (not a and not b): l = ['']
	return list(sorted(set(l)))

print(interleavings("ab","cd"))
print(interleavings("a","bc"))
print(interleavings("abc","de"))
