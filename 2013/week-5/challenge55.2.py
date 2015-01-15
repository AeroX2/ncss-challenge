from node import Node
import re

class ParseException(Exception):
    pass

class Operation:
	left = None
	right = None
	text = ""
	type = ""
	label = ""
	number = 0
	condition = ""

	def __str__(self):
		if self.type == "OR" or self.type == "AND":
			return "({0} {1} {2})".format(self.left, self.type, self.right)
		if self.type == "NWH" or self.type == "PWH":
			return "({0} {1})".format(self.type, self.left)
		if self.type == "AN":
			return "({0})".format(self.type)
		if self.type == "NWL":
			return "({0} {1} {2} {3})".format(self.condition, self.number, self.type, self.label)
		if self.type == "N":
			return "({0} {1} {2})".format(self.condition, self.number, self.type)
		if self.type == "NL" or self.type == "L":
			return "({0} {1})".format(self.type, self.label)
		return "Oops " + self.type

conditions = []


class Graph:
	def __init__(self, label, filename):
		self.label = label
		self.nodes = []
		if (filename != None):
			self.load(filename)

	def size(self):
		return len(self.nodes)
	
	def load(self, filename):
		file = open(filename)
		file_text = file.read().strip().split("\n\n")
		for line in file_text[0].split("\n"):
			id = line.split(": ")[0]
			label = line.split(": ")[1]
			new_node = Node(id, label)

			for node in self.nodes:
				if (new_node.id == node.id):
					raise ValueError
			self.nodes.append(new_node)
				

		for line in file_text[1].split("\n"):
			line = line.split(":")
			id1 = line[0]
			label = line[1] if line[1] != "" else None 
			id2 = line[2]
			self.get_node(id1).add_neighbour(self.get_node(id2),label)

	def output(self):
		for node in self.nodes:
			outputid = {}
			outputstring = "({}: {}) [".format(node.id, node.label)
			for neighbour in node.neighbours.keys():
				for nodedd in node.neighbours[neighbour]:
					outputid[nodedd.id] = neighbour if neighbour != None else ""
			
			for i in sorted(outputid):
				outputstring += "{}:{}, ".format(i,outputid[i])
			print(outputstring.strip(", ") + "]")

	def get_node(self, id):
		print(id)
		for node in self.nodes:
			if (node.id == id):
				return node
		raise ValueError

	def degrees_of_separation(self, n1, n2):
		node1 = self.get_node(n1)
		node2 = self.get_node(n2)
		paths = [[node1]]

		while (paths):
			current_path = paths.pop(0)
			if (current_path[-1] == node2):
				return len(current_path)-1
			for direction in current_path[-1].get_neighbours(None):
				if (direction not in current_path):
					new_path = list(current_path)
					new_path.append(direction)
					paths.append(new_path)
		return -1

	def graph_search(self, node, query):
		self.current_node = node
		data = self.replaceBrackets(query)    
		root = self.buildTree(data)
		return sorted(self.searchTree(root), key=lambda x:x.id)

	def replaceBrackets(self, data):
		while True:
			match = re.search(r"\(([^\(\)]*)\)", data)
			if match:
				data = data[:match.start()] + '##' + str(len(conditions)) + data[match.end():]
				conditions.append(match.group(1))
			else:
				break
		return data

	def buildTree(self, data):
		match = re.match(r" *NEIGHBOURS WHO HAVE (.*)", data)
		if match:
			operation = Operation()
			operation.left = self.buildTree(match.group(1))
			operation.type ="NWH"
			return operation
		match = re.match(r"ALL NEIGHBOURS", data)
		if match:
			operation = Operation()
			operation.type ="AN"
			return operation
		match = re.match(r" *PEOPLE WHO HAVE (.*)", data)
		if match:
			operation = Operation()
			operation.left = self.buildTree(match.group(1))
			operation.type ="PWH"
			return operation
		match = re.search(r" OR ", data)
		if match:
			operation1 = self.buildTree(data[:match.start()])
			operation2 = self.buildTree(data[match.end():])
			operation = Operation()
			operation.left = operation1
			operation.right = operation2
			operation.type = "OR"
			return operation
		match = re.search(r" AND ", data)
		if match:
			operation1 = self.buildTree(data[:match.start()])
			operation2 = self.buildTree(data[match.end():])
			operation = Operation()
			operation.left = operation1
			operation.right = operation2
			operation.type = "AND"
			return operation
		match = re.match(r"##([0-9]*)", data)
		if match:
			return self.buildTree(conditions[int(match.group(1))])
		match = re.match(r" *(EXACTLY|LESS THAN|MORE THAN) *([0-9]+) *(NEIGHBOURS WITH LABEL) *([^ ]+) *", data)
		if match:
			operation = Operation()
			operation.label = match.group(4)
			operation.number = int(match.group(2))
			operation.condition = match.group(1)
			operation.type ="NWL"
			return operation
		match = re.match(r" *(EXACTLY|LESS THAN|MORE THAN) *([0-9]+) *(NEIGHBOURS) *", data)
		if match:
			operation = Operation()
			operation.number = int(match.group(2))
			operation.condition = match.group(1)
			operation.type ="N"
			return operation
		match = re.match(r" *([0-9]+) *DEGRESS OF SEPARATION FROM ME *", data)
		if match:
			operation = Operation()
			operation.number = int(match.group(2))
			operation.type ="DOS"
			return operation
		match = re.match(r" *NEIGHBOUR LABEL *([^ ]+) *", data)
		if match:
			operation = Operation()
			operation.label = match.group(1)
			operation.type ="NL"
			return operation
		match = re.match(r" *LABEL *([^ ]+) *", data)
		if match:
			operation = Operation()
			operation.label = match.group(1)
			operation.type ="L"
			return operation
		raise ParseException

	def searchTree(self, condition):
		if (condition.type == "NWH"):
			result = self.intersect(self.getAllNeighbours(), self.searchTree(condition.left))
		elif (condition.type == "PWH"):
			result = self.searchTree(condition.left)
		elif (condition.type == "AN"):
			result = self.getAllNeighbours()
		elif (condition.type == "AND"):
			result = self.intersect(self.searchTree(condition.left), self.searchTree(condition.right))
		elif (condition.type == "OR"):
			result = self.join(self.searchTree(condition.left), self.searchTree(condition.right))
		elif (condition.type == "NWL"):
			result = self.getNeighboursWithLabel(condition.condition, condition.number, condition.label)
		elif (condition.type == "N"):
			result =  self.getNeighbours(condition.condition, condition.number)
		elif (condition.type == "NL"):
			result =  self.getNeighboursLabel(condition.label)
		elif (condition.type == "L"):
			result = self.getLabel(condition.label)
		elif (condition.type == "DOS"):
			result =  self.getDegreesOfSeparation(condition.number)
		else:
			result = []
		print("condition = " + str(condition))
		for i in result:
			print(str(i))
		return result

	def intersect(self, list1, list2):
		union = set()
		for i in list1:
			if i in list2:
				union.add(i)
		return list(union)

	def join(self, list1, list2):
		union = set()
		for i in list1:
			union.add(i)
		for i in list2:
			union.add(i)
		return list(union)
		
	# comply with AN
	def getAllNeighbours(self):
		return self.get_all_nodes(self.current_node)

	# comply with EXACTLY|LESSTHAN\MORETHAN num NEIGHBOURS WITH LABEL label
	def getNeighboursWithLabel(self, condition, number, label):
		return self.get_condition_neighbour(condition, number, label)

	# comply with EXACTLY|LESSTHAN\MORETHAN num NEIGHBOURS
	def getNeighbours(self, condition, number):
		return self.get_condition_neighbour(condition, number, None)

	# comply with NEIGHBOURS WITH LABEL label
	def getNeighboursLabel(self, label):
		return self.get_neighbour_nodes_with_label(label)

	# comply with LABEL label
	def getLabel(self, label):
		return self.get_nodes_with_label(label)

	# comply with PWH num DEGREES OF SEPARATION FROM ME
	def getDegreesOfSeparation(self, number):
		return self.degrees_of_separation(self.current_node, number)
								
	def get_nodes_with_label(self, label):
		nodes = set()
		for node in self.nodes:
			if node.label == label:
				nodes.add(node)
		return list(nodes)

	def get_neighbour_nodes_with_label(self, label):
		nodes = set()
		for node in self.nodes:
			if len(node.get_neighbours(label)) > 0:
				nodes.add(node)
		return list(nodes)

	def get_condition_neighbour(self, condition, number, label):
		nodes = set()
		for node in self.nodes:
			result = node.get_neighbours(label)
			if (condition == "EXACTLY"):
				if (len(result) == number):
					nodes.add(node)
			elif (condition == "LESS THAN"):
				if (len(result) < number):
					nodes.add(node)	
			elif (condition == "MORE THAN"):
				if (len(result) > number):
					nodes.add(node)
		return list(nodes)

	def get_all_nodes(self, root):
		return root.get_neighbours(None)

	def get_nodes_degrees(self, node1, number):
		nodes = set()
		for node2 in self.nodes:
			if (self.degrees_of_separation(node1, node2) == number):
				nodes.add(node2)
		return list(nodes)

graph = Graph("graph","input.txt")
#results = graph.graph_search(graph.get_node("1"),"NEIGHBOURS WHO HAVE LABEL Bob")
results = graph.graph_search(graph.get_node("0"),"NEIGHBOURS WHO HAVE NEIGHBOUR LABEL friend AND MORE THAN 2 NEIGHBOURS")
#results = graph.graph_search(graph.get_node("1"),"NEIGHBOURS WHO HAVE ( EXACTLY 1 NEIGHBOURS WITH LABEL father OR LABEL Bob ) AND LESS THAN 10 NEIGHBOURS")
for result in results:
	print(result.label)
