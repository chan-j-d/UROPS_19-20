import sys

from killer_intervals.interval_chooser.interval_chooser_interface import *

class Smallest_Ratio_Interval_Chooser(Interval_Chooser_Interface):

    def choose_interval(self, number, interval_lst):
        
        interval_lst.sort(key=lambda x : abs(number - x.get_midpoint()) / x.range())

        return interval_lst[0]