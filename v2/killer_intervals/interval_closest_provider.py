from killer_intervals.generators.interval_generator_package import *
from killer_intervals.interval_collection import *

#Data structures
from data_structures.interval_tree import *
from data_structures.naive_interval_tree import *

SIZE = 10

class Interval_Closest_Provider:
    
    def __init__(self, s, r, *Generators):
        self.s = s
        self.r = r
        
        #Generating killer intervals
        self.collection = Interval_Collection()
        for generator in Generators:
            self.collection.extend(generator(s, r, SIZE).generate_intervals())
        intervals = self.collection.get_interval_lst()
        
        #Find gaps
        gaps = find_gaps(intervals)
        
        #Building trees
        self.gaps_tree = Naive_Interval_Tree(gaps)
        self.interval_tree = Interval_Tree(intervals)
    
    #Checks if the number is within an interval    
    def in_interval(self, number):
        return not self.gaps_tree.contains(number)
    
    
    #Returns a 2 element tuple of the word and matrix of the selected interval
    def get_interval(self, number):
        
        if not self.gaps_tree.contains(number):
            
            #Falls within a killer interval so we use it
            intervals = self.interval_tree.find_intervals_containing(number)
            
            matrix_lst = []
            
            for interval in intervals:
                matrix_lst.extend(list(interval.get_word_dic().items()))
                
            def sorting_key(number, matrix_pair):
                
                matrix = matrix_pair[1]
                
                m = number.get_p()
                n = number.get_q()
                
                numerator = m * matrix.get(0, 0) + n * matrix.get(1, 0)
                denominator = m * matrix.get(0, 1) + n * matrix.get(1, 1)
                
                if denominator == 0: return 0
                
                numerator = SR(numerator, denominator)
                
                return abs((m ** 2 * denominator) - (n ** 2 * numerator))
                #return abs((m * denominator) - (n * numerator))
                #return abs(denominator)
                #return abs(numerator)
                
            matrix_lst.sort(key=lambda p: sorting_key(number, p))
            #print(matrix_lst)
            return matrix_lst[0]
            
            
            
def SR2(x, y):
    t = x - y * (x // y)
    if t == x + y or 2 * abs(t) <= abs(y):
        return t
    else:
        return t - y
        
def SR(x, y):
    t = x - y * (x // y)
    if t == x + y or (t != x and 2 * abs(t) <= abs(y)):
        return t
    else:
        return t - y