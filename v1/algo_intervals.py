import sys
sys.path.append('C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v1')

from killer_intervals import *
from algo import *
from rational_package import *
from interval_package import *
from matrix_operations import *
from words_package import *
from graphing_tools import *

WORD_LENGTH = 1
SIZE = 10

def interval_algo(s, r, N):
    
    #Settings up killer intervals
    intervals_details = find_intervals(length_words(s, r, WORD_LENGTH, SIZE))
    gaps = intervals_details[0]
    interval_info = intervals_details[1]
    interval_info.sort(key = lambda x : get_midpoint(x[0]))
    #print(tuple(map(lambda x : float_rep_interval(x), gaps)))
    interval_lst = []
    matrix_info = []
    for k, v in interval_info:
        interval_lst.append(k)
        matrix_info.append(v)
    matrix_info = list(map(lambda tup : (inverse_power_lst(tup[0]), ab_inverse(tup[1])), matrix_info))
        
        
    #Starting algorithm
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return True
    xi = r
    first_letter = (r - SR(r, s)) // s
    yi = first_letter
    
    if yi == 0:
        return True
        
    word = create_empty_word()
    add_letter(word, create_letter("b", first_letter))
    q = create_q(xi, s * yi)
    pair_tracker = [q]

    b_reduce_sr = lambda q : b_reduce(q, s, r)
    
    factor_100 = N // 100
    
    for i in range(N):
        #if i % factor_100 == 0:
            #print(i // factor_100, "%:", q)
        added_power, q = a_reduce(q)
        add_letter(word, added_power)
        
        #print("a:", q, float_rep(q))
        if i > 1 and covered(q, gaps):
            inverse_index = find_best_interval(q, interval_lst)
            print(q, interval_lst[inverse_index])
            matrix_details = matrix_info[inverse_index]
            letters = matrix_details[0]
            matrix = matrix_details[1]
            q = create_q_tup(q_mul_matrix(q, matrix))
            extend_word(word, letters)
            
        else:
            added_power, q = b_reduce_sr(q)
            add_letter(word, added_power)
            
        #print("other:", q, float_rep(q))
        
        if get_s(q) * get_r(q) * (abs(get_s(q)) - 1) == 0 or member_of(q, pair_tracker):
            pair_tracker.append(q)
            final_matrix = matrix_word(word, s, r)
            if final_matrix[0][1] == 0:
                a_letter = remove_last_a(word)
                if a_letter != None:
                    final_matrix = matrix_mul(final_matrix, a_n(-get_power(a_letter)))
            #print("new algo:", len(pair_tracker))
            print("word:", s, r, len(word))
            #print(final_matrix)
            return True
            
        pair_tracker.append(q)
        
    print(q)
    return False
    
    
#returns the 2-valued word path instead
def interval_algo_info(s, r, N):
    
    #Settings up killer intervals
    intervals_details = find_intervals(length_words(s, r, WORD_LENGTH, SIZE))
    gaps = intervals_details[0]
    interval_info = intervals_details[1]
    interval_info.sort(key = lambda x : get_midpoint(x[0]))
    #print(tuple(map(lambda x : float_rep_interval(x), gaps)))
    interval_lst = []
    matrix_info = []
    for k, v in interval_info:
        interval_lst.append(k)
        matrix_info.append(v)
    matrix_info = list(map(lambda tup : (inverse_power_lst(tup[0]), ab_inverse(tup[1])), matrix_info))
        
        
    #Starting algorithm
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return []
    xi = r
    first_letter = (r - SR(r, s)) // s
    yi = first_letter
    
    if yi == 0:
        return []
        
    word = create_empty_word()
    add_letter(word, create_letter("b", first_letter))
    q = create_q(xi, s * yi)
    pair_tracker = [q]

    b_reduce_sr = lambda q : b_reduce(q, s, r)
    
    factor_100 = N // 100
    
    for i in range(N):
        #if i % factor_100 == 0:
            #print(i // factor_100, "%:", q)
        added_power, q = a_reduce(q)
        add_letter(word, added_power)
        
        #print("a:", q, float_rep(q))
        if i > 1 and covered(q, gaps):
            #print("Killer interval used!")
            inverse_index = find_best_interval(q, interval_lst)
            matrix_details = matrix_info[inverse_index]
            letters = matrix_details[0]
            matrix = matrix_details[1]
            q = create_q_tup(q_mul_matrix(q, matrix))
            extend_word(word, letters)
            
        else:
            
            added_power, q = b_reduce_sr(q)
            add_letter(word, added_power)
            
        #print("other:", q, float_rep(q))
        
        if get_s(q) * get_r(q) * (abs(get_s(q)) - 1) == 0 or member_of(q, pair_tracker):
            pair_tracker.append(q)
            final_matrix = matrix_word(word, s, r)
            if final_matrix[0][1] == 0:
                a_letter = remove_last_a(word)
                if a_letter != None:
                    final_matrix = matrix_mul(final_matrix, a_n(-get_power(a_letter)))
            #print("new algo:", len(pair_tracker))
            #print("word:", len(word), word)
            #print(final_matrix)
            return pair_tracker
            
        pair_tracker.append(q)
        
    print(q)
    return pair_tracker
    
def graph_test(s, r):
    lst = interval_algo_info(s, r, 5000)
    graph(lst)
    
#Multiplying word with matrix
def q_mul_matrix(q, matrix):
    return matrix_mul([q], matrix)[0]

#Binary search to see if q falls into one of the uncovered gaps (inclusive)
def covered(q, gaps):
    if len(gaps) == 0:
        return True
    elif (greater_than(q, create_q(1, 2)) or less_than(q, create_q(-1, 2))):
        return False
    start = 0
    end = len(gaps) - 1
    mid = (start + end) // 2
    if left_of(q, gaps[0]) or right_of(q, gaps[end]):
        return True
    elif inside_interval_inc(q, gaps[end]):
        return False
    while start != end:
        curr_gap_interval = gaps[mid]
        if inside_interval_inc(q, curr_gap_interval):
            return False
        elif right_of(q, curr_gap_interval):
            start = mid + 1
        else:
            end = mid
        mid = (start + end) // 2
    return True

def find_best_interval(q, interval_lst):
    start = 0
    end = len(interval_lst) - 1
    right_end = False
    left_end = False
    found_closest = False
    
    #Checking edge cases
    if greater_than(q, get_midpoint(interval_lst[end])):
        right_end = True
        found_closest = True
        closest = (end, end)
    elif less_than(q, get_midpoint(interval_lst[start])):
        left_end = True
        found_closest = True
        closest = (start, start)
    mid = (start + end) // 2
    
    #Finding gap in which this rational number falls between the midpoint of the left and right intervals
    while not found_closest:
        right_midpoint = get_midpoint(interval_lst[mid + 1])
        left_midpoint = get_midpoint(interval_lst[mid])
        if less_than_or_eq(q, right_midpoint):
            if equal_q(q, right_midpoint):
                return mid + 1
            elif greater_than_or_eq(q, left_midpoint):
                if equal_q(q, left_midpoint):
                    return mid
                else:
                    found_closest = True
                    closest = (mid, mid + 1)
                    break
            end = mid
        else:
            start = mid + 1
        mid = (start + end) // 2
        
    #Searching outwards for an interval which fits q
    while not (right_end or left_end):
        #print("Closest:", closest)
        left_interval = interval_lst[closest[0]]
        right_interval = interval_lst[closest[1]]
        if inside_interval(q, left_interval):
            if not inside_interval(q, right_interval):
                return closest[0]
            else:
                left_distance = distance_from_midpoint(q, left_interval)
                right_distance = distance_from_midpoint(q, right_interval)
                if left_distance > right_distance:
                    return closest[1]
                else:
                    return closest[0]
        elif inside_interval(q, right_interval):
            return closest[1]
        else:
            new_left = closest[0] - 1
            new_right = closest[1] + 1
            if new_left < 0:
                left_end = True
                break
            elif new_right > len(interval_lst) - 1:
                right_end = True
                break
            closest = (new_left, new_right)
    #print(float_rep(q))
    
    #When one end is reached, continue searching in the other direction
    if left_end:
        ref_index = closest[1]
        while True:
            if inside_interval(q, interval_lst[ref_index]):
                return ref_index
            ref_index += 1
    elif right_end:
        ref_index = closest[0]
        while True:
            ref_interval = interval_lst[ref_index]
            #print(ref_index, tuple(map(lambda x : float_rep(x), ref_interval)))
            if inside_interval(q, ref_interval):
                return ref_index
            ref_index -= 1
 
 
    
#Test to see if the second value of the rational number actually gets smaller when multiplied by a killer interval matrix
def test_smaller_r(s, r):
    intervals_details = find_intervals(length_words(s, r, WORD_LENGTH, SIZE))
    gaps = intervals_details[0]
    interval_info = intervals_details[1]
    interval_info.sort(key = lambda x : get_midpoint(x[0]))
    #print(tuple(map(lambda x : float_rep_interval(x), gaps)))
    interval_lst = []
    matrix_info = []
    for k, v in interval_info:
        interval_lst.append(k)
        matrix_info.append(v)
    print(matrix_info)
    matrix_info = list(map(lambda tup : (inverse_power_lst(tup[0]), ab_inverse(tup[1])), matrix_info))
    print(matrix_info)    
    
    #print(tuple(map(lambda x : float_rep_interval(x), interval_lst)))
    for i in range(-20, 21):
        q = create_q(i, 40)
        if covered(q, gaps):
            index = find_best_interval(q, interval_lst)
            #print("Best interval:", q, interval_lst[index])
            inverse_word_lst = matrix_info[index][0]
            inverse_mat = matrix_info[index][1]
            print("inverse and mat:", inverse_word_lst, inverse_mat)
            print("Matrix word:", inverse_mat)
            print("After mul:", matrix_mul([q], inverse_mat))
        else:
            print("Not covered:", q)
    
    return

def test1_new():
    excep = []
    for r in range(2, 11):
        for s in range(2, 4 * r):
            #rel_num(s, r, 5000)
            if not interval_algo(s, r, 5000):
                excep.append((s, r))
    print(excep)