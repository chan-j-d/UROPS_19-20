import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
import math
from basic_packages.rational_package import *
from basic_packages.matrix_operations import *

#Encapsulates a rational number represented by a 1 x 2 matrix capable of interacting with 2 x 2 matrices.
class Rational_Special(Rational_Number):
    
    def __init__(self, m, n):
        super().__init__(m, n)
        
    @staticmethod
    def create_q(m, n):
        return Rational_Special(m, n)
        
    @staticmethod
    def create_q_tup(tup):
        return Rational_Special(tup[0], tup[1])
        
    #This rational number is capable of multiplying with a 2 x 2 matrix as if it were a 1 x 2 matrix
    def __mul__(self, matrix):
        starting_matrix = Matrix([[self.p, self.q]])
        final_matrix = starting_matrix * matrix
        return Rational_Special.create_q_tup(final_matrix.get_matrix()[0])

     
#Creates the starting point at infinity for the project
def starting_point():
    return Rational_Special(1, 0)