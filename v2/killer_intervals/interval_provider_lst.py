from killer_intervals.interval_provider import Interval_Provider
from killer_intervals.generators import *
from killer_intervals.matrix_chooser import *
from killer_intervals.interval_chooser import *
from killer_intervals.interval_closest_provider import *

#List of commonly used interval providers

class F_R_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                random_chooser.Random_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class F_C0_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                closest_zero_chooser.Closest_Zero_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class F_CB0_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                closest_below_zero_chooser.Closest_Below_Zero_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class F_CA0_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                closest_above_zero_chooser.Closest_Above_Zero_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class F_CH_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                closest_half_chooser.Closest_Half_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class F_COr_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                closest_original_chooser.Closest_Original_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
        
class F_L_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                largest_ratio_chooser.Largest_Ratio_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class F_S_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                smallest_ratio_chooser.Smallest_Ratio_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class L_S_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, largest_ratio_interval_chooser.Largest_Ratio_Interval_Chooser, \
                smallest_ratio_chooser.Smallest_Ratio_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
                
class R_R_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, random_midpoint_chooser.Random_Midpoint_Chooser, \
                random_chooser.Random_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)
  
#Original
class F_R_NU_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                random_chooser.Random_Chooser, \
                naive_unique_interval_generator.Naive_Unique_Interval_Generator)
                
class F_R_S_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                random_chooser.Random_Chooser, \
                naive_simple_generator.Naive_Simple_Generator)
                
class F_R_CG_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, furthest_midpoint_chooser.Furthest_Midpoint_Chooser, \
                random_chooser.Random_Chooser, \
                combined_interval_generator.Combined_Interval_Generator)    
                
class S_S_CG_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, smallest_ratio_interval_chooser.Smallest_Ratio_Interval_Chooser, \
                smallest_ratio_chooser.Smallest_Ratio_Chooser, \
                combined_interval_generator.Combined_Interval_Generator)  
                
class S_R_N_Provider(Interval_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, smallest_ratio_interval_chooser.Smallest_Ratio_Interval_Chooser, \
                random_chooser.Random_Chooser, \
                naive_interval_generator.Naive_Interval_Generator)  
                
class Closest_Combined_Provider(Interval_Closest_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, combined_interval_generator.Combined_Interval_Generator)
        
class Closest_Naive_Provider(Interval_Closest_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, naive_interval_generator.Naive_Interval_Generator)
        
class Closest_Simple_Provider(Interval_Closest_Provider):
    
    def __init__(self, s, r):
        super().__init__(s, r, naive_simple_generator.Naive_Simple_Generator)
                