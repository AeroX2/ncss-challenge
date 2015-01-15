import string
from collections import deque

def equal_size(l):
	largest = 0
	for i in l:
		largest = max(len(i),largest)
	for i in l:
		while (len(i) < largest):
			i.append(0)
	return largest

def plus(queue):
	add1 = queue.pop()
	add2 = queue.pop()
	equal_size([add1,add2])

	for i in range(len(add1)):
		add1[i] += add2[i]
	queue.append(add1)

	return queue

def minus(queue):
	minus1 = queue.pop()
	minus2 = queue.pop()
	equal_size([minus1,minus2])

	for i in range(len(minus1)):
		minus2[i] -= minus1[i]
	queue.append(minus2)

	return queue

def multiply(queue):
	multiply1 = queue.pop()
	multiply2 = queue.pop()

	test = [0] * (len(multiply2) + len(multiply1))
	for i in range(len(multiply2)):
		for ii in range(len(multiply1)):
			test[i+ii] += multiply2[i]*multiply1[ii]

#	print("multiply " + str(multiply1) + " by " + str(multiply2) + " = " + str(test)) 
	queue.append(test)

	return queue

def power(queue):
	power = queue.pop()[0]
	element = queue.pop()
	if (power == 0):
		queue.append([1,0])
		#print("power " + str(element) + " by " + str(power) + " = " + str([1]))
		#print(queue) 
		return queue
	result = element
	for i in range(1,power):
		test = [0] * (len(element) + len(result))
		for i in range(len(element)):
			for ii in range(len(result)):
				test[i+ii] += element[i]*result[ii]
		result = test
	#print("power " + str(element) + " by " + str(power) + " = " + str(result)) 
	queue.append(result)

	return queue

def do_operation(operation,queue):
	if (operation == "+"): queue = plus(queue)
	elif (operation == "-"): queue = minus(queue)
	elif (operation == "*"): queue = multiply(queue)
	elif (operation == "^"): queue = power(queue)
	return queue

def check_operation(operation):
	operations = ["+","-","*","^"]
	if (operation in operations): return True
	return False

def RPN(operations):
	result = []
	queue = deque()
	for operation in operations:
		#print(queue)
		if (not check_operation(operation)):
			if (operation in string.ascii_letters):
				queue.append([0,1])
			else:
				queue.append([int(operation),0])
		else:
			queue = do_operation(operation,queue)
		#print(queue)
	
	if (len(queue) < 2):
		result = queue[0]
	else:
		print("Error invalid syntax for input")
		raise TypeError
	return result

def print_RPN(results):
	output = ""
	results_test = results[2:]
#	results_test.reverse()
	for result in range(len(results_test)-1,-1,-1):
		#print(results_test)
		#print(result)
		if (results_test[result] > 0):
			output += " + x^" + str(result+2) if (results_test[result] == 1) else " + "+str(results_test[result]) + "x^" + str(result+2)
		elif (results_test[result] < 0):
			output += " - x^" + str(result+2) if (results_test[result] == -1) else " - "+str(-results_test[result]) + "x^" + str(result+2)

	#Single pronumeral
	if (results[1] > 0):
		output += " + x" if (results[1] == 1) else " + " + str(results[1]) + "x"
	elif (results[1] < 0):
		output += " - x" if (results[1] == -1) else " - " + str(-results[1]) + "x"

	#Digit
	if (results[0] > 0):
		output += " + " + str(results[0])
	elif (results[0] < 0):
		output += " - " + str(-results[0])

	if (output[:3] == " + "):
		output = output[3:]
	elif (output[:3] == " - "):
		output = "-"+output[3:]

	if (not output):
		output += "0"
	print(output.strip("+ "))


input = input("RPN: ").strip()
#input = "x 2 ^ 3 - 1 2 x * - *"
#input = "x 2 ^ 0 *"
#input = "2 x 3 + 2 ^ * 4 x 1 - x 2 + * * + 3 x 1 + * + 4 x * - 6 +"
#input = "3 2 +"
#input = "5 x 2 * 3 x 2 ^ * + + 3 ^"
#input = "3 x + 3 + 3 + 9 + 7 + 6 - x - 7 - 2 x +"
#input = "2 x + 2 x + -"
#input = "x 2 ^"
#input = "23 x *"
#input = "1 x + 5 ^"
operations = input.split(" ")
print_RPN(RPN(operations))
