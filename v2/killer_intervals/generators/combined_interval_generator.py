from killer_intervals.generators.interval_generator_package import *
from killer_intervals.generators.naive_interval_generator import *
from killer_intervals.generators.AC_interval_generator import *
from killer_intervals.generators.R_interval_generator import *

class Combined_Interval_Generator(Interval_Generator_Interface):
    
    def __init__(self, s, r, size):
        self.s = s
        self.r = r
        self.size = size
        
    def generate_intervals(self):
        naive_generator = Naive_Interval_Generator(self.s, self.r, self.size)
        ac_generator = AC_Interval_Generator(self.s, self.r, self.size)
        r_generator = R_Interval_Generator(self.s, self.r, self.size)
        interval_lst = naive_generator.generate_intervals()
        interval_lst.extend(ac_generator.generate_intervals())
        interval_lst.extend(r_generator.generate_intervals())
        return interval_lst