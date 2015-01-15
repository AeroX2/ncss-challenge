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
		"""
		Initialise a graph with a given label.
		If filename is not None, load the graph from the file
		"""
		self.label = label
		self.nodes = {}
		if filename:
			self.load(filename)

	def load(self, filename):
		"""
		Load the graph from the given filename.
		Raise ValueError if a node with a duplicate
		id is added or if a relationship between
		nonexisting nodes is created
		"""
		nodes = True
		for line in open(filename):
			line = line.strip()
			if not line:
				nodes = False
				continue
			if nodes:
				id, label = line.split(":")
				self._add_node(id.strip(), label.strip())
			else:
				from_id, label, neighbour_id = line.split(":")
				self._add_neighbour(from_id, label, neighbour_id)

	def size(self):
		"""
		Return the number of nodes in the graph
		"""
		return len(self.nodes)

	def _add_node(self, id, label):
		if id in self.nodes:
			raise ValueError("Node with that id already exists")
		self.nodes[id] = Node(id, label)

	def _add_neighbour(self, from_id, label, neighbour_id):
		from_node = self.get_node(from_id)
		neighbour_node = self.get_node(neighbour_id)
		if label:
			from_node.add_neighbour(neighbour_node, label)
		else:
			from_node.add_neighbour(neighbour_node, None)

	def output(self):
		"""
		Prints the graph with nodes listed in sorted order
		of ids with their neighbours
		e.g.
		(0: Bob) [1, 2]
		(1: John) [0, 2]
		(2: Jane) [0]
		"""
		for id in sorted(self.nodes):
			node = self.nodes[id]
			print(node, end=" ")
			neighbours = []
			out = []
			for label in node.neighbours:
				for n in node.neighbours[label]:
					neighbours.append((n.id, label))
			for n, label in sorted(neighbours):
				out.append("{0}:{1}".format(n, label if label else ""))
			print("[{0}]".format(", ".join(out)))

	def degrees_of_separation(self, n1, n2):
		"""
		Returns the minimum degrees of separation from
		n1 to n2 where each x on the path between n1
		and n2 fulfills the has_neighbour relationship.
		Return -1 if n1 and n2 are not connected.
		Raise ValueError if either n1 or n2 is not in
		this graph
		e.g. graph.degrees_of_separation(x, y)
		"""
		n1 = self.get_node(n1)
		n2 = self.get_node(n2)
		todo = [(0, n1)]
		explored = set()
		while todo:
			dist, node = todo.pop(0)
			if node.id == n2.id and node.label == n2.label:
				return dist
			else:
				explored.add(node.id)
				for n in node.get_neighbours(None):
					if n.id not in explored:
						todo.append((dist + 1, n))
		return -1


	def get_node(self, id):
		"""
		Returns the node with the given id
		Raise ValueError if no node with the id exists
		"""
		if id in self.nodes:
			return self.nodes[id]
		else:
			raise ValueError("Given id is not in graph")

	def graph_search(self, node, query):
		self.current_node = node
		self.start = False
		self.nwh = None
		data = self.replaceBrackets(query)    
		root = self.buildTree(data, "")
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

	def buildTree(self, data, previous):
		match = re.match(r"^\s*NEIGHBOURS\s+WHO\s+HAVE\s+(.*)$", data, re.IGNORECASE)
		if match:
			if self.start:
				raise ParseException
			self.nwh = True
			self.start = True
			operation = Operation()
			operation.left = self.buildTree(match.group(1), "NWH")
			operation.type ="NWH"
			return operation
		match = re.match(r"^\s*ALL\s+NEIGHBOURS\s*$", data, re.IGNORECASE)
		if match:
			if self.start:
				raise ParseException
			self.start = True
			operation = Operation()
			operation.type ="AN"
			return operation
		match = re.match(r"^\s*PEOPLE\s+WHO\s+HAVE\s+(.*)$", data, re.IGNORECASE)
		if match:
			if self.start:
				raise ParseException
			self.nwh = False
			self.start = True
			operation = Operation()
			operation.left = self.buildTree(match.group(1), "PWH")
			operation.type ="PWH"
			return operation
		match = re.search(r"\s+OR\s+", data, re.IGNORECASE)
		if match:
			if not self.start:
				raise ParseException
			if previous == "NWH" or previous == "PWH" or previous == "()":
				operation1 = self.buildTree(data[:match.start()], "OR")
				operation2 = self.buildTree(data[match.end():], "OR")
				operation = Operation()
				operation.left = operation1
				operation.right = operation2
				operation.type = "OR"
				return operation
			else:
				raise ParseException
		match = re.search(r"\s+AND\s+", data, re.IGNORECASE)
		if match:
			if not self.start:
				raise ParseException
			if previous == "NWH" or previous == "PWH" or previous == "OR" or previous == "()":
				operation1 = self.buildTree(data[:match.start()], "AND")
				operation2 = self.buildTree(data[match.end():], "AND")
				operation = Operation()
				operation.left = operation1
				operation.right = operation2
				operation.type = "AND"
				return operation
			else:
				raise ParseException
		match = re.match(r"^\s*##([0-9]*)\s*$", data)
		if match:
			if not self.start:
				raise ParseException
			if previous == "OR" or previous == "AND" or previous == "()":
				return self.buildTree(conditions[int(match.group(1))], "()")
			else:
				raise ParseException
		match = re.match(r"^\s*(EXACTLY|LESS\s+THAN|MORE\s+THAN)\s+([0-9]+)\s+(NEIGHBOURS\s+WITH\s+LABEL)\s+([^\s]+)\s*$", data, re.IGNORECASE)
		if match:
			if not self.start:
				raise ParseException
			operation = Operation()
			operation.label = match.group(4)
			operation.number = int(match.group(2))
			operation.condition = match.group(1)
			operation.type ="NWL"
			return operation
		match = re.match(r"^\s*(EXACTLY|LESS\s+THAN|MORE\s+THAN)\s+([0-9]+)\s+(NEIGHBOURS)\s*$", data, re.IGNORECASE)
		if match:
			if not self.start:
				raise ParseException
			operation = Operation()
			operation.number = int(match.group(2))
			operation.condition = match.group(1)
			operation.type ="N"
			return operation
		match = re.match(r"^\s*([0-9]+)\s+DEGREES\s+OF\s+SEPARATION\s+FROM\s+ME\s*$", data, re.IGNORECASE)
		if match:
			if self.nwh or not self.start:
				raise ParseException
			operation = Operation()
			operation.number = int(match.group(1))
			operation.type ="DOS"
			return operation
		match = re.match(r"^\s*NEIGHBOUR\s+LABEL\s+([^\s]+)\s*$", data, re.IGNORECASE)
		if match:
			if not self.nwh:
				raise ParseException
			operation = Operation()
			operation.label = match.group(1)
			operation.type ="NL"
			return operation
		match = re.match(r"^\s*LABEL\s+([^\s]+)\s*$", data, re.IGNORECASE)
		if match:
			if not self.nwh:
				raise ParseException
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
#		print("condition = " + str(condition))
#		for i in result:
#			print(str(i))
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
		return self.get_nodes_degrees(self.current_node, number)
	
	def get_neighbour_nodes_with_label(self, label):
		nodes = set()
		if self.nwh:
			for node in self.current_node.get_neighbours(label):
				nodes.add(node)
		else:
			for node in self.nodes.values():
				for neighbour in node.get_neighbours(label):
					nodes.add(neighbour)
