import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
from data_structures.avl_tree_package import *

def create_new_tree():
    return Tracking_Tree()

class Tracking_Tree(AVL_Tree):
    
    def __init__(self):
        super().__init__()
        self.number_lst = []
        
    def search_and_add(self, number):
        self.number_lst.append(number)
        return super().search_and_add(number)
        
    def get_number_lst(self):
        return self.number_lst
        
from basic_packages.rational_special import *
    
def test():
    tree = Tracking_Tree()
    lst = []
    total = 0
    for i in range(-100, 100):
        if i == 0:
            continue
        for j in range(1, 10):
            total += 1
            lst.append(Rational_Special(i, j))
    random.shuffle(lst)
    found_count = 0
    for q in lst:
        if tree.search_and_add(q):
            found_count += 1
    lst = tree.in_order_traversal()
    print(lst)
    print(tree.get_number_lst())
    print(len(lst))
    print(found_count, len(lst), total)