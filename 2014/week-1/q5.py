#!/usr/bin/python
import math
def is_kaprekar(num):
	kaprekar = num == 1
	str_num = str(num ** 2)
	for i in range(len(str_num)-1):
		first_num = int(str_num[i+1:])
		second_num = int(str_num[:i+1])
		if (first_num != 0 and second_num != 0):
			if (first_num + second_num == num):
				kaprekar = True
	return kaprekar


for i in "1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999 , 17344, 22222, 38962, 77778, 82656, 95121, 99999, 142857, 148149, 181819, 187110, 208495, 318682, 329967, 351352, 356643, 390313, 461539, 466830, 499500, 500500, 533170, 100, 2, 4 , 55 , 89".split(","):
	print(is_kaprekar(int(i)))
