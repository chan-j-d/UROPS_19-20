import math
from algo import *
from rational_package import *
from matrix_operations import *
from interval_package import *
from words_package import *

#Finds the list of gap intervals (index 0), followed by the intervals covered
#represented by a tuple. Index 0 has the interval, index 1 has a tuple of the word followed by the matrix)
def find_intervals(lst):
    intervals_covered = {}
    for i in lst:
        interval = find_interval(i[1])
        if interval not in intervals_covered:
            intervals_covered[interval] = i
    intervals_covered = [(k, v) for k, v in intervals_covered.items()]
    gaps = find_gaps(intervals_covered)
    return find_gaps(intervals_covered), intervals_covered

#From a matrix, finds its killer interval range
def find_interval(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    mid_value = create_q(a, b)
    range_value = create_q(1, b)
    upper = add_q(mid_value, range_value)
    lower = minus_q(mid_value, range_value)
    if compare_q(lower, upper) == 1:
        upper, lower = lower, upper
    return create_interval(lower, upper)

#Creates words from a^m * b^n where m and n vary from -size to size
def mono_words(s, r, size):
    matrices = []
    for i in range(-size, size + 1):
        if i == 0:
            continue
        matrix_A = a_n(i)
        for j in range(-size, size + 1):
            if j == 0:
                continue
            matrix_B = b_n(s, r, j)
            final_mat = matrix_mul(matrix_A, matrix_B)
            final_mat = matrix_gcd_reduction(final_mat)
            change_needed = check_for_change(final_mat)
            if change_needed:
                reduced_a_power, final_mat = change_interval(final_mat)
            repeated = False
            for upper_half in map(lambda x: create_q_tup(x[1][0]), matrices):
                if equal_q(create_q_tup(final_mat[0]), upper_half):
                    repeated = True
                    break
            if repeated:
                continue
            word = create_word([create_letter("a", i), create_letter("b", j)])
            if change_needed:
                add_letter(word, create_letter("a", reduced_a_power))
            matrices.append((word, final_mat))
    return matrices

#Creates words of the form (a^m1 * b^n1) * (a^m2 * b^n2) ... of length length
def length_words(s, r, length, size):
    matrices = []
    if length == 1:
        return mono_words(s, r, size)
    else:
        shortened_lst = length_words(s, r, length - 1, size)
        for i in range(-size, size + 1):
            if i == 0:
                continue
            matrix_A = a_n(i)
            for j in range(-size, size + 1):
                if j == 0:
                    continue
                matrix_B = b_n(s, r, j)
                inter_mat = matrix_mul(matrix_A, matrix_B)
                inter_mat = matrix_gcd_reduction(inter_mat)
                for pair in shortened_lst:
                    new_word = create_word([create_letter("a", i), create_letter("b", j)])
                    extend_word(new_word, pair[0])
                    final_mat = matrix_mul(inter_mat, pair[1])
                    final_mat = matrix_gcd_reduction(final_mat)
                    change_needed = check_for_change(final_mat)
                    if change_needed:
                        reduced_a_power, final_mat = change_interval(final_mat)
                    repeated = False
                    for upper_half in map(lambda x: create_q_tup(x[1][0]), matrices):
                        if equal_q(create_q_tup(final_mat[0]), upper_half):
                            repeated = True
                            break
                    if repeated:
                        continue
                    elif change_needed:
                        add_letter(new_word, create_letter("a", reduced_a_power))
                    matrices.append((new_word, final_mat))
        shortened_lst.extend(matrices)
        return shortened_lst

#By post-multiplying another a matrix, we bring the killer interval of the matrix into (-1/2, 1/2)
def change_interval(matrix):
    w = matrix[0][0]
    x = matrix[0][1]
    new_matrix = []
    new_matrix.append(matrix[0].copy())
    new_matrix.append(matrix[1].copy())
    reduce_a_power = -(w - SR2(w, x)) // x
    new_matrix = matrix_mul(new_matrix, a_n(reduce_a_power))
    return reduce_a_power, new_matrix

#Checks if the matrix's killer interval is within (-1/2, 1/2)
def check_for_change(matrix):
    w = matrix[0][0]
    x = matrix[0][1]
    if abs(x) < abs(w) * 2:
        return True
    return False

#Finds gap intervals
def find_gaps(lst):
    lst = lst.copy()
    lst.sort(key = lambda x: float_rep(get_left_end(x[0])))
    start = lst[0][0][0]
    end = lst[len(lst) - 1][0][1]
    gaps = []
    previous_end = create_q(-1, 2)
    for i in range(len(lst)):
        interval = lst[i][0]
        left_end = get_left_end(interval)
        right_end = get_right_end(interval)
        if equal_q(previous_end, left_end) or compare_q(previous_end, left_end) == -1:
            gaps.append(create_interval(previous_end, left_end))
            previous_end = create_q_tup(right_end)
        elif compare_q(previous_end, right_end) == -1:
            previous_end = create_q_tup(right_end)
    if less_than(previous_end, create_q(1, 2)):
        gaps.append(create_interval(previous_end, create_q(1, 2)))
    #gaps = list(map(lambda x: (x[0][0] / x[0][1], x[1][0] / x[1][1]), gaps))
    print(gaps)
    return gaps

def test2_7():
    for i in range(2, 8):
        for j in range(1, i):
            print(j, i)
            print(test(j, i, 1, 10))

def test(s, r, length, size):
    return find_intervals(length_words(s, r, length, size))

def test_intervals(s, r, length,    size):
    matrices = length_words(s, r, length, size)
    flag = True
    for pair in matrices:
        matrix_checker = matrix_word(pair[0], s, r)
        if matrix_checker != pair[1]:
            flag = False
            print(pair[0])
            print("Problem!", matrix_checker, pair[1])
    if flag:
        print("No issues")
