class Interval_Collection:
    
    def __init__(self):
        self.interval_lst = []
        
    def append(self, interval):
        if interval in self.interval_lst:
            index = self.interval_lst.index(interval)
            old_interval = self.interval_lst[index]
            old_interval.append(interval)
        else:
            self.interval_lst.append(interval)
            
    def extend(self, interval_collection):
        for interval in interval_collection.interval_lst:
            self.append(interval)
            
    def get_interval_lst(self):
        return self.interval_lst
            
    def __contains__(self, item):
        return item in self.interval_lst