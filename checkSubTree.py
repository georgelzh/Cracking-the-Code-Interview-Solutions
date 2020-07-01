"""
Check Subtree: 
Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
Hints:#4, #11, #18, #31, #37

my own solution
O(T1 + T2)
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

def pre_traverse(root):
    val_list = []
    if root == None:
        return val_list
    else:
        # to the root
        val_list.extend([root.val])

        # traverse to the left
        if root.left != None:
            val_list.extend(pre_traverse(root.left))

        # to the right
        if root.right != None:
            val_list.extend(pre_traverse(root.right))
    return val_list

def check_subtree(t1, t2):
    if t1 == None:
        return False
    elif t2 == None:
        return True
    # traverse also takes less space than recursion
    # traverse t2 and get an list of all the vals for later comparison
    t2_traversal_val_list = pre_traverse(t2)

    # do the same to t1
    t1_traversal_val_list = pre_traverse(t1)

    # check if t1 val list includes t2s or not.
    t1_val_len = len(t1_traversal_val_list)
    t2_val_len = len(t2_traversal_val_list)
    curr = 0
    while curr < t1_val_len:
        # no need to keep checking if the rest of the t1 has less 
        # than the amount of values in t2, return False
        if (t1_val_len - curr) < t2_val_len:
            return False 

        # if the element in t1 mathces the root val of t2,
        # then compare all the rest part check if they are identical.
        # return true if yes, else continue checking the rest of t1
        elif t1_traversal_val_list[curr] == t2_traversal_val_list[0]:
            t1_includes_t2 = True
            for val in t2_traversal_val_list:
                if t1_traversal_val_list[curr] != val:
                    t1_includes_t2 = False
                    break
                else:
                    curr += 1
            if t1_includes_t2:
                return True
        else:
            curr += 1

class Test(unittest.TestCase):
    def test_pre_traversal(self):
        root = Node(100)
        root.insert(50)
        root.insert(200)
        root.insert(25)
        root.insert(70)
        root.insert(150)
        root.insert(300)
        root.insert(400)
        root.insert(5)
        pre_traverse_output = [100, 50, 25, 5, 70, 200, 150, 300, 400]
        real_output = pre_traverse(root)
        print(real_output)
        self.assertEqual(real_output, pre_traverse_output)
        self.assertEqual(check_subtree(root, root.right), True)

        t2 = Node(50)
        t2.insert(25)
        t2.insert(5)
        t2.insert(70)
        self.assertEqual(check_subtree(root, t2), True)


if __name__ == "__main__":
    unittest.main()