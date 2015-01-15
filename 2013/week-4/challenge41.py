# Enter your code for "Carry On" here.
def largest(a,b):
    if (a > b):
        return a
    else:
        return b

	def smallest(a,b):
		if (a < b):
			return a
		else:
			return b


	def carries(a, b):
		largest_num = str(largest(a,b))
		smallest_num = str(smallest(a,b)).zfill(len(largest_num))
		add_to_number = 0
		carry = 0

		for i in range(-1,-len(largest_num)-1,-1):
			sum_of_num = int(largest_num[i]) + int(smallest_num[i])
			if (add_to_number > 0):
				sum_of_num += add_to_number
				add_to_number = 0

			#Ummm don't look here
			if (sum_of_num != 10):
				blub1 = sum_of_num % 10
				blub2 = sum_of_num % 100
				blub3 = blub2 - blub1
			else:
				blub3 = 10

			if (blub3 >= 10):
				carry += 1
				add_to_number = int(blub3 / 10)
		return carry

	#print(str(carries(1094, 3197)) + "Carry")
	#print(str(carries(1094, 3107)) + "Carry")
	#print(str(carries(199999999999, 1)) + "Carry")
