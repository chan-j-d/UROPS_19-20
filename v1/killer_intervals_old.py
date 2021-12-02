import math
from algo import *

def test(s, r, size):
    return find_intervals(mono_words(s, r, size))

def test_intervals(s, r, size):
    matrices = mono_words(s, r, size)
    for pair in matrices:
        matrix_checker = matrix_word(pair[0], s, r)
        if matrix_checker != pair[1]:
            print(pair[0])
            print("Problem!", matrix_checker, pair[1])
    

def find_intervals(lst):
    intervals_covered = []
    for i in lst:
        intervals_covered.append(find_interval(i[1]))
    intervals_covered = list(dict.fromkeys(intervals_covered))
    return parse_intervals(intervals_covered)

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
            w = final_mat[0][0]
            x = final_mat[0][1]
            if abs(x) < abs(w) * 2:
                reduce_a_power = -(w - SR(w, x)) // x
                final_mat = matrix_mul(final_mat, a_n(reduce_a_power))
                matrices.append(((0, i, j, reduce_a_power), final_mat))
            else:
                matrices.append(((0, i, j), final_mat))
    return matrices

def find_interval(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    if (a - 1) / b > (a + 1) / b:
        return (((a + 1), b), ((a - 1), b))
    return (((a - 1), b), ((a + 1), b))

def parse_intervals(lst):
    lst.sort(key = lambda x: x[0][0] / x[0][1])
    print(lst)
    start = lst[0][0]
    end = lst[len(lst) - 1][1]
    gaps = []
    previous_end = (-1, 2)
    for i in range(len(lst)):
        if compare_tup(previous_end, lst[i][0]) == -1:
            gaps.append((previous_end, lst[i][0]))
            previous_end = lst[i][1]
        elif compare_tup(previous_end, lst[i][1]) == -1:
            previous_end = lst[i][1]
    if compare_tup(previous_end, (1, 2)) == -1:
        gaps.append((previous_end, (1, 2)))
    gaps = list(map(lambda x: (x[0][0] / x[0][1], x[1][0] / x[1][1]), gaps))
    return start, end, gaps

def compare_tup(tup1, tup2):
    if tup1[0] == tup2[0] and tup1[1] == tup2[1]:
        return 0
    elif tup1[0] / tup1[1] > tup2[0] / tup2[1]:
        return 1
    else:
        return -1
            
