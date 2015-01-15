number = input("Number: ")
width = int(input("Width: "))

width_total = width + 2
height_total = 2 * width + 3

def define_numbers():
    file = open("numbers.txt")
    numbers = []
    blub = []
    string = ""
    ii = 1
    for i in file:
        #print(i)
        if (i.find("-") != -1):
            string += " " + "-" * width + " \n"
        elif (i.find("|") != -1):
            for iii in range(width):
                if (i[0] == "|"):
                    string += "|"
                else:
                    string += " "
                string += " " * width
                if (i[-2] == "|"):
                    string += "|"
                else:
                    string += " "
                string += "\n"
            ii += width - 1
        else:
            string += " " * width_total + "\n"
        if (ii % height_total == 0):
            numbers.append(string)
            string = ""
        ii += 1

    for i in numbers:
        #print(i.replace(" ","."))
        blub.append(i.split("\n"))
    return blub

def print_numbers():
    output = []
    string = ""
    for i in range(height_total):
        for ii in range(len(number)):
            if ii != len(number)-1:
                string += numbers[int(number[ii])][i] + " "
            else:
                string += numbers[int(number[ii])][i]
        print(string)
        string = ""

numbers = define_numbers()
print_numbers()
