import math
from rational_package import *

def create_interval(q1, q2):
    if less_than(q2, q1):
        q1, q2 = q2, q1
    return (q1, q2)

def get_left_end(interval):
    return interval[0]

def get_right_end(interval):
    return interval[1]

def inside_interval(q, interval):
    return greater_than(q, get_left_end(interval)) and \
           less_than(q, get_right_end(interval))

def inside_interval_inc(q, interval):
    return greater_than_or_eq(q, get_left_end(interval)) and \
           less_than_or_eq(q, get_right_end(interval))

def get_midpoint(interval):
    return divide_q(add_q(get_left_end(interval), get_right_end(interval)),
                    create_q(2, 1))

def distance_from_midpoint(q, interval):
    return abs_q(minus_q(get_midpoint(interval), q))

def is_point_interval(interval):
    return equal_q(get_left_end(interval), get_right_end(interval))

def right_of(q, interval):
    return greater_than(q, get_right_end(interval))

def left_of(q, interval):
    return less_than(q, get_left_end(interval))

def float_rep_interval(interval):
    return (float_rep(get_left_end(interval)), float_rep(get_right_end(interval)))
