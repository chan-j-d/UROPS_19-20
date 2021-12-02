import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v1'
if path not in sys.path:
    sys.path.append(path)

import math
from matrix_operations import *
from rational_package import *
from words_package import *

def SR(x, y):
    t = x - y * (x // y)
    if t == x + y or (t != x and 2 * abs(t) <= abs(y)):
        return t
    else:
        return t - y

def SR2(x, y):
    t = x - y * (x // y)
    if t == x + y or 2 * abs(t) <= abs(y):
        return t
    else:
        return t - y

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def member_of(tup, lst):
    for pair in lst:
        if tup[0] == pair[0] and abs(tup[1]) == abs(pair[1]):
            return True
    return False

def rel_num(s, r, M):
    
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return True

    xi = r
    yi = (r - SR(r, s)) // s
    
    if yi == 0:
        return True
        
    word = create_empty_word()
    add_letter(word, create_letter("b", (r - SR(r, s)) // s))
    q = create_q(xi, s * yi)
    
    pair_tracker = [q]
    
    b_reduce_sr = lambda q : b_reduce(q, s, r)

    for i in range(M):
        added_power, q = a_reduce(q)
        add_letter(word, added_power)
        
        added_power, q = b_reduce_sr(q)
        add_letter(word, added_power)
        if get_s(q) * get_r(q) * (abs(get_s(q)) - 1) == 0 or member_of(q, pair_tracker):
            pair_tracker.append(q)
            print("rel_num:", len(pair_tracker))
            print("word:", len(word), word)
            print("q:", s, r)
            print(matrix_word(word, s, r))
            return True
            
        pair_tracker.append(q)
        
    return False
    
def a_reduce(q):
    x = get_s(q)
    s_y = get_r(q)
    new_x = SR(x, s_y)
    added_power = -((x - new_x) // (s_y))
    return create_letter("a", added_power), create_q(new_x, s_y)
    
def b_reduce(q, s, r):
    x = get_s(q)
    y = get_r(q) // s
    new_y = SR(r * y, x)
    added_power = -((r * y - new_y) // x)
    new_x = r * x
    new_y *= s
    return create_letter("b", added_power), create_q(new_x, new_y)

def min3(a, b, c):
    if a * b * c == 0 or a < 0 or c < 0:
        return
    if a % b == 0:
        return (-b / a, 1, c)
    y_bound = min(a - 2, c + abs(c - abs(a - abs(b))))
    xr = 1
    yr = 1
    min_val = abs(a + b + c)
    for y in range(-y_bound, y_bound + 1):
        if y == 0:
            continue
        t = - (c / y + b) / a
        x = int(t)
        if x == 0 or (x != - 1 and (t - x) > 0.5): x += 1
        min_temp = abs((a * x + b) * y + c)
        if min_temp < min_val:
            xr = x
            yr = y
            min_val = min_temp
    return (xr, yr, (a * xr + b) * yr + c)

def rel_num_min(s, r, M):
    
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return True
    xi = SR(r, s)
    yi = (r - SR(r, s)) // s
    if yi == 0:
        return True
    sigma = sign(xi)
    xi = sigma * xi
    yi = sigma * yi
    pair_tracker = [(xi, s * yi)]
    power_tracker = [("b", 1), ("a", -((r - SR(r, s)) // s))]

    for i in range(M):
        
        u, v, x_ = min3(s * xi, s * r * yi, r * xi)
        y_ = r * yi + u * xi

        power_tracker.append(("b", u))
        power_tracker.append(("a", v))
        
        d = math.gcd(x_, y_)
        sigma = sign(x_)
        print(u, v, x_, y_, d)
        if d != 1:
            xi = x_ * sigma // d
            yi = y_ * sigma // d
        else:
            xi = x_ * sigma
            yi = y_ * sigma
        if xi * yi * (xi - 1) == 0 or member_of((xi, s * yi), pair_tracker):
            pair_tracker.append((xi, s * yi))
            print(pair_tracker)
            print(power_tracker)
            return True
        pair_tracker.append((xi, s * yi))
        
    return False

def test1():
    excep = []
    for r in range(2, 11):
        for s in range(2, 4 * r):
            if not rel_num(s, r, 5000):
                excep.append((s, r))
    print(excep)

def test2():
    excep = []
    for s in range(2, 31):
        for r in range(2, 10 * s + 1):
            if math.gcd(s, r) == 1 and not rel_num(s, r, 5000):
                excep.append((s, r))
    print(excep)

