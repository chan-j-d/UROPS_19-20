import math
import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
from basic_packages.matrix_operations import *
from basic_packages.rational_package import *
from basic_packages.words_package import *
from basic_packages.letters import *
from algorithms.algo_interface import *

def SR(x, y):
    t = x - y * (x // y)
    if t == x + y or (t != x and 2 * abs(t) <= abs(y)):
        return t
    else:
        return t - y
    
#Algo class that implements the algo_interface. This is the naive algorithm (first algorithm)
class Naive_Algo(Algo_Interface):
    
    def __init__(self, s, r):
        super().__init__(s, r)
        self.start = True
        
        #Keeps track of the word
        self.word = create_empty_word()

        #Table of letters used
        naive_algo_table = {'a': a_n, 'b': lambda n : b_n(self.s, self.r, n)}
        self.table = Letter_Table(naive_algo_table)
        
    def get_next_matrix(self, number):
        
        #First iteration converts to (r, s) number
        if self.start:
            letter = Letter('b', (self.r - SR(self.r, self.s)) // self.s)
            self.word += letter
            self.start = False
            return self.table.get_matrix(letter)
            
        #Normal naive algorithm
        else:
            
            #Reduction of numerator by 'a' matrix
            a_letter = Naive_Algo.a_reduce(number)
            a_matrix = self.table.get_matrix(a_letter)
            
            #update number
            number *= a_matrix
            
            #Change in numerator and denominator by 'b' matrix
            b_letter = Naive_Algo.b_reduce(number, self.s, self.r)
            b_matrix = self.table.get_matrix(b_letter)
            
            #combined a_b chain
            added_word = a_letter + b_letter
            
            #update word
            self.word += added_word
            
            return a_matrix * b_matrix
            
    #Reduces the numerator of the rational_special
    @staticmethod
    def a_reduce(number):
        x = number.get_p()
        s_y = number.get_q()
        new_x = SR(x, s_y)
        added_power = -((x - new_x) // (s_y))
        return Letter("a", added_power)
            
    @staticmethod
    def b_reduce(number, s, r):
        x = number.get_p()
        y = number.get_q() // s
        new_y = SR(r * y, x)
        added_power = -((r * y - new_y) // x)
        return Letter("b", added_power)
            
        
    def get_word(self):
        return self.word
        
    def get_letter_table(self):
        return self.table
        

