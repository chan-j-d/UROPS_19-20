from killer_intervals.matrix_chooser.matrix_chooser_interface import *

class Largest_Ratio_Chooser(Matrix_Chooser_Interface):
    
    def choose(self, number, killer_interval):
        
        word_matrix_lst = [(k, v) for k, v in killer_interval.get_word_dic().items()]
        
        p = number.get_p()
        q = number.get_q()
        
        sorting_key = lambda x : abs(x[1].get(0, 0) * p + x[1].get(1, 0) * q)
        
        word_matrix_lst.sort(key=sorting_key, reverse=True)

        return word_matrix_lst[0]