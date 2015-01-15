input_numbers = input("Number: ")
numbers = []
why = True

for i in range(9):
    numbers.append(input_numbers.count(str(i)))

if (len(input_numbers) < 10):
    for i in range(len(input_numbers)):
        if (int(input_numbers[int(i)]) != numbers[int(i)]):
            why = False
else:
    why = False

if (why):
    print(input_numbers + " is autobiographical")
else:
    print(input_numbers + " is not autobiographical")
