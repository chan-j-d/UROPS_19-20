from killer_intervals.generators.interval_generator_package import *
from killer_intervals.interval_collection import *

#Data structures
from data_structures.interval_tree import *
from data_structures.naive_interval_tree import *

SIZE = 10

class Interval_Provider:
    
    def __init__(self, s, r, Interval_Chooser, Matrix_Chooser, *Generators):
        self.s = s
        self.r = r
        self.interval_chooser = Interval_Chooser()
        self.matrix_chooser = Matrix_Chooser()
        
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
            
            interval_used = self.interval_chooser.choose_interval(number, intervals)
            
            #print(interval_used.word_dic)
            
            #Selecting matrix within interval
            pair_used = self.matrix_chooser.choose(number, interval_used)
            #print(pair_used)
            return pair_used
            
            