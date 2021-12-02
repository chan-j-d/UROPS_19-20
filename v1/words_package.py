import math
from rational_package import *
from matrix_operations import *

def create_empty_word():
    return []
    
def create_word(lst):
    return lst
    
def create_letter(type, power):
    return (type, power)
    
def get_type(letter):
    return letter[0]
    
def get_power(letter):
    return letter[1]
    
def same_type(letter1, letter2):
    return get_type(letter1) == get_type(letter2)
    
def delete_letter(word, index):
    return word.pop(index)
    
def add_letter(word, letter):
    if len(word) == 0:
        word.append(letter)
        return
    last_letter = word[-1]
    if same_type(last_letter, letter):
        new_power = get_power(last_letter) + get_power(letter)
        if new_power == 0:
            delete_letter(word, -1)
            return
        else:
            word[-1] = create_letter(get_type(last_letter), new_power)
    else:
        word.append(letter)
    
def extend_word(word1, word2):
    if len(word1) == 0:
        word1.extend(word2)
    for i in range(len(word2)):
        new_letter = word2[i]
        last_letter = word1[-1]
        if same_type(last_letter, new_letter):
            add_letter(word1, new_letter)
        else:
            word1.extend(word2[i:])
            return            
            

def matrix_word(lst, s, r):
    start = [[1, 0], [0, 1]]
    b_n_SR = lambda n : b_n(s, r, n)
    for i in lst:
        letter, power = i
        if letter == "b":
            func = b_n_SR
        elif letter == "a":
            func = a_n
        curr_letter = func(power)
        start = matrix_mul(start, curr_letter)
        start = matrix_gcd_reduction(start)
    return start

def inverse_power_lst(lst):
    inverse_lst = []
    for i in range(len(lst) - 1, -1, -1):
        ref_letter = lst[i]
        inverse_lst.append((ref_letter[0], -ref_letter[1]))
    return inverse_lst

def remove_last_a(word):
    last_letter = word[-1]
    if get_type(last_letter) == "a":
        return delete_letter(word, -1)
        