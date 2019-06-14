import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 2:
            det = self[0][0]*self[1][1] - self[0][1]*self[1][0]
        elif self.h == 1:
            det = 1
        
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        s=0
        for i in range(0,self.h):
            for j in range(0,self.w):
                if i==j:
                    s=s+self[i][j]
        
        return s

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
            
        inverse=[]

        # TODO - your code here
        if self.h == 1:
            inverse.append([1 / self[0][0]])
        elif self.h == 2:
            
            # If the matrix is 2x2, check that the matrix is invertible
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self[0][0]
                b = self[0][1]
                c = self[1][0]
                d = self[1][1]
                
                factor = 1 / (a * d - b * c)
            
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        row=[]
        Tr=[]
        for j in range(0,self.w):
            row=[]
            for i in range(0,self.h):
                row.append(self[i][j])
            
            Tr.append(row)
        
        return Matrix(Tr)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        row=[]
        Add=[]
        for i in range(0,self.h):
            row=[]
            for j in range(0,self.w):
                row.append(self[i][j]+other[i][j])

            Add.append(row)
        return Matrix(Add)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        row=[]
        Neg=[]
        for i in range(0,self.h):
            row=[]
            for j in range(0,self.w):
                row.append(-self[i][j])

            Neg.append(row)
        return Matrix(Neg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        row=[]
        Sub=[]
        for i in range(0,self.h):
            row=[]
            for j in range(0,self.w):
                row.append(self[i][j]-other[i][j])

            Sub.append(row)
        return Matrix(Sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        product = []
    
        transposeB = other.T()
        
        for r1 in range(0,self.h):
            new_row = []
            for r2 in range(0,transposeB.h):
                rr1 = self[r1]
                rr2 = transposeB[r2]
                result = 0
                for i in range(0,len(rr1)):
                    result += rr1[i] * rr2[i]
                
                new_row.append(result)

            product.append(new_row)

        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            #pass
            #   
            # TODO - your code here
            #
            row=[]
            rnul=[]
            for i in range(0,self.h):
                row=[]
                for j in range(0,self.w):
                    row.append(other*self[i][j])
                rnul.append(row)
                
        return Matrix(rnul)