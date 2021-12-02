class Tree_Node:
    
    def __init__(self, interval):
        self.interval = interval
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.interval < other.interval
        
    def __gt__(self, other):
        return self.interval > other.interval
        
class Naive_Interval_Tree:
    
    def __init__(self, interval_lst):
        self.root = Naive_Interval_Tree.create_tree(interval_lst)
        
    #Recursively creates a tree from a sorted list of disjoint intervals
    @staticmethod
    def create_tree(interval_lst):
        length = len(interval_lst)
        if length == 0: 
            return None
        elif length == 1:
            return Tree_Node(interval_lst[0])
        else:
            middle_index = length // 2
            root_node = Tree_Node(interval_lst[middle_index])
            root_node.left = Naive_Interval_Tree.create_tree(interval_lst[:middle_index])
            root_node.right = Naive_Interval_Tree.create_tree(interval_lst[middle_index+1:])
            return root_node
    
    #Checks if a number is contained within the interval tree
    def contains(self, number):
        #helper method to recursively check the nodes
        def helper(node, number):
            if node.interval.contains_inc(number):
                return True
            elif node.interval.left_of(number):
                if node.right == None:
                    return False
                else:
                    return helper(node.right, number)
            else:
                if node.left == None:
                    return False
                else:
                    return helper(node.left, number)
        return helper(self.root, number)
        
#Testing
"""
import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
from killer_intervals.naive_interval_generator import *
from killer_intervals.interval_generator_package import *
from basic_packages.rational_package import *
g = Naive_Interval_Generator(39, 10)
gaps = find_gaps(g.mono_words(10))
tree = Naive_Interval_Tree(gaps)
def test(denom):
    covered = 0
    for i in range(-denom, denom + 1):
        if not tree.contains(Rational_Number(i, denom)):
            covered += 1
    return covered
"""