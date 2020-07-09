"""
Check Subtree: 
Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
Hints:#4, #11, #18, #31, #37

check all node in T1, if the node equals to the root node of T2, 
then, check if the subtree of the node in T1 is identical to the subtree of T2.
use recursion

This run time is O(n + km // k is number of time the root of t2 occurs in t1, usually smaller than this
memory O(log(n) + log(m)) // since value here is not stored. it's only compared. It saves memory

memory usage can be a problem for scalaibility, so this solution is really optimal for 
memory.

run time isnt too much different than the other solution. However, the worst case scenario
can go like O(n + km)
"""

import unittest


class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        if self.val != None:
            if val < self.val:
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

# check all the subtree of r1, return true if there's a subtree that's identical to r2
def subTree(r1, r2):
    if r1 == None:
        return False    # big tree is empty and t2 still not found
    elif r1.val == r2.val and matchTree(r1, r2) == True:
        # return true when root is identical, and r1 and r2's subtrees are identical too.
        return True
    return subTree(r1.left, r2) or subTree(r1.right, r2)   
    # else repeat this process above to the children of root node


# check if r1 is identical to r2
def matchTree(r1, r2):
    if r1 == None and r2 == None:   # when everything matches & no node left to compare
        return True
    elif r1 == None or r2 == None:
        return False
    elif r1.val != r2.val:
        return False
    else:
        return matchTree(r1.left, r2.left) and matchTree(r1.right, r2.right)
        # if both node has same value, and they are not None Node
        # check whether the children of two tree are identical.

def containsTree(t1, t2):
    if t2 == None:  # empty tree is always a subset
        return True
    return subTree(t1, t2)



class Test(unittest.TestCase):
    def test_subTree(self):
        root = Node(100)
        root.insert(50)
        root.insert(200)
        root.insert(25)
        root.insert(70)
        root.insert(150)
        root.insert(300)
        root.insert(400)
        root.insert(5)

        self.assertEqual(containsTree(root, root.right), True)
        t2 = Node(50)
        t2.insert(25)
        t2.insert(5)
        t2.insert(70)
        self.assertEqual(containsTree(root, t2), True)


if __name__ == "__main__":
    unittest.main()