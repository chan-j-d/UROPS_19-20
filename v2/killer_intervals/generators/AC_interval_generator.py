from killer_intervals.generators.interval_generator_package import *
from killer_intervals.killer_interval import Killer_Interval
from killer_intervals.interval_collection import Interval_Collection

from basic_packages.words_package import *
from basic_packages.letters import *

class AC_Interval_Generator(Interval_Generator_Interface):
    
    def __init__(self, s, r, size):
        self.s = s
        self.r = r
        self.size = size
        
    def generate_intervals(self):
        return self.mono_words(self.size)
        
    #Creates words from a^m, c^n, a^k where m and n vary from -size to size and
    #k brings the word back to the range -1 to 1
    def mono_words(self, size):
        
        #object holding all intervals by the end
        intervals = Interval_Collection()
        
        for i in range(-size, size + 1):
            #Skip words where A has 0 power
            if i == 0:
                continue
                
            #First letter & matrix
            word = Letter('a', i)
            matrix_A = a_n(i)
            
            for j in range(-size, size + 1):
                #Skip words where C has 0 power
                if j == 0:
                    continue
                
                #Second letter & matrix
                final_word = word + Letter('c', j)
                matrix_C = c_n(self.s, j)
                final_mat = matrix_A * matrix_C
                
                #Power to add to bring it within the principle range of (-1/2, 1/2)
                additional_letter = adjust_interval(final_mat)
                
                #New word
                final_word += additional_letter
                
                #New matrix
                final_mat *= a_n(additional_letter.get_power())

                #Creating the new killer interval with word and matrix
                new_interval = Killer_Interval(final_word, final_mat)
                
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

