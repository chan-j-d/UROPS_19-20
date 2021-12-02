import random

#Basic packages    
from basic_packages.matrix_operations import *
from basic_packages.words_package import *
from basic_packages.interval_package import *
from basic_packages.letters import *

from algorithms.algo_interface import *

SIZE = 10
THRESHOLD = 0

class Naive_Killer_Algo2(Algo_Interface):
    
    def __init__(self, s, r, Interval_Provider):
        super().__init__(s, r)
        self.count = 0
        self.principal_range = Interval(create_q(-1, 2), create_q(1, 2))
        
        #Keeps track of the word
        self.word = create_empty_word()
        
        #Table of letters used
        R_algo_table = {'a': a_n, 'c': lambda n : c_n(self.s, n), \
                'r': lambda n : r_n(self.s, self.r, n), \
                'b': lambda n : b_n(self.s, self.r, n)}
        self.table = Letter_Table(R_algo_table)

        #create interval_provider
        self.interval_provider = Interval_Provider(s, r)
        
        #boolean to check whether the next is an a_reduce operation or killer_interval/b_reduce
        self.a_step = True
        self.killer_used = False

        
    def get_next_matrix(self, number):
        
        #First iteration converts to (r, s)
        if self.count == 0:
            self.count += 1
            #start
            letter = Letter('b', (self.r - SR(self.r, self.s)) // self.s)
            self.word += letter
            
            return self.table.get_matrix(letter) 
        
        #a_reduce step
        elif self.a_step:        
            self.count += 1
            #Reduction of numerator by 'a' matrix
            if self.killer_used:
                a_letter = Naive_Killer_Algo2.a_reduce2(number)
                self.killer_used = False
            else: a_letter = Naive_Killer_Algo2.a_reduce(number)
            a_matrix = self.table.get_matrix(a_letter)
            
            self.word += a_letter  
            
            #change next_step to a_step
            self.a_step = False

            return a_matrix
            
        #non a_reduce step
        else:
            #change the next step back to an a_reduce
            self.a_step = True
            
            p = number.get_p()
            q = number.get_q()
            if SR(self.r * q, p) == 0:
                #Change in numerator and denominator by 'b' matrix
                b_letter = Naive_Killer_Algo2.b_reduce(number, self.s, self.r)
                b_matrix = self.table.get_matrix(b_letter)
                
                #update word
                self.word += b_letter
                
                return b_matrix
            elif SR(q, self.s * p) == 0:
                print('wow!\n\n\n')
            
            #Checks to see if the number is contained within some killer interval
            #Can only be run after 2 'naive cycles' for some reason to avoid trivial words
            if self.count > 2 and self.interval_provider.in_interval(number) and \
                    self.principal_range.contains_inc(number):

                #print("killer_interval_used")

                #get interval from the Interval_Provider
                word, matrix = self.interval_provider.get_interval(number)

                #update word
                self.word += word
                
                self.killer_used = True
                
                #return matrix
                return matrix
                
            else:   
                #Change in numerator and denominator by 'b' matrix
                b_letter = Naive_Killer_Algo2.b_reduce(number, self.s, self.r)
                b_matrix = self.table.get_matrix(b_letter)
                
                #update word
                self.word += b_letter
                
                return b_matrix
                
                
    def get_word(self):
        return self.word
        
    def get_letter_table(self):
        return self.table
            
    #Reduces the numerator of the rational_special
    @staticmethod
    def a_reduce(number):
        x = number.get_p()
        s_y = number.get_q()
        new_x = SR(x, s_y)
        added_power = -((x - new_x) // (s_y))
        return Letter("a", added_power)
            
    @staticmethod
    def a_reduce2(number):
        x = number.get_p()
        s_y = number.get_q()
        new_x = SR2(x, s_y)
        new_x2 = SR(x, s_y)
        added_power = -((x - new_x) // (s_y)) 
        if added_power == 0 or (added_power != 1 and randomTrue(THRESHOLD)): added_power -= 1
        return Letter("a", added_power)
            
    @staticmethod
    def b_reduce(number, s, r):
        x = number.get_p()
        y = number.get_q() // s
        new_y = SR(r * y, x)
        added_power = -((r * y - new_y) // x)
        return Letter("b", added_power)
    
    @staticmethod
    def b_reduce2(number, s, r):
        x = number.get_p()
        y = number.get_q() // s
        new_y = SR2(r * y, x)
        added_power = -((r * y - new_y) // x)
        return Letter("b", added_power) 
        
def randomTrue(threshold):
    n = random.randint(0, 100)
    if n >= threshold:
        return True
    return False
           
            
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