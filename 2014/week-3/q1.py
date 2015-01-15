#!/usr/bin/python3
# Enter your code for "Rövarspråket!" here.
import re
def lower(x):
	con = x.group(1)
	return con + "o" + con.lower()

def upper(x):
	con = x.group(1)
	return con + ("o" if con.islower() else "O") + con

def encode(s):
	if (s.istitle()): 
		print("is")
		string = re.sub(r"([^aeiouAEIOU\s])",lower,s)
	else: string = re.sub(r"([^aeiouAEIOU\s])",upper,s)
	return string

def decode(s):
	if re.match(r"(?:([^aeiou])o\1|[^aeiou][aeiou][^aeiou])+",s,flags=re.I):
		return re.sub(r"([^aeiou])o\1",r"\1",s,flags=re.I)
	else:
		return s

print(decode(encode("stubborn")))
print(decode(encode("Sweden")))
print(decode(encode("BLOMKVIST")))
print(decode(encode("GothenburG")))
print(decode(encode("Gothenburg")))
print(decode(encode("TestCase")))
print()
print(encode("This Is A Test"))
print("Tothohisos Isos A totesostot")
print()
print(encode("This Is ATest"))
print("Tothohisos Isos ATOTesostot")
print()
print(decode("sostotubobboborornon"))
print(decode("Soswowedodenon"))
print(decode("aoatot"))
print(decode("BOBLOLOMOMKOKVOVISOSTOT"))
print(decode("Cocoololeror"))
