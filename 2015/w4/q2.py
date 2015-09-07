#!/bin/env python3
# This is a copy of the original code in program.py in case you delete it.

class Matrix:
    def __init__(self, m, n):
        """
        Initialises a matrix of dimensions m by n.
        """
        self.rows = m
        self.cols = n
        self.matrix = [[0 for c in range(n)] for r in range(m)] 

    def __getitem__(self, key):
        """
        Returns the (i,j)th entry of the matrix, where key is the tuple (i,j).
        i or j may be Ellipsis (...) indicating that the entire i-th row
        or j-th column should be selected. In this case, this method returns a
        list of the i-th row or j-th column. 
        Used as follows: x = matrix[0,0] || x = matrix[...,1] || x = matrix[0,...]
         * raises IndexError if (i,j) is out of bounds
         * raises TypeError if (i,j) are both Ellipsis
        """
        if key[0] is Ellipsis and key[1] is Ellipsis: raise TypeError
        if key[0] is Ellipsis:
            newlist = []
            for row in enumerate(self.matrix):
                newlist.append(self.matrix[row[0]][key[1]])
            return newlist
        if key[1] is Ellipsis:
            return list(self.matrix[key[0]])
        if key[0] < 0 or key[1] < 0: raise IndexError
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key, data):
        """
        Sets the (i,j)th entry of the matrix, where key is the tuple (i,j)
        and data is the number being added. 
        One of i or j may be Ellipsis (...) indicating that the entire i-th row
        or j-th column should be replaced. In this case, data should be a list 
        or a tuple of integers of the same dimensions as the equivalent matrix 
        row or column. This method then replaces the i-th row or j-th column 
        with the contents of the list or tuple
        Used as follows: matrix[0,0] = 1 || matrix[...,1] = [4,5,6] || matrix[0,...] = (1,2)
         * raises IndexError if (i,j) is out of bounds
         * raises TypeError if (i,j) are both Ellipsis
         * if i and j are integral, raises TypeError if data is not an integer
         * if i or j are Ellipsis, raises TypeError if data is not a list or tuple of integers
         * if i or j are Ellipsis, raises ValueError if data is not the correct size
        """
        if key[0] is Ellipsis and key[1] is Ellipsis: raise TypeErro
        if key[0] is Ellipsis or key[1] is Ellipsis:
            if not isinstance(data, list) and not isinstance(data,tuple): raise TypeError
            for i in data:
                if not isinstance(i, int):
                    raise TypeError
        if key[0] is Ellipsis:
            if len(data) != self.cols: raise ValueError
            for row in enumerate(self.matrix):
                self.matrix[row[0]][key[1]] = data[row[0]]
            return
        if key[1] is Ellipsis:
            if len(data) != len(self.matrix[key[0]]): raise ValueError
            self.matrix[key[0]] = data
            return
        if not isinstance(data, int): raise TypeError
        if key[0] < 0 or key[1] < 0: raise IndexError
        self.matrix[key[0]][key[1]] = data

    def __iadd__(self, other):
        self = self.add(other)
        return self

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __str__(self):
        """
        Returns a string representation of this matrix in the form:
          a b c
          d e f
          g h i
        Used as follows: s = str(m1)
        """
        string = ""
        for col in self.matrix:
            string += " ".join(str(row) for row in col) + "\n"
        return string.strip()

    def transpose(self):
        """
        Returns a new matrix that is the transpose of this Matrix object
        This method should not modify the current matrix.
        """ 
        newmatrix = Matrix(self.cols,self.rows)
        for row in enumerate(self.matrix):
            for col in enumerate(row[1]):
                newmatrix[col[0],row[0]] = self[row[0],col[0]]
        return newmatrix

    def copy(self):
        """
        Returns a new Matrix that is an exact and independent copy of this one
        This method should not modify the current matrix.
        """
        newmatrix = Matrix(self.cols, self.rows)
        newmatrix.matrix = [row[:] for row in self.matrix]
        return newmatrix

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

        if isinstance(other, int): 
            newmatrix = Matrix(self.rows, self.cols)
            for row in enumerate(self.matrix):
                for col in enumerate(row[1]):
                    key = (row[0],col[0])
                    newmatrix.set(key,self.get(key)*other)
        elif isinstance(other, Matrix):
            newmatrix = Matrix(self.rows, other.cols)
            if self.cols != other.rows: raise ValueError
            for y1 in enumerate(newmatrix.matrix):
                #print(y1[0],"row")
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


#matrix1 = Matrix(4,3)
#matrix1[0,0]=7
#matrix1[0,1]=2
#matrix1[0,2]=5
#matrix1[1,0]=3
#matrix1[1,1]=0
#matrix1[1,2]=4
#matrix1[2,0]=2
#matrix1[2,1]=6
#matrix1[2,2]=3
#matrix1[3,0]=4
#matrix1[3,1]=3
#matrix1[3,2]=1
#
#print(str(matrix1))
#print()
#print(matrix1[2,1])
#print()
#print(str(matrix1+6))
#print()
#print(str(matrix1*6))
#print()
#
##matrix1 = Matrix(2,2)
#matrix2 = Matrix(2,2)
##matrix1[0,0]=7
##matrix1[0,1]=2
##matrix1[1,0]=3
##matrix1[1,1]=0
#matrix2[0,0]=1
#matrix2[0,1]=3
#matrix2[1,0]=4
#matrix2[1,1]=5
#print(str(matrix1))
#print()
#print(str(matrix2))
#print()
##print(str(matrix1 * matrix2))
#matrix3 = matrix2.copy()
#matrix3[0,0] = 0
#print(matrix2)
#print(matrix3)
#matrix4 = Matrix(1,2)
#matrix5 = Matrix(2,2)
#matrix4[0,0] = 1
#matrix4[0,1] = 2
#print(matrix4)
#print(matrix4.transpose())
#matrix5[0,0] = 7
#matrix5[0,1] = 2
#matrix5[1,0] = 3
#matrix5[1,1] = 0
#print(matrix5)
#print(matrix5.transpose())
#print()
#print()
#
#print(matrix5[...,1])
#print(matrix5[1,...])
#matrix5[...,1] = [1,1]
#matrix5[1,...] = [1,1]
#print(matrix5[...,1])
#print(matrix5[1,...])
#print(str(matrix5))
##print(matrix1[...,...])
##matrix5[1,...] = 2
#print(str(matrix5))
#matrix5 += 3
#print(str(matrix5),"skdjdsk")
#
#
#matrix1 = Matrix(4,3)
#matrix1.set((0,0),7)
#matrix1.set((0,1),2)
#matrix1.set((0,2),5)
#matrix1.set((1,0),3)
#matrix1.set((1,1),0)
#matrix1.set((1,2),4)
#matrix1.set((2,0),2)
#matrix1.set((2,1),6)
#matrix1.set((2,2),3)
#matrix1.set((3,0),4)
#matrix1.set((3,1),3)
#matrix1.set((3,2),1)
#
#print(str(matrix1))
#print()
#print(matrix1.get((2,1)))
#print()
#print(str(matrix1.add(6)))
#print()
#print(str(matrix1 * 6))
#print()
#
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
print(str(matrix1 * matrix2))

#print(str(Matrix(2,2) * Matrix(2,2)))
#print(str(Matrix(2,2) * Matrix(2,3)))
#print(str(Matrix(3,1) * Matrix(1,3)))
