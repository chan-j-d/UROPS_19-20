import random

from killer_intervals.interval_chooser.interval_chooser_interface import *

class Random_Midpoint_Chooser(Interval_Chooser_Interface):

    def choose_interval(self, number, interval_lst):
        
        #Chooses a random index to select an interval to be used
        return interval_lst[random.randint(0, len(interval_lst) - 1)]