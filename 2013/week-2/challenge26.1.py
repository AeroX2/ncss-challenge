import re

site=open("site.html").read()
for m in re.findall('img .*?src="(.*?)"', site):print(m)
#print(*re.findall('img .*?src="(.*?)"', site))
