#Class representing a Node with a number.
class Tree_Node:
        
    def __init__(self, number, tree=None):
        self.number = number
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.tree = tree
    
    def __repr__(self):
        return "(Num: %s, Height: %d)" % (str(self.number), self.height)
            
    def get_left_height(self):
        if self.left == None:
            return -1
        else:
            return self.left.height
        
    def get_right_height(self):
        if self.right == None:
            return -1
        else:
            return self.right.height
            
    def is_left_child(self):
        return self == self.parent.left
            
    def is_right_child(self):
        return self == self.parent.right
            
    def is_root(self):
        return self.parent == None
        
    #Note that the set_left/right function automatically gives the child node its parents information.
    def set_left(self, node):
        self.left = node
        if node != None:
            node.parent = self
            
    def set_right(self, node):
        self.right = node
        if node != None:
            node.parent = self
            
    def is_imbalanced(self):
        return abs(self.get_left_height() - self.get_right_height()) >= 2
            
    def is_leaf(self):
        return self.left == None and self.right == None
            
    def left_heavy(self):
        return self.get_left_height() > self.get_right_height()
        
    def is_balanced(self):
        return self.get_left_height() == self.get_right_height()
            
    def right_heavy(self):
        return self.get_left_height() < self.get_right_height()
         
    #Updates own height
    def update_height(self):
        new_height = max(self.get_left_height(), self.get_right_height()) + 1
        if new_height != self.height:
            self.height = new_height
            return True
        else: 
            return False
        
    #Left rotation for rebalancing
    def left_rotate(self):
        
        #Transferred child node
        transferred_node = self.right.left
        #Immediate parent node
        parent_node = self.parent
        #print("left rotate2:", self, transferred_node, parent_node)
        #Determines if current node is the root.
        if parent_node != None:
            #Determine if the current node was a left or right child
            if self.is_left_child():
                is_left = True
            else:
                is_left = False
        
        #Re-ordering child/parent pointers
        self.right.set_left(self)
        self.set_right(transferred_node)
        self.update_height()
        self.parent.update_height()
        #print("left rotate2:", self, transferred_node, parent_node)
        
        #Reconnects parent node
        if parent_node != None:
            if is_left:
                parent_node.set_left(self.parent)
            else:
                parent_node.set_right(self.parent)
        else:
            self.parent.parent = None
            self.parent.tree = self.tree
            self.tree.root = self.parent

        
    #Right rotation for rebalancing
    def right_rotate(self):
        
        #Transferred child node
        transferred_node = self.left.right
        #Immediate parent node
        parent_node = self.parent
        
        #Determines if current node is the root.
        if parent_node != None:
            #Determine if the current node was a left or right child
            if self.is_left_child():
                is_left = True
            else:
                is_left = False

        #Re-ordering of child/parent pointers
        self.left.set_right(self)
        self.set_left(transferred_node)
        self.update_height()
        self.parent.update_height()
        #print("right rotate:", self, transferred_node)
        
        #Reconnects parent node
        if parent_node != None:
            if is_left:
                parent_node.set_left(self.parent)
            else:
                parent_node.set_right(self.parent)
        else:
            self.parent.parent = None
            self.parent.tree = self.tree
            self.tree.root = self.parent

        
    def rebalance(self):
        
        #If height is unchanged, no need to touch any nodes further up.
        if self.update_height():
        
            #Checks to see if rebalancing is needed.
            if self.is_imbalanced():
                #print("rebalance (not balanced):", self, "1eft:", self.left, "right:", self.right)
                if self.left_heavy():
                    if not self.left.right_heavy():
                        self.right_rotate()
                    else:
                        self.left.left_rotate()
                        self.right_rotate()
                elif self.right_heavy():
                    if not self.right.left_heavy():
                        self.left_rotate()
                    else:
                        self.right.right_rotate()
                        self.left_rotate()
                
                if not self.parent.is_root():
                    self.parent.parent.rebalance()
            
            #If not the root, then recurse upwards
            if not self.is_root():
                self.parent.rebalance()
                    
        
    def __lt__(self, other):
        return self.number < other.number
            
    def __le__(self, other):
        return self.number <= other.number
        
    def __eq__(self, other):
        if other == None:
            return False
        return self.number == other.number
            
    def __gt__(self, other):
        return self.number > other.number
            
    def __ge__(self, other):
        return self.number >= other.number

#Self-balancing dynamic binary search tree.
#Numbers are on all nodes in the tree.
class AVL_Tree:            
    
    def __init__(self):
        self.root = None
        
    #adds a number to the tree
    def add_number(self, number):
        
        
        if self.root == None:
            self.root = Tree_Node(number, self)
            return
        
        new_node = Tree_Node(number)
        
        #Starting node to recurse on is the root node.
        current_node = self.root
        
        while (True):
            
            #Go left
            if new_node < current_node:
                
                #If .left is None then we place the node there.
                if current_node.left == None:
                    current_node.set_left(new_node)
                    break
                else:
                    current_node = current_node.left
            
            else:
                
                if current_node.right == None:
                    current_node.set_right(new_node)
                    break
                else:
                    current_node = current_node.right

        #checks for need to rebalance
        current_node.rebalance()
            
            
    def search_and_add(self, number):
        
        if self.root == None:
            self.root = Tree_Node(number, self)
            return False
            
        new_node = Tree_Node(number)
            
        #Starting node to recurse on is the root node
        current_node = self.root
        
        while (True):
            
            #number found
            if new_node == current_node:
                return True
            
            #Go left
            if new_node < current_node:
                
                #If .left is None then we place the node there.
                if current_node.left == None:
                    current_node.set_left(new_node)
                    break
                else:
                    current_node = current_node.left
            
            else:
                
                if current_node.right == None:
                    current_node.set_right(new_node)
                    break
                else:
                    current_node = current_node.right

        #checks for need to rebalance
        current_node.rebalance()
        return False
                
    
    #In-order traversal for checking
    def in_order_traversal(self):
        
        def helper(node):
            if node == None:
                return []
            else:
                lst = helper(node.left)
                lst.append(node)
                lst.extend(helper(node.right))
                return lst
                
        return helper(self.root)
        
    def check_balance(self):
        def node_balanced(node):
            if node.is_imbalanced():
                print(node)
                return False
            if node.left != None:
                if not node_balanced(node.left):
                    return False
            if node.right != None:
                if not node_balanced(node.right):
                    return False
            return True
            
        return node_balanced(self.root)
        

import random
import sys
path = 'C:/Users/raido/Desktop/NUS/NUS Year 1 Sem 2/UROPS/v2'
if path not in sys.path:
    sys.path.append(path)
from basic_packages.rational_special import *
    
def test():
    tree = AVL_Tree()
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
    print(tree.check_balance())
    print(len(lst))
        

def test2():
    tree = AVL_Tree()
    for i in range(10):
        tree.search_and_add(i)
    print(tree.in_order_traversal())
    print(tree.check_balance())
        
    
    