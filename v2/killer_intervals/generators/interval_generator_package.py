from basic_packages.rational_package import *
from basic_packages.interval_package import *

class Interval_Generator_Interface:
    
    def __init__(self, s, r):
        self.s = s
        self.r = r
        
    def generate_intervals():
        pass
    
#Find the two powers of 'a' to postmultiply the matrix with to obtain 2 intervals in (-1, 1)
def adjust_interval(matrix):
    a = matrix.get(0, 0)
    b = matrix.get(0, 1)
    
    #Find change in power necessary
    n = a // abs(b)
    
    if b < 0:
        return n, n + 1
    else:
        return -n, -n - 1
        
def join_interval_lst(*lsts):
    interval_set = set()
    for lst in lsts:
        interval_set = interval_set.union(set(lst))
    return list(interval_set)

#Finds gap intervals from a set of intervals
def find_gaps(lst):
    lst = lst.copy()
    lst.sort(key = lambda x: x.get_left_end())
    start = lst[0].get_left_end()
    #end = lst[len(lst) - 1][0][1]
    gaps = []
    previous_end = Rational_Number(-1, 2)
    for interval in lst:
        left_end = interval.get_left_end()
        right_end = interval.get_right_end()
        if previous_end == left_end or previous_end < left_end:
            gaps.append(Interval(previous_end, left_end))
            previous_end = right_end
        elif previous_end < right_end:
            previous_end = right_end
    if previous_end <= Rational_Number(1, 2):
        gaps.append(Interval(previous_end, Rational_Number(1, 2)))
    return gaps