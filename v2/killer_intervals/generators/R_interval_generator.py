from killer_intervals.generators.interval_generator_package import *
from killer_intervals.killer_interval import Killer_Interval
from killer_intervals.interval_collection import Interval_Collection

from basic_packages.words_package import *
from basic_packages.letters import *

class R_Interval_Generator(Interval_Generator_Interface):
    
    def __init__(self, s, r, size):
        self.s = s
        self.r = r
        self.size = size
        
    def generate_intervals(self):
        
        #object holding all intervals by the end
        intervals = Interval_Collection()
        
        #generates R = AB^-1 from 1 to R_POWER
        for i in range(1, self.size + 1):
            
            #New word with one letter as the r power
            word = Word([Letter('r', i)])
            matrix = r_n(self.s, self.r, i)
            
            #Adjust to within the principal range of -1/2 to 1/2
            additional_letter = adjust_interval(matrix)
            
            #New word
            word += additional_letter
            #New matrix
            matrix *= a_n(additional_letter.get_power())
            
            #Creating new interval
            new_interval = Killer_Interval(word, matrix)
            
            #Add the new interval into the collection
            intervals.append(new_interval)
            
        return intervals

        
#By post-multiplying another a matrix, we bring the killer interval of the matrix into (-1/2, 1/2)
def adjust_interval(matrix):
    a = matrix.get(0, 0)
    b = matrix.get(0, 1)
    return Letter('a', -(a - SR2(a, b)) // b)
    
def SR2(x, y):
    t = x - y * (x // y)
    if 2 * abs(t) <= abs(y):
        return t
    else:
        return t - y