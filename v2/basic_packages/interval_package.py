import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
import math
from basic_packages.rational_package import *

def create_interval(q1, q2):
    return Interval(q1, q2)

#Encapsulates Interval related operation
class Interval:
    
    def __init__(self, q1, q2):
        if q2 < q1:
            q1, q2 = q2, q1
        self.left_end = q1
        self.right_end = q2
    
    def get_left_end(self):
        return self.left_end
        
    def get_right_end(self):
        return self.right_end
        
    def contains(self, q):
        return self.left_end < q and self.right_end > q
        
    def contains_inc(self, q):
        return self.left_end <= q and self.right_end >= q
        
    def get_midpoint(self):
        return (self.left_end + self.right_end) / create_q(2, 1)
        
    def distance_from_midpoint(self, q):
        return abs((q - self.get_midpoint()))
        
    def is_point_interval(self):
        return self.left_end == self.right_end
        
    def right_of(self, q):
        return q < self.left_end
        
    def left_of(self, q):
        return q > self.right_end
        
    def range(self):
        return self.right_end - self.left_end
        
    def __repr__(self):
        return "(%s, %s)" % (self.left_end, self.right_end)
        
    def float_rep(self):
        return (self.left_end.float_rep(), self.right_end.float_rep())
        
    def __eq__(self, other):
        return self.left_end == other.left_end and self.right_end == other.right_end
        
    def __hash__(self):
        return hash((self.left_end.tup_rep(), self.right_end.tup_rep()))
