from killer_intervals.interval_chooser.interval_chooser_interface import *

class Closest_Midpoint_Chooser(Interval_Chooser_Interface):
    
    def choose_interval(self, number, interval_lst):
        
        interval_lst.sort(key=lambda x : abs(number - x.get_midpoint()))
 
        return interval_lst[0]
