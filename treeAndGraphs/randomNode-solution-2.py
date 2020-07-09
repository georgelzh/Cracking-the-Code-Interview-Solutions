#!Python3
"""
4.11
Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
Hints: #42, #54, #62, #75, #89, #99, #112, #119

Option #7 [Fast & Working]
Random number calls can be expensive. If we'd like, we can reduce the number of random number calls
substantially.

But what if we went right instead? We have a number between 7 and 8 (inclusive) but we would need a
number between O and 1 (inclusive). That's easy to fix:just subtract out LEFT _SIZE + 1.

The initial random number call indicates which node
(i) to return, and then we're locating the ith node in an in-order traversal. Subtracting LEFT _SIZE + 1
from i reflects that, when we go right, we skip over LEFT _SIZE + 1 nodes in the in-order traversal.
"""

# bST Node class
from random import randint

class Tree:
    def __init__(self):
        self.root = Node()
        
    def size(self):
        return self.root.size

    def get_random_node(self):
        if self.root.val == None:
            return None
        else:
            # get random int
            i = randint(0, (self.size() -1))
            return self.root.get_ith_node(i)
    
    def insert(self, val):
        if self.root.val == None:
            self.root.val = val
        else:
            self.root.insert(val)

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.size = 0
        if self.val != None:
            self.size += 1

    def insert(self, val):
        if self.val != None:
            if val > self.val:
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
            elif val < self.val:
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            self.size += 1
        else:
            self.val = val
            self.size += 1

    def get_ith_node(self, i):
        left_size = self.left.size if self.left != None else 0
        # traverse to the ith node
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self.val
        else:
            return self.right.get_ith_node(i - (left_size + 1))

            """
            since the order of insertion is in-order,
            the ith here we mean the ith node of the tree
            therefore, before we traverse to the right,
            we take subtract all left nodes + root node out 
            by getting self.right.get_ith_node(i - (left_size + 1))
            because how the traverse is writte, it traverse to the left
            according to the left_size, when it reaches to the right,
            it again is decided by the left_size, however, left_size
            in this case is the left_size of the current node after traverse to the right.

            If you can't understand this algorithm, walk through this algorithm with the
            tree I provided in the bottom of this code. you will understand how it works.
            """
    def find(self, val):
        if val == self.val:
            return self
        elif val < self.val:
            if self.left == None:
                return None
            else:
                return self.left.find(val)
        elif val > self.val:
            if self.right == None:
                return None
            else:
                return self.right.find(val)
        else:
            return None

if __name__ == "__main__":
    t = Tree()
    t.insert(-1)
    t.insert(2)
    t.insert(0)
    t.insert(12)
    t.insert(5)
    t.insert(2)

    print(t.get_random_node())

"""
use this tree to understand the get_ith_node function
index starts from 0
so the max index will be 5 for this tree

            2
        1          5
    -1         4       9
"""