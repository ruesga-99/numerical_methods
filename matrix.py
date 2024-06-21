class Matrix:
    def __init__(self, n):
        self.n = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def set_value(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.n:
            self.matrix[i][j] = value
        else:
            print("Index out of range")

    def get_value(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            return self.matrix[i][j]
        else:
            print("Index out of range")
            return None
        
    def print_mtx(self):
        for i in self.matrix:
            print(i)
        
    '''
    """ OPERATOR OVERLOADING """
    '''

    def __add__ (self, other):
        if self.n != other.n:
            raise ValueError("Matrixes must be the same order")
        
        result = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        
        return result
    
    def __sub__ (self, other):
        if self.n != other.n:
            raise ValueError("Matrixes must be the same order")
        
        result = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        
        return result
    
    def __mul__ (self, other):
        if self.n != other.n:
            raise ValueError("Matrixes must be the same order")
        
        result = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        
        return result
    
    # Used for scalar product (matrix and matrix)
    def __truediv__ (self, other):
        if self.n != other.n:
            raise ValueError("Matrixes must be the same order")
        
        result = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] * other.matrix[i][j]
        
        return result
    
    # Used for scalar product (scalar and matrix)
    def __floordiv__ (self, scalar):
        result = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j] * scalar
        
        return result


'''
    """ BASIC OPERATIONS USE CASE """
'''

A = Matrix(3)
B = Matrix(3)

# Asign values
k = 0
for i in range(3):
    for j in range(3):
        A.set_value(i, j, k)
        B.set_value(i, j, 2*k)
        k += 1

# Print Matrix
print("Matrix A:")
A.print_mtx()
print("Matrix B:")
B.print_mtx()

op = A + B
print("Matrix A + B:")
op.print_mtx()

op = A - B
print("Matrix A - B:")
op.print_mtx()

op = A * B
print("Matrix A * B:")
op.print_mtx()

op = A / B
print("Matrix A x B:")  # Matrix and Matrix (scalar product)
op.print_mtx()

op = A // 2
print("Matrix A x b:")  # Matrix and scalar (scalar product)
op.print_mtx()
