user_input = input("Line: ")
lines = []
output = ""

while (user_input):
    lines.append(user_input)
    user_input = input("Line: ")
#lines.reverse()

for line in lines:
    for word in line.split(" "):
        output += word[::-1] + " "
    print(output.rstrip())
    output = ""
