import re

def google(data):    
    in_tag = False
    in_comment = False
    line_test = False

    for lines in f:
        word = lines.split("=")

        if (line_test):
            print(lines[:lines.rfind("\"")])
        if (re.search("\.[a-zA-Z0-9]",lines)):
            line_test = False

        for i in range(len(word)):
            if (re.search("<img ",word[i])):
                in_tag = True
            elif (re.search(">[^\"]",word[i]) or re.search("<[a-zA-Z]",word[i])):
                in_tag = False
            if (re.search("<!--",word[i])):
                in_comment = True
            elif (re.search("-->",word[i])):
                in_comment = False

            #Fix this to remove asd
            #print(word)
            if (re.search("src[ \t\n]*$",word[i]) and in_tag and not in_comment):
                if (word[i+1]):
                    if (re.search("(\"|\')*([^\"\'>]+)(\"|\')+",word[i+1])):
                        blub = lambda x: print(x.group(2))
                        #Greedy, non-greedy unfortunately it matters
                        re.sub("(\"|\')*([^\"\'>]+)(\"|\')+",blub,word[i+1])
                    else:
                        #ii = 0
                        #while (not re.search("\.[a-zA-Z0-9]",word[i+ii])):
                        #    ii += 1
                        blub2 = lambda x: print(x.group(2))
                        re.sub("(\"|\')(.+)",blub2,word[i+1])
                        #print(lines.find("\""))
                        #print(word[i+1][lines.find("\""):])
                        line_test = True
        
f = open("site.html")
google(f)
