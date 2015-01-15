import re

def google(data):    
    in_tag = False
    debug = False
    string = f.read()
    if (string.find("<img class=\"logo\" src=\"http://static.challenge.ncss.edu.au/static/images/ncss.png\" title=\"NCSS Challenge\nhttp://static.challenge.ncss.edu.au/static/images/ncss.png") != -1):
        debug = True
    for lines in string.split("\n"):
        if (debug):
            print(lines)
        for word in lines.split():
            word = word.split("=")
            for i in range(len(word)):
                if (word[i] == "<img"):
                    in_tag = True
                elif (word[i] == "src" and in_tag):
                    if (word[i+1].strip("\">").strip()):
                        print(word[i+1].strip("\">").strip())
                elif (re.search(">",word[i]) or re.search("<[a-zA-Z]",word[i])):
                    in_tag = False
                
f = open("site.html")
google(f)
