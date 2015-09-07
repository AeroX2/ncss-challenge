#!/bin/env python3

class Matrix:
    def __init__(self, m, n):
        """Initialises (with zeros) a matrix of dimensions m by n."""
        self.rows = m
        self.cols = n
        self.matrix = [[0 for c in range(n)] for r in range(m)] 

    def __str__(self):
        """Returns a string representation of this matrix as integers in the form:
          a b c
          d e f
          g h i
        Used as follows: s = str(m1)
        """
        string = ""
        for col in self.matrix:
            string += " ".join(str(row) for row in col) + "\n"
        return string.strip()

    def get(self, key):
        """Returns the (i,j)th entry of the matrix, where key is the tuple (i, j)
        Used as follows: x = matrix.get((0,0))
        * raises IndexError if (i,j) is out of bounds
        """
        if key[0] < 0 or key[1] < 0: raise IndexError
        return self.matrix[key[0]][key[1]]

    def set(self, key, data):
        """Sets the (i,j)th entry of the matrix, where key is the tuple (i, j)

        and data is the number being added.
        Used as follows: matrix.set((0,0), 1)
        * raises IndexError if (i,j) is out of bounds
        * raises TypeError if data is not an integer
        """
        if not isinstance(data, int): raise TypeError
        if key[0] < 0 or key[1] < 0: raise IndexError
        self.matrix[key[0]][key[1]] = data

    def add(self, other):
        """Adds self to another Matrix or integer, returning a new Matrix.

        This method should not modify the current matrix or other.
        Used as follows: m1.add(m2) => m1 + m2
        or: m1.add(3) => m1 + 3
        * raises TypeError if other is not a Matrix object or an integer
        * raises ValueError if the other Matrix does not have the same dimensions
        """
        newmatrix = Matrix(self.rows, self.cols)
        if not isinstance(other, Matrix) and not isinstance(other, int): raise TypeError
        if isinstance(other,Matrix): 
            if self.cols != other.cols or self.rows != other.rows: raise ValueError

        for row in enumerate(self.matrix):
            for col in enumerate(row[1]):
                key = (row[0],col[0])
                if isinstance(other, int): newmatrix.set(key,self.get(key)+other)
                else: newmatrix.set(key,self.get(key)+other.get(key))
        return newmatrix

    def mul(self, other):
        """Multiplies self with another Matrix or integer, returning a new Matrix.

        This method should not modify the current matrix or other.
        Used as follows: m1.mul(m2) m1 x m2 (matrix multiplication, not point-wise)
        or: m1.mul(3) => m1*3
        * raises TypeError if the other is not a Matrix object or an integer
        * raises ValueError if the other Matrix has incorrect dimensions
        """
        newmatrix = Matrix(self.rows, self.cols)

        if isinstance(other, int): 
            for row in enumerate(self.matrix):
                for col in enumerate(row[1]):
                    key = (row[0],col[0])
                    newmatrix.set(key,self.get(key)*other)
        elif isinstance(other, Matrix):
            if self.cols != other.rows: raise ValueError
            for y1 in enumerate(self.matrix):
                for x1 in enumerate(y1[1]):
                    addition = 0
                    for x2 in enumerate(other.matrix):
                        key1 = (y1[0],x2[0])
                        key2 = (x2[0],x1[0])
                        addition += self.get(key1) * other.get(key2)
                    key3 = (y1[0],x1[0])
                    newmatrix.set(key3,addition)

        else:
            raise TypeError
        return newmatrix

matrix1 = Matrix(4,3)
matrix1.set((0,0),7)
matrix1.set((0,1),2)
matrix1.set((0,2),5)
matrix1.set((1,0),3)
matrix1.set((1,1),0)
matrix1.set((1,2),4)
matrix1.set((2,0),2)
matrix1.set((2,1),6)
matrix1.set((2,2),3)
matrix1.set((3,0),4)
matrix1.set((3,1),3)
matrix1.set((3,2),1)

print(str(matrix1))
print()
print(matrix1.get((2,1)))
print()
print(str(matrix1.add(6)))
print()
print(str(matrix1.mul(6)))
print()

matrix1 = Matrix(2,2)
matrix2 = Matrix(2,2)
matrix1.set((0,0),7)
matrix1.set((0,1),2)
matrix1.set((1,0),3)
matrix1.set((1,1),0)
matrix2.set((0,0),1)
matrix2.set((0,1),3)
matrix2.set((1,0),4)
matrix2.set((1,1),5)
print(str(matrix1))
print()
print(str(matrix2))
print(str(matrix1.mul(matrix2)))
