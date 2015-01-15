#!/usr/bin/python3
import math

class Coin:
	parent = None
	children = []
	num = 0

	def __init__(self, num, parent):
		self.num = num
		self.parent = parent
		self.children = []

	def __repr__(self):
		return "Num: " + str(self.num)# + str(self.children)

def addChildren(coin):
	if (coin.num < (math.floor(coin.num / 2) + math.floor(coin.num / 3) + math.floor(coin.num / 4))):
		current_children = []
		current_children.append(Coin(math.floor(coin.num / 2),coin))
		current_children.append(Coin(math.floor(coin.num / 3),coin))
		current_children.append(Coin(math.floor(coin.num / 4),coin))
		coin.children = current_children

def convert_grokcoin(num):
	parents = [Coin(num, None)]
	main_parent = parents[0]

	done = False
	while not done:
		done = True
		for parent in parents:
			addChildren(parent)
			if parent.children:
				done = False
				parents.remove(parent)
				for child in parent.children:
					parents.append(child)
			#print(parents)
	#print(main_parent)
	
	parents = [main_parent]
	for parent in parents:
		for child in parent.children:
			parents.append(child)
	#print(parents)

	while len(parents) > 1:
		for parent in reversed(parents):
			#print(str(parents) + " :Hi")
			if parent != main_parent:
				total_sum = 0
				for child in parent.parent.children:
					total_sum += child.num
					parents.remove(child)
				#print(total_sum)
				parent.parent.num = total_sum if total_sum > 0 else parent.parent.num
				parent.parent.children = []

	return main_parent.num

#print(convert_grokcoin(18))
#print(convert_grokcoin(17))
print(convert_grokcoin(24))
print(convert_grokcoin(25))
print(convert_grokcoin(42))
#print(convert_grokcoin(50))
#print(convert_grokcoin(12))
print(convert_grokcoin(10000))
print(convert_grokcoin(100000000000000))
#print(convert_grokcoin(4225970322942321237549))
#print(convert_grokcoin(1203985721309857213098572310598312750931285712309857231059832715098321750123985230198572310589723059823175098231750912387502319857231098572310985172))
