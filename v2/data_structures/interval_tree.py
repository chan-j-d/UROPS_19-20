class Tree_Node:
    
    def __init__(self, number, lst):
        self.number = number
        
        #List sorted by left end
        self.left_ordered_lst = lst.copy()
        self.left_ordered_lst.sort(key=lambda x : x.get_left_end())
        
        #List sorted by right end
        self.right_ordered_lst = lst.copy()
        self.right_ordered_lst.sort(key=lambda x : x.get_right_end())
        
        self.left = None
        self.right = None

    def get_number(self):
        return self.number
        
    def find_intervals_containing(self, number):
        
        contained_lst = []
        
        #If the number equals the number of this node, we can safely add all intervals
        #to the list
        if number == self.number:
            return self.left_ordered_lst
            
        #If less than the centre number, then we need only checked those with left ends
        #smaller than the number
        elif number < self.number:
            for interval in self.left_ordered_lst:
                if interval.get_left_end() >= number:
                    break
                else:
                    contained_lst.append(interval)
        
        else:
            for interval in self.right_ordered_lst[::-1]:
                if interval.get_right_end() <= number:
                    break
                else:
                    contained_lst.append(interval)
        
        return contained_lst
        
    def get_number(self):
        return self.number
        
    def __repr__(self):
        return "%s: %s" % (str(self.number), str(self.left_ordered_lst))
    
class Interval_Tree:
    
    def __init__(self, interval_lst):
        self.root = Interval_Tree.create_tree(interval_lst)
        
    @staticmethod
    def create_tree(interval_lst):
        
        if len(interval_lst) == 0:
            return None
        
        #find split point
        split = find_split(interval_lst)
        
        #List to store the intervals containing the split value
        contains_split = []
        #Lists containing those left of the number and those right of the number
        left_of_split = []
        right_of_split = []
        for interval in interval_lst:
            if interval.contains_inc(split):
                contains_split.append(interval)
            elif interval.left_of(split):
                left_of_split.append(interval)
            else:
                right_of_split.append(interval)
        
        #Create root_node and attach children
        root_node = Tree_Node(split, contains_split)
        root_node.left = Interval_Tree.create_tree(left_of_split)
        root_node.right = Interval_Tree.create_tree(right_of_split)
        
        return root_node
        
    def find_intervals_containing(self, number):

        #Helper function to help with the recursion through the nodes
        def helper(node, number):
            
            #Check currentnode for intervals
            contained_lst = node.find_intervals_containing(number)
            
            #Compare with the node number to find out where to recurse on
            node_number = node.get_number()
            #If the number equals the node number, then we need not recurse any further
            if number < node_number and node.left != None:
                #If it is smaller than the node number, then we need to recurse on the left
                contained_lst.extend(helper(node.left, number))
            elif number > node_number and node.right != None:
                contained_lst.extend(helper(node.right, number))
                
            return contained_lst
            
        return helper(self.root, number)
        
    def in_order_traversal(self):
        def helper(node):
            if node == None:
                return ""
            else:
                return helper(node.left) + str(node) + helper(node.right)
        return helper(self.root)
            
#Finds the midpoint which splits a list of intervals roughly into 2
def find_split(lst):
    length = len(lst)
    mid_index = length // 2
    if length % 2 == 0:
        midpoint = lst[mid_index].get_midpoint() + lst[mid_index - 1].get_midpoint()
        midpoint /= 2
        return midpoint
    else:
        return lst[mid_index].get_midpoint()
        
#Test
"""import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
from killer_intervals.naive_interval_generator import *
from killer_intervals.interval_generator_package import *
from basic_packages.rational_package import *
g = Naive_Interval_Generator(39, 10)
intervals = g.mono_words(10)
tree = Interval_Tree(intervals)
def test(denom):
    for i in range(-denom, denom + 1):
        number = Rational_Number(i, denom)
        lst = tree.find_intervals_containing(number)
        if len(lst) != 0:
            print(number, lst)"""