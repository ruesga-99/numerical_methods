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
    """ UNARY OPERATORS OVERLOADING """
    '''

    def __neg__ (self):
        neg_matrix = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                neg_matrix.set_value(i, j, -self.matrix[i][j])

        return neg_matrix

    '''
    """ COMPARISSON OPERATORS OVERLOADING """
    '''
    
    def __eq__ (self, other):
        if self.n != other.n:
            return False
        else:
            for i in range(self.n):
                for j in range(self.n):
                    if self.matrix[i][j] != other.matrix[i][j]:
                        return False
            return True
        
    def __ne__ (self, other):
        return not self == other

    '''
    """ BINARY (MATHEMATICAL) OPERATORS OVERLOADING """
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
    
    def __pow__(self, pow):
        if pow == 0:
            # Return identity matrix
            result = Matrix(self.n)
            for i in range(self.n):
                result.matriz[i][i] = 1
            return result
        
        if pow == 1:
            return self
        
        # n greater or equal to 2
        result = Matrix(self.n)
        
        for i in range(self.n):
            for j in range(self.n):
                result.matrix[i][j] = self.matrix[i][j]

        k = 1
        while k < pow:
            result = result * self
            k += 1

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
    """ OTHER MATRIX OPERATIONS """
    '''

    def transpose (self):
        result = Matrix(self.n)

        for i in range(self.n):
            for j in range(self.n):
                result.matrix[j][i] = self.matrix[i][j]

        return result
    
    def calculate_identity (self):
        result = Matrix(self.n)

        for i in range(self.n):
            result.matrix[i][i] = 1

        return result
    
    def diagonal_product (self):
        dp = 1

        for i in range(self.n):
            dp *= self.matrix[i][i]

        return dp

    # The I and J indexes will be skipped from the original matrix
    def get_submatrix (self, I, J):
        submatrix = Matrix(self.n - 1)
        sub_i = 0

        for i in range(self.n):
            if i == I:
                continue
            sub_j = 0
            for j in range(self.n):
                if j == J:
                    continue
                submatrix.matrix[sub_i][sub_j] = self.matrix[i][j]
                sub_j += 1
            sub_i += 1
        
        return submatrix
    
    def determinant (self):
        if self.is_triangular() or self.is_diagonal():
            return self.diagonal_product()
        
        if self.n == 1:
            return self.matrix[0][0]
        elif self.n == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            det = 0
            for j in range(self.n):
                sign = (-1) ** j
                sub_det = self.get_submatrix(0, j).determinant()
                det += sign * self.matrix[0][j] * sub_det
            return det
    
    '''
    """ MATRIX PROPERTIES """
    '''

    def is_null (self):
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] != 0:
                    return False
        return True
    
    def is_diagonal (self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.matrix[i][j] != 0:
                    return False
        return True
    
    def is_identity (self):
        if not self.is_diagonal():
            return False

        for i in range(self.n):
            if self.matrix[i][i] != 1:
                return False   
                
        return True
    
    def is_scalar (self):
        if not self.is_diagonal():
            return False
        
        for i in range(self.n - 1):
            if self.matrix[i][i] != self.matrix[i+1][i+1]:
                return False
            
        return True
    
    def is_symmetrical (self):
        return self == self.transpose()

    def is_skew_symmetric (self):
        return self == -self.transpose()
    
    def is_regular (self):
        return self.determinant() != 0
    
    def is_singular (self):
        return not self.is_regular()
    
    def is_idempotent (self):
        return  self == self ** 2
    
    def is_involutory (self):
        return (self ** 2).is_identity()
    
    def is_orthogonal (self):
        identity = Matrix(self.n).calculate_identity()
        return (self * self.transpose()) == identity
    
    def is_normal (self):
        return (self * self.transpose()) == (self.transpose() * self)
    
    def is_triangular (self):
        return self.is_upper_triangular() or self.is_lower_triangular()
    
    def is_upper_triangular (self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.matrix[i][j] != 0:
                    return False     
        return True
    
    def is_lower_triangular (self):
        for i in range(self.n):
            for j in range(i):
                if self.matrix[i][j] != 0:
                    return False
        return True