import random
from killer_intervals.matrix_chooser.matrix_chooser_interface import *

class Random_Chooser(Matrix_Chooser_Interface):
    
    def choose(self, number, killer_interval):
        key_lst = list(killer_interval.get_word_dic().keys())
        
        key = key_lst[random.randint(0, len(key_lst) - 1)]
        
        #print("Matrix chosen:", killer_interval.get_word_dic()[key], "for number", number, number.float_rep())
        
        """"
        word_matrix_lst = [(k, v) for k, v in killer_interval.get_word_dic().items()]
        
        p = number.get_p()
        q = number.get_q()
        
        def sorting_key(pair):
            matrix = pair[1]
            numerator = p * matrix.get(0, 0) + q * matrix.get(1, 0)
            denominator = p * matrix.get(0, 1) + q * matrix.get(1, 1)

            if denominator == 0:
                return 0
            
            return abs(SR2(numerator, denominator)) / abs(denominator)
            
        word_matrix_lst.sort(key=sorting_key)
        lst = list(map(lambda x : (x[1], sorting_key(x)), word_matrix_lst))
        print("Matrix list sorted by distance from 0:", lst)"""
        
        return key, killer_interval.get_word_dic()[key]
        
        
def SR2(x, y):
    t = x - y * (x // y)
    if t == x + y or 2 * abs(t) <= abs(y):
        return t
    else:
        return t - y
        