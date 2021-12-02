import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)

#Own packages
from basic_packages.rational_special import *
from basic_packages.matrix_operations import *
from data_structures.tracking_tree import *
from basic_packages.words_package import *


def run_algo(s, r, n, Algo_Class):
    
    #Checks for already known cases
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return True
        
    #Hash Table tracker
    tracker = {}
    
    #Instantiates an Algorithm object (initiates the algorithm)
    algo = Algo_Class(s, r)
    
    #[1, 0] starting point representing infinity
    number = starting_point()
    
    #Run test n times
    for i in range(n):
        
        
        #Get next matrix and multiply
        matrix = algo.get_next_matrix(number)
        number *= matrix
        
        #print(number)

        #Checks that the number has returned to infinity
        if number.get_q() == 0:
            lst = list(tracker.keys())
            lst.insert(0, starting_point())
            lst.append(number)
            
            #print(lst)
            print("length:", len(algo.get_word()))
            print("word:", algo.get_word())
            print("matrix:", algo.get_matrix())
            return True
        
        #Checks that the number has looped
        elif number in tracker:
            print("repeated")
            lst = list(tracker.keys())
            lst.insert(0, starting_point())
            lst.append(number)
            
            #Comment out the below code block for accurate word looping
            word = algo.get_word()
            prev_word = tracker[number]
            final_word = word + prev_word.inverse()
            #print(lst)
            print("length:", len(final_word))
            print("word:", final_word)
            print("matrix:", matrix_word(final_word, algo.get_letter_table()))
            
            #Comment out the above block for improved performance without storing the word
            #in the hashtable
            #print(lst)
            #print(len(algo.get_word()))
            #print(algo.get_word())
            #print(algo.get_matrix())
            
            return True
            
        #Adds the number to the hashtable with its corresponding word
        else:
            #tracker[number] = 1
            tracker[number] = algo.get_word()
            
    #print(list(tracker.keys()))
    return False


#Method that returns the list of numbers and algorithm details.
def run_algo_details(s, r, n, Algo_Class):
    
    if abs(s / r) >= 4 or math.gcd(s, r) != 1 or s % r == 0:
        return None, None, None
        
    tracker = {}
    
    algo = Algo_Class(s, r)
    
    number = starting_point()

    lst = []
    
    is_completed = False
    
    for i in range(n):
        
        matrix = algo.get_next_matrix(number)
        number *= matrix
        
        if number.get_p() * number.get_q() == 0:
            lst = list(tracker.keys())
            lst.insert(0, starting_point())
            lst.append(number)
            is_completed = True
            break
            
        elif number in tracker:
            lst = list(tracker.keys())
            lst.insert(0, starting_point())
            lst.append(number)
            
            word = algo.get_word()
            prev_word = tracker[number]
            final_word = word + prev_word.inverse()
            algo.word = final_word
            is_completed = True
            break
            
        else:
            tracker[number] = algo.get_word()
            
    return lst, algo, is_completed