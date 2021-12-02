from basic_packages.interval_package import *
from basic_packages.words_package import *

#Class containing the information of a killer interval: word, matrix and interval
class Killer_Interval(Interval):
    
    def __init__(self, word, matrix):
        
        self.word_dic = {word.inverse(): matrix.inverse()}
        
        a = matrix.get(0, 0)
        b = matrix.get(0, 1)
        self.midpoint = Rational_Number(a, b)
        distance = Rational_Number(1, b)

        super().__init__(self.midpoint - distance, self.midpoint + distance)
        
    def get_midpoint(self):
        return self.midpoint
        
    def append(self, other_interval):
        for k, v in other_interval.word_dic.items():
            if k not in self.word_dic:
                self.word_dic[k] = v
                
    def get_word_dic(self):
        return self.word_dic
        
    def __lt__(self, other):
        return self.midpoint < other.midpoint
        
    def __gt__(self, other):
        return self.midpoint > other.midpoint

