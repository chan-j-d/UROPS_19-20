import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
    
from algorithms.naive_killer_algo import *
from algorithms.naive_killer_algo2 import *

#Interval choosing algorithm.
from killer_intervals.interval_provider_lst import *

class F_L_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_L_N_Provider)
        
class F_R_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_R_N_Provider)
        
class S_R_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, S_R_N_Provider)
        
class F_C0_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_C0_N_Provider) 
               
class F_CB0_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_CB0_N_Provider)
        
class F_CA0_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_CA0_N_Provider)
        
class F_CH_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_CH_N_Provider)
        
class F_COr_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_COr_N_Provider)
        
class F_S_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_S_N_Provider)
        
class L_S_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, L_S_N_Provider)
        
class F_C_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_C_N_Provider)
        
class R_R_N(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, R_R_N_Provider)
        
#Original
class F_R_NU(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_R_NU_Provider)
        
class F_R_S(Naive_Killer_Algo2):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_R_S_Provider)
        
class F_R_CG(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, F_R_CG_Provider)
        
class S_S_CG(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, S_S_CG_Provider)
        
class Closest_Combined(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, Closest_Combined_Provider)
        
class Closest_Naive(Naive_Killer_Algo):
    
    def __init__(self, s, r):
        super().__init__(s, r, Closest_Naive_Provider)
        
class Closest_Simple_Overall(Naive_Killer_Algo2):
    
    def __init__(self, s, r):
        super().__init__(s, r, Closest_Simple_Provider)