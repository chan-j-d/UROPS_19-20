from killer_intervals.generators.interval_generator_package import *
from killer_intervals.killer_interval import Killer_Interval
from killer_intervals.interval_collection import Interval_Collection

from basic_packages.words_package import *
from basic_packages.letters import *

class Naive_Unique_Interval_Generator(Interval_Generator_Interface):
    
    def __init__(self, s, r, size):
        self.s = s
        self.r = r
        self.size = size
        
    def generate_intervals(self):
        return self.mono_words(self.size)
        
    #Creates words from a^m, b^n, a^k where m and n vary from -size to size and
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
                #Skip words where B has 0 power
                if j == 0:
                    continue
                
                #Second letter & matrix
                final_word = word + Letter('b', j)
                matrix_B = b_n(self.s, self.r, j)
                final_mat = matrix_A * matrix_B
                
                #Power to add to bring it within the principle range of (-1/2, 1/2)
                additional_letter = adjust_interval(final_mat)
                
                #New word
                final_word += additional_letter
                
                #New matrix
                final_mat *= a_n(additional_letter.get_power())

                #Creating the new killer interval with word and matrix
                new_interval = Killer_Interval(final_word, final_mat)
                
                #Add the new interval if it not already in the collection
                if new_interval not in intervals:
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
    
#Creates words of the form (a^m1 * b^n1) * (a^m2 * b^n2) ... of length length
def length_words(s, r, length, size):
    matrices = []
    if length == 1:
        return mono_words(s, r, size)
    else:
        shortened_lst = length_words(s, r, length - 1, size)
        for i in range(-size, size + 1):
            if i == 0:
                continue
            matrix_A = a_n(i)
            for j in range(-size, size + 1):
                if j == 0:
                    continue
                matrix_B = b_n(s, r, j)
                inter_mat = matrix_mul(matrix_A, matrix_B)
                inter_mat = matrix_gcd_reduction(inter_mat)
                for pair in shortened_lst:
                    new_word = create_word([create_letter("a", i), create_letter("b", j)])
                    extend_word(new_word, pair[0])
                    final_mat = matrix_mul(inter_mat, pair[1])
                    final_mat = matrix_gcd_reduction(final_mat)
                    change_needed = check_for_change(final_mat)
                    if change_needed:
                        reduced_a_power, final_mat = change_interval(final_mat)
                    repeated = False
                    for upper_half in map(lambda x: create_q_tup(x[1][0]), matrices):
                        if equal_q(create_q_tup(final_mat[0]), upper_half):
                            repeated = True
                            break
                    if repeated:
                        continue
                    elif change_needed:
                        add_letter(new_word, create_letter("a", reduced_a_power))
                    matrices.append((new_word, final_mat))
        shortened_lst.extend(matrices)
        return shortened_lst