#		print("get_neighbour_nodes_with_label " + label + " = " + self.printList(nodes))
		return list(nodes)

	def get_nodes_with_label(self, label):
		nodes = set()
		if self.nwh:
			for node in self.current_node.get_neighbours(None):
				if node.label == label:
					nodes.add(node)
		else:
			for node in self.nodes.values():
				if node.label == label:
					nodes.add(node)
#		print("get_nodes_with_label " + label + " = " + self.printList(nodes))
		return list(nodes)

	def get_condition_neighbour(self, condition, number, label):
		nodes = set()
		if self.nwh:
			data = self.current_node.get_neighbours(None)
		else:
			data = self.nodes.values()
		for node in data:
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
		#print("node1.id = " + str(node1.id))
		for node2 in self.nodes.values():
			#print(node2.id)
			if (self.degrees_of_separation(node1.id, node2.id) == number):
				nodes.add(node2)
		return list(nodes)

	def printList(self, x):
		result = "{"
		for item in x:
			result += item.label + ","
		return result + "}"

#graph = Graph("graph","input.txt")
#graph.output()
#results = graph.graph_search(graph.get_node("1"),"ALL NEIGHBOURS WHO HAVE LABEL Bob")
#results = graph.graph_search(graph.get_node("1"),"NEIGHBOURS WHO HAVE ALL NEIGHBOURS")
#results = graph.graph_search(graph.get_node("1"),"PEOPLE WHO HAVE 2 DEGREES OF SEPARATION FROM ME")
#results = graph.graph_search(graph.get_node("4"),"NEIGHBOURS WHO HAVE NEIGHBOUR LABEL friend AND MORE THAN 2 NEIGHBOURS")
#results = graph.graph_search(graph.get_node("4"),"NEIGHBOURS WHO HAVE LABEL John OR LABEL Jane OR (LABEL X)")
#results = graph.graph_search(graph.get_node("0"),"PEOPLE WHO HAVE 2 DEGREES OF SEPARATION FROM ME")
#for result in results:
#	print(result.label)

