import math

def a_n(n):
    return [[1, 0], [n, 1]]

def b_n(s, r, n):
    return [[r, n * s], [0, r]]

def ab_inverse(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    return [[d, -b], [-c, a]]

def matrix_mul(m1, m2):
    new_mat = []
    for i in range(len(m1)):
        new_row = []
        for j in range(len(m2)):
            ij_value = 0
            for k in range(len(m2)):
                ij_value += m1[i][k] * m2[k][j]
            new_row.append(ij_value)
        new_mat.append(new_row)
    return new_mat

def matrix_power(m1, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    return matrix_mul(m1, matrix_power(m1, n - 1))

def matrix_gcd_reduction(matrix):
    new_matrix = []
    new_matrix.append(matrix[0].copy())
    new_matrix.append(matrix[1].copy())
    gcd1 = math.gcd(new_matrix[0][0], new_matrix[0][1])
    gcd2 = math.gcd(new_matrix[1][0], new_matrix[1][1])
    gcd = math.gcd(gcd1, gcd2)
    if gcd != 1:
        new_matrix[0][0] = new_matrix[0][0] // gcd
        new_matrix[0][1] = new_matrix[0][1] // gcd
        new_matrix[1][0] = new_matrix[1][0] // gcd
        new_matrix[1][1] = new_matrix[1][1] // gcd
    return new_matrix
