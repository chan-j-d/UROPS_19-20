import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
from basic_packages.words_package import matrix_word

#Interface for algorithm implementation.
class Algo_Interface:
    
    def __init__(self, s, r):
        self.s = s
        self.r = r
        
    #Method to override to obtain the next matrix from the current number.
    def get_next_matrix(self, number):
        pass
    
    def get_word(self):
        pass
        
    def get_letter_table(self):
        pass
        
    #Default method to get the current matrix
    def get_matrix(self):
        return matrix_word(self.get_word(), self.get_letter_table())