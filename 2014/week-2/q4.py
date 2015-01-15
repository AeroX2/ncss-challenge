#!/usr/bin/python3
import re
dates_file = open("ambiguous-dates.txt").read()
dates = re.findall("\d+[^0-9\n]{1}\d+[^0-9\n]{1}\d+",dates_file)
date_format = []

for date in dates:
	#y,m,d
	correct = [False,False,False]
	temp_date_format = [-1,-1,-1]
	for index in enumerate(re.split("[^0-9\n]",date)):
		number = int(index[1])
		#month must be within 1 to 12
		if (number >= 1 and number <= 12 and not correct[1]):
			temp_date_format[index[0]] = 1
			correct[1] = True
		#day must be larger then 12 to be unambigous but less then 31 to be a day
		elif (number >= 13 and number <= 31 and not correct[2]):
			temp_date_format[index[0]] = 2
			correct[2] = True
		#year larger then 32 to be unambigous
		elif (number >= 32 and not correct[0]):
			temp_date_format[index[0]] = 0
			correct[0] = True	
	if (False not in correct):
		date_format = temp_date_format
#Stupid rule for if the date is ymd
if (dates):
	if (False in correct and int(re.split("[^0-9\n]",dates[0])[0]) >= 32):
		date_format = [0,1,2]

if date_format:
	for date in dates:
		temp_string = ""
		numbers = re.split("[^0-9\n]",date)
		sorted_date = [i[0] for i in sorted(zip(numbers,date_format),key=lambda x: x[1])]
		temp_string += sorted_date[0].rjust(4,"0") + "-"
		temp_string += sorted_date[1].rjust(2,"0") + "-"
		temp_string += sorted_date[2].rjust(2,"0")
		print(temp_string)
else:
	print("No unambiguous dates found")
		
