#!/bin/env python3
import re
from collections import deque

class Node:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self,child):
        self.children.append(child)
    
    def get_children(self):
        return self.children

    def __eq__(self, other):
        if isinstance(other,Node):
            if self.label == other.label:
                return True
        return False

    def __str__(self):
        string = self.label+"\n"
        for child in self.children:
            string += " "+child.label+"\n"
        return string

    def __repr__(self):
        return self.label
        
    def copy(self):
        new_node = Node(self.label)
        new_node.children = self.children.copy()
        return new_node

def bfs(start, end, tree):
    todo = deque()
    visited = set()
    if start in tree:
        todo.appendleft(tree[start])
    while todo:
        node = todo.pop()
        if node.label in visited: continue
        visited.add(node.label)

        if node.label == end:
            return True

        for child in node.get_children():
            if child.label not in visited:
                todo.appendleft(child)
    return False


config = input("Enter configuration: ")
tree = {}

size = 400
config = ' '.join(['{}_{}->{}_{}'.format(i, j, x, y) for i in range(size) for j in range(size) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= x < size and 0 <= y < size])
compiled = re.compile(r"(\w+?)(<?->?)(\w+)")
for pair in compiled.finditer(config):
    left = pair.group(1)
    middle = pair.group(2)
    right = pair.group(3)

    if left not in tree:
        left_node = Node(left)
        tree[left] = left_node
    if right not in tree:
        right_node = Node(right)
        tree[right] = right_node

    if middle == "<-":
        tree[right].add_child(tree[left])
    if middle == "->":
        tree[left].add_child(tree[right])
    if middle == "<->":
        tree[left].add_child(tree[right])
        tree[right].add_child(tree[left])

query = input("Query: ")
while query:
    query = query.split("->")
    if bfs(query[0],query[1],tree):
        print("Connected!")
    else:
        print("No connection.")
    query = input("Query: ")
