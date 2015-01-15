#!/usr/bin/python3
import math

cache = {}
def convert_grokcoin(num):
	global cache
	if (math.floor(num / 2) + math.floor(num / 3) + math.floor(num / 4)) <= num: 
		return num
	if num not in cache: 
		cache[num] = convert_grokcoin(math.floor(num / 2)) + convert_grokcoin(math.floor(num / 3)) + convert_grokcoin(math.floor(num / 4))
	return cache[num]

