from algo_clean import *

#Algorithms
from algorithms.naive_killer_list import *
from algorithms.naive_algo import Naive_Algo as Naive

NUM_TESTS = 5000

#Runs through denominators 2 to 10 and rational numbers > 0 and < 4
def test1(algo):
    excep = []
    for r in range(2, 11):
        for s in range(2, 4 * r):
            print("num:", (s, r))
            if not run_algo(s, r, NUM_TESTS, algo):
                excep.append((s, r))
    print(excep)

#Runs the algorithm 'repeats' number of times for the Random selection
def test2(s, r, algo, repeats):
    count = 0
    for i in range(repeats):
        if i % (repeats // 10) == 0: print(str(i // (repeats // 10)) + "0%")
        if run_algo(s, r, NUM_TESTS, algo): count += 1
    print(count)
        
def shortest_search(s, r, algo, repeats):
    shortest = None
    second_shortest = None
    for i in range(repeats):
        if i % (repeats // 10) == 0: print(str(i // (repeats // 10)) + "0%")
        lst, algo_instance, is_completed = run_algo_details(s, r, NUM_TESTS, algo)
        if is_completed and shortest == None:
            shortest = algo_instance
        elif is_completed and len(shortest.get_word()) > len(algo_instance.get_word()):
            second_shortest = shortest
            shortest = algo_instance
    return shortest, second_shortest
    
def test1_shortest(algo, repeats):
    excep = []
    for r in range(2, 11):
        for s in range(2, 4 * r):
            if math.gcd(s, r) != 1: continue
            print("num:", (s, r))
            shortest = None
            for i in range(repeats):
                lst, algo_instance, is_completed = run_algo_details(s, r, NUM_TESTS, algo)
                if is_completed and shortest == None:
                    shortest = algo_instance
                elif is_completed and len(shortest.get_word()) >= \
                        len(algo_instance.get_word()):
                    shortest = algo_instance
                    if len(shortest.get_word()) <= 20:
                        break
            if shortest == None: 
                print("Unable to find")
                continue
            print("length:", len(shortest.get_word()))
            print("word:", shortest.get_word())
            print("matrix:", matrix_word(shortest.get_word(), \
                    shortest.get_letter_table()), "\n")
        
    
#Test 2 algorithms and compare their word length generation for test1
def test3(algo1, algo2):
    for r in range(2, 11):
        for s in range(2, 4 * r):
            lst11, algo_instance1, is_completed1 = run_algo_details(s, r, NUM_TESTS, algo1)
            if lst11 == None:
                continue
            length1 = len(algo_instance1.get_word()) if is_completed1 else -1
            lst2, algo_instance2, is_completed2 = run_algo_details(s, r, NUM_TESTS, algo2)
            length2 = len(algo_instance2.get_word()) if is_completed2 else -1
            print("(%d, %d): Closest_Naive:" % (s, r), length1, "Closest_Combined:", length2)
                    
#Test 2 algorithms and compare their word length generation for a specific s, r value
def test4(s, r, algo1, algo2):
    tree1, algo_instance1 = run_algo_details(s, r, NUM_TESTS, algo1)
    tree2, algo_instance2 = run_algo_details(s, r, NUM_TESTS, algo2)
    print("(%d, %d): algo1:" % (s, r), algo_instance1.get_word(), "algo2:", \
            algo_instance2.get_word())

#Tests the 2nd batch of values
def test5(algo):
    excep = []
    for s in range(2, 31):
        for r in range(2, 10 * s + 1):
            print("num:", (s, r))
            if math.gcd(s, r) == 1 and not run_algo(s, r, NUM_TESTS, algo):
                excep.append((s, r))
    print(excep)
    
#Test 2 algorithms and compare their word length generation for test5
def test6(algo1, algo2):
    for s in range(2, 31):
        for r in range(2, 10 * s + 1):
            lst1, algo_instance1, is_completed1 = run_algo_details(s, r, NUM_TESTS, algo1)
            if lst1 == None:
                continue
            lst2, algo_instance2, is_completed1 = run_algo_details(s, r, NUM_TESTS, algo2)
            if len(algo_instance1.get_word()) > 10:
                print("(%d, %d): Closest_Naive:" % (s, r), \
                        len(algo_instance1.get_word()), "Closest_Combined:", \
                        len(algo_instance2.get_word()))
 
DENOMINATOR = 115
#Tests the 2nd batch of values
def test7(algo):
    excep = []
    for r in range(2, DENOMINATOR + 1):
        for s in range(2, r + 1):
            if math.gcd(s, r) != 1:
                continue
            print("num:", (s, r))
            if not run_algo(s, r, NUM_TESTS, algo):
                print("unable to find")
                excep.append((s, r))
            print()
    print(excep)
    