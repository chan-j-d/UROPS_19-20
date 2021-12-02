from basic_packages.matrix_operations import *

def a_n(n):
    return AB_Matrix([[1, 0], [n, 1]])
    
def b_n(s, r, n):
    return AB_Matrix([[r, n * s], [0, r]])
    
def c_n(s, n):
    return AB_Matrix([[1, n * s], [0, 1]])
    
def r_n(s, r, n):
    if n >= 0:
        return (a_n(1) * b_n(s, r, -1)) ** n
    else:
        return (b_n(s, r, 1) * a_n(-1)) ** (-n)