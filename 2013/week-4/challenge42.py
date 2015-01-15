from node import Node

class Graph:
	def __init__(self, label, filename):
		"""
		Initialise a graph with a given label.
		If filename is not None, load the graph from the file
		"""
		self.label = label
		self.nodes = []
		if (filename != None):
			self.load(filename)

		pass  # TODO

	def size(self):
		"""
		Return the number of nodes in the graph
		"""
		return len(self.nodes)  # TODO
	
	def load(self, filename):
		"""
		Load the graph from the given filename.
		Raise ValueError if a node with a duplicate
		id is added or if a relationship between
		nonexisting nodes is created
		"""
		file = open(filename)
		file_text = file.read().strip().split("\n\n")
		for line in file_text[0].split("\n"):
			id = line.split(": ")[0]
			label = line.split(": ")[1]
			new_node = Node(id, label)

			#if (not node in self.nodes):
			#	self.nodes.append(node)
			#else:
			#	raise ValueError
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
		pass

	def output(self):
		"""
		Prints the graph with nodes listed in sorted order
		of ids with their neighbours and neighbour labels
		If neighbour labels are None, print the empty
		string.
		Print empty brackets if a node has no neighbours
		e.g.
		(0: Bob) [1:son, 2:wife]
		(1: John) [0:father, 2:mother]
		(2: Jane) [0:husband, 1:son]
		(3: Greg) [1:friend]
		"""
		for node in self.nodes:
			outputid = {}
			outputstring = "({}: {}) [".format(node.id, node.label)
			for neighbour in node.neighbours.keys():
				for nodedd in node.neighbours[neighbour]:
					outputid[nodedd.id] = neighbour if neighbour != None else ""
			
			for i in sorted(outputid):
				outputstring += "{}:{}, ".format(i,outputid[i])
			print(outputstring.strip(", ") + "]")

		pass

	def degrees_of_separation(self, n1, n2):
		"""
		Returns the minimum degrees of separation from
		n1 to n2, where n1 and n2 are ids.
		Each x on the path between n1
		and n2 fulfills the has_neighbour relationship.
		Return -1 if n1 and n2 are not connected.
		Raise ValueError if either n1 or n2 is not in
		this graph
		If n2 is a neighbour of n1, then there is
		1 degree of separation.
		e.g. graph.degrees_of_separation(n1, n2)
		"""
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
			#for i in paths:
				#print ', '.join(map(str, i))
		return -1
				
	def get_node(self, id):
		"""
		Returns the node with the given id
		Raise ValueError if no node with the id exists
		"""
		for node in self.nodes:
			if (node.id == id):
				return node
		raise ValueError

graph = Graph('graph', "input.txt")
#graph = Graph('graph2', None)
#graph = Graph('graph1', "")

print(graph.get_node("0")) 
print(graph.get_node("1")) 
print(graph.get_node("2"))
print(graph.size())
#print(graph.get_node(-1))
#print(graph.get_node(66))
graph.output()
print(graph.degrees_of_separation("1", "0"))
print(graph.degrees_of_separation("0", "4"))
print(graph.degrees_of_separation("0", 4))
