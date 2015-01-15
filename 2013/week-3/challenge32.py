import re

file = open("leaderboard.txt")
file_text = file.readlines()
scores = []
names = []

students = []

for line in file_text:
    line = line.strip().split(",")
    students.append(line)
#    names.append(line[0])
#    scores.append(line[1])

new = []

for student in students:
    name = student[0]
    name = name.lstrip("0123456789").strip()
    name = re.sub(r"^[A-Z]+([A-Z])+",r"\1",name)
    name = re.sub(r" \b[A-Z0-9]+(?![a-z])\b","",name)
    name = re.sub(r"\b[A-Z0-9]+(?![a-z])\b ","",name)
    name = re.sub(r"\b[a-z][A-Za-z0-9]\b","",name)
    name = re.sub(r" \b[a-z]+[A-Za-z0-9]*\b","",name)
    name = re.sub(r"\b[a-z]+[A-Za-z0-9]*\b ","",name)
    name = re.sub(r" [a-z0-9]+\b","",name)
    #name = re.sub(r"  ","",name)
    if (name.isupper() or not name[0].isupper()): name = ""
    if (name == ""): name = "Invalid Name"

    new.append((name, int(student[1])))

#blub2 = sorted(zip(scores,names),reverse=True)
blub2 = sorted(new, key=lambda x:(-x[1], x[0]))
for i in blub2:
    print('%s,%d' % (i[0], i[1]))
