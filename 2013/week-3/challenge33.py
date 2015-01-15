class Node:
  def __init__(self, id, label):
    """
    Initialise a node with a given id and label
    """
    self.id = str(id)
    self.label = str(label)
    self.neighbours = {}
    pass  # TODO

  def __str__(self):
    """
    Return a string representation of the node
    as "(id: label), e.g. (4: Greg)"
    """
    return "({}: {})".format(self.id, self.label) # TODO

  def add_neighbour(self, neighbour, label):
    """
    Add a neighbour to this node with
    a given edge label
    e.g. x.add_neighbour(y, "brother")
    """
    try:
        self.neighbours[label].append(neighbour) 
    except KeyError:
        self.neighbours[label] = [neighbour]
    pass  # TODO

  def get_neighbours(self, label):
    """
    Returns a list of node objects that are
    neighbours of this node with a given edge label
    Return an empty list if there are no neighbours
    with the given label
    Return all neighbours if label is None
    e.g. x.get_neighbours("brother")
    """
    
    if label != None:
        try:
            return self.neighbours[label]
        except KeyError:
            return []
    temp_list = []
    for i in self.neighbours.values():
        for ii in i:
            temp_list.append(ii)
    return temp_list

  def degree(self, label):
    """
    Returns the number of neighbours with a given
    edge label
    Return total number of neighbours
    if label is None
    """
    if label != None:
        try:
            return len(self.neighbours[label])
        except KeyError:
            return 0
    else:
        temp_number = 0
        for i in self.neighbours.values():
            temp_number += len(i)
        return temp_number

  def has_neighbour(self, node, label):
    """
    Returns True if this node has 'node' as a
    neighbour with a given label, False otherwise
    Returns True if this node has 'node' as a
    neighbour if label is None, False otherwise
    """
    if label != None:
        try:
            if (node in self.neighbours[label]):
                return True
            else:
                return False
        except KeyError:
            return False
    else:
        for i in self.neighbours.values():
            if (node in i):
                return True
        return False

n1 = Node(1, "1")  
n1.add_neighbour(Node(2, "2"), "r1")  
n1.add_neighbour(Node(3, "3"), "r1")  
n1.add_neighbour(Node(4, "4"), "r2")  
print(n1.degree(None))  # Should be 3  
print(n1.degree("r1"))  # Should be 2  
print(n1.degree("r2"))  # Should be 1  
print(n1.degree("r3"))  # Should be 0

print(n1.get_neighbours(None))  # Should return a list of the 3 neighbour nodes  
print(n1.get_neighbours("r1"))  # Should return a list of the first two nodes  
print(n1.get_neighbours("r2"))  # Should return a list of the last node  
print(n1.get_neighbours("r3"))  # Should return []

n5 = Node(5, "5")  
n1.add_neighbour(n5, "r2")  
print(n1.has_neighbour(n5, None))  # Should be True  
print(n1.has_neighbour(n5, "r2"))  # Should be True  
print(n1.has_neighbour(n5, "r1"))  # Should be False  
print(n1.has_neighbour(None, "r2"))  # Should be False 
print(n1.has_neighbour(None, "6666oddfuturebro"))  # Should be False 
