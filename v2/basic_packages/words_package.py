import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
import math
from basic_packages.rational_package import *
from basic_packages.matrix_operations import *

#Represents the letter to matrix conversion, holds a dictionary of letter and function pairs.
#The function takes in the power and returns the matrix in O(1) time.
class Letter_Table:
    
    def __init__(self, dic):
        self.table = dic.copy()
        
    @staticmethod
    def empty_table():
        return Letter_Table({})
        
    def add_letter(self, string, func):
        if string not in self.table:
            self.table[string] = func
            return True
        else:
            return False
            
    def get_matrix(self, letter):
        power = letter.get_power()
        string = letter.get_letter()
        return self.table[string](power)
        
    #Shows the table and their functions to the 1st power (shows a matrix)
    def show_table(self):
        return dict(map(lambda d : (d[0], d[1](1)), self.table.items()))
        
    def __add__(self, other):
        new_table = self.table.copy()
        for k, v in other.table.items():
            if k not in new_table:
                new_table[k] = v
        return Letter_Table(new_table)
        
    def __repr__(self):
        return str(self.show_table())
           
def new_table():
    return Letter_Table.empty_table()
    
"""
table1 = new_table()
table2 = Letter_Table({'a': a_n, 'b': lambda x : b_n(1, 7, x)})
table1.add_letter('a', a_n)
print(table1 + table2)"""
                
#'Letter' which is a matrix represented by its letter and a number for its power
class Letter:
    
    def __init__(self, string, number):
        self.letter = string
        self.power = number
        
    def get_letter(self):
        return self.letter
        
    def get_power(self):
        return self.power
        
    def __repr__(self):
        return "%s^%d" % (self.letter, self.power)
        
    def same_type(self, other):
        return self.letter == other.letter
        
    def __add__(self, other):
        if isinstance(other, Word):
            return Word([self]) + other
        elif self.power == 0:
            return other
        elif self.same_type(other):
            return Letter(self.letter, self.power + other.power)
        else:
            return Word([self, other])
            
    def inverse(self):
        return Letter(self.letter, -self.power)
        
    def __eq__(self, other):
        return self.letter == other.letter and self.power == other.power

#A string of letters
class Word:
    
    def __init__(self, lst):
        self.letters = lst.copy()

    def __add__(self, other):
        
        #If empty word, then it becomes a word of the added letter or other word
        if len(self.letters) == 0:
            if isinstance(other, Letter):
                return Word([other])
            else:
                return Word(other.letters.copy())
        
        def helper(word, other):
            
            new_lst = word.letters.copy()

            if len(new_lst) == 0:
                return Word(new_lst)
            
            last_letter = new_lst[-1]
            
            #If power == 0 then we are not adding a significant letter and can ignore it.
            if other.get_power() == 0:
                return word
            
            #If the other's type is the same as our last letter, then we join both letters together.
            elif last_letter.same_type(other):
                new_letter = last_letter + other
                #In the event that the new letter has power 0, we remove it from the word.
                if new_letter.get_power() == 0:
                    new_lst.pop(-1)
                else:
                    new_lst[-1] = new_letter
                return Word(new_lst)
                
            #If not of the same type, we simply add it to the end of the list.
            else:
                new_lst.append(other)
                return Word(new_lst)
        
        if isinstance(other, Letter):
            return helper(self, other)
        
        else:
            final_word = self
            for i in other.letters:
                final_word = helper(final_word, i)
            return final_word
        
    def __repr__(self):
        return ", ".join((str(letter) for letter in self.letters))
        
    def get_lst(self):
        return self.letters
        
    def __len__(self):
        return len(self.letters)
        
    def inverse(self):
        new_word = Word([])
        for letter in self.letters[::-1]:
            new_word += letter.inverse()
        return new_word
        
    def get_total_power(self):
        return sum(map(lambda x : abs(x.get_power()), self.letters))
        
    #Creates a word from the current printed version of the word
    @staticmethod
    def create_word(string):
        string_letter_lst = string.split(", ")
        string_letter_converter = lambda x : Letter(x.split('^')[0], \
                int(x.split('^')[1]))
        return Word(list(map(string_letter_converter, string_letter_lst)))
            

def create_empty_word():
    return Word([])
        
#Using a pre-determined letter_table and a word, we convert it into its final matrix.
def matrix_word(word, letter_table):
    letters = word.get_lst()
    matrix = AB_Matrix.convert_to_AB_matrix(Matrix.get_identity(2))
    for letter in letters:
        matrix *= letter_table.get_matrix(letter)
    return matrix

#Testing

empty = create_empty_word()
l1 = Letter('a', 1)
l2 = Letter('a', 5)
l3 = Letter('a', -5)
l4 = Letter('b', 7)
l5 = Letter('b', -8)
w2 = l2 + l3 + l5 + l4 + l2 + l1 + l5
w3 = w2 + l2 + l4
w4 = w2 + w3