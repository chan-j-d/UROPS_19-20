import math

#Stunted matrix implementation. Capable of most normal matrix operations but catered to this project.
class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    #Multiples 2 matrices together
    def __mul__(self, other):
        m1 = self.matrix
        m2 = other.matrix
        new_mat = []
        for i in range(len(m1)):
            new_row = []
            for j in range(len(m2)):
                ij_value = 0
                for k in range(len(m2)):
                    ij_value += m1[i][k] * m2[k][j]
                new_row.append(ij_value)
            new_mat.append(new_row)
        return Matrix(new_mat)
    
    @staticmethod
    def get_identity(n):
        matrix = []
        for i in range(n):
            new_row = [0] * n
            new_row[i] = 1
            matrix.append(new_row)
        return Matrix(matrix)
        
    def get_dimensions(self):
        return (len(self.matrix), len(self.matrix[0]))
        
    #Iterative method to obtain the power of a matrix
    def __pow__(self, n):
        if n == 0:
            return Square_Matrix.get_identity(self.get_dimensions()[0])
        if n < 0:
            return self.inverse() ** (-n)
        final_matrix = self
        for i in range(n - 1):
            final_matrix *= self
        return final_matrix
            
    def __repr__(self):
        return "[[" + "], [".join((", ".join(map(lambda x: str(x), lst)) for lst in self.matrix)) + "]]"

    def get_matrix(self):
        return self.matrix
        
    def get(self, i, j):
        return self.matrix[i][j]

#Reduces all entries of a matrix by their gcd
def matrix_gcd_reduction(matrix):
    new_matrix = []
    new_matrix.append(matrix[0].copy())
    new_matrix.append(matrix[1].copy())
    gcd1 = math.gcd(new_matrix[0][0], new_matrix[0][1])
    gcd2 = math.gcd(new_matrix[1][0], new_matrix[1][1])
    gcd = math.gcd(gcd1, gcd2)
    sigma = 1 if matrix[0][0] >= 0 else -1
    new_matrix[0][0] = new_matrix[0][0] // gcd * sigma
    new_matrix[0][1] = new_matrix[0][1] // gcd * sigma
    new_matrix[1][0] = new_matrix[1][0] // gcd * sigma
    new_matrix[1][1] = new_matrix[1][1] // gcd * sigma
    return new_matrix
    
    
#2 x 2 matrix always made up of integers where [[ra, rb], [rc, rd]] == [[a, b], [c, d]] in this project
class AB_Matrix(Matrix):
    
    def __init__(self, matrix):
        matrix = matrix_gcd_reduction(matrix)
        super().__init__(matrix)
        
    def inverse(self):
        matrix = self.matrix
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return AB_Matrix([[d, -b], [-c, a]])
        
    @staticmethod
    def convert_to_AB_matrix(matrix):
        return AB_Matrix(matrix.matrix)
        
    def __mul__(self, other):
        new_matrix = super().__mul__(other)
        return AB_Matrix(new_matrix.matrix)
        
    def __eq__(self, other):
        mat1 = self.matrix
        mat2 = other.matrix
        return mat1[0] == mat2[0] and mat1[1] == mat2[1]