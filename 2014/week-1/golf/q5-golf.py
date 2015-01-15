def is_kaprekar(n):
	k,s=n==1,str(n**2)
	for i in range(len(s)-1):
		f,x=int(s[i+1:]),int(s[:i+1])
		if f!=0 and x!=0 and f+x==n:
			k=True
	return k
