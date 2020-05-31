"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Hints: #70, #76, #28, #36, #46, #70, #80, #96

node  does not have parent link

Alternatively, you could follow a chain in which p and q are on the same side. That is, if p and q are both on
the left of the node, branch left to look for the common ancestor. If they are both on the right, branch right
to look for the common ancestor. When p and q are no longer on the same side, you must have found the
first common ancestor.

"""
import unittest

def find_common_ancestor(root, n1, n2):
    """
    check if both node exists in the tree
    check if either one of the node covers the other node.
    """
    if not covers(root, n1) or not covers(root, n2):
        return None
    return ancestor_helper(root, n1, n2)

def ancestor_helper(root, n1, n2):
    if root == None or root == n1 or root == n2:
        return root
    n1_is_on_left = covers(root.left, n1)
    n2_is_on_left = covers(root.left, n2)

    if n1_is_on_left != n2_is_on_left:
        return root
    
    # use the concept recurssion, just call this function itself
    next_branch = root.left if n1_is_on_left else root.right
    return ancestor_helper(next_branch, n1, n2)

def covers(root, n):
    if root == None:
        return False
    if root == n:
        return True
    return covers(root.left, n) or covers(root.right, n)

class Node:
    def __init__(self, value = None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class TestFindAncestor(unittest.TestCase):

    def test_find_common_ancestor(self):
        root = Node(10)
        root.left = Node(1, root)
        root.left.left = Node(7, root.left)
        root.left.left.left = Node(1000, root.left.left)
        root.left.left.left.right = Node(200, root.left.left.left)

        root.left.right = Node(22, root.left)
        root.right = Node(5, root)
        root.right.left = Node(120, root.right)
        root.right.left.left = Node(5, root.right.left)
        root.right.left.right = Node(3, root.right.left)

        root.right.right = Node(100, root.right)
        root.right.right.right = Node(4, root.right.right)
        # print(covers(root, None)) # False
        # print(get_siblings(root.right).value) #1
#################################################################
        n1 = root.left.left.left.right
        n2 = root.left.right
        # print(n1.value)
        # print(n2.value)
        # print(find_common_ancestor(n1, n2).value)

        self.assertEqual(find_common_ancestor(root, n1, n2).value, 1)
        n2 = root.right
        self.assertEqual(find_common_ancestor(root, n1, n2).value, 10)

        n1 = root.right.left.right
        n2 = root.right.left.left

        self.assertEqual(find_common_ancestor(root, n2, n1).value, 120)


if __name__ == "__main__":
    unittest.main()
"""
This algorithm runs in O(n) time on a balanced tree. This is because c overs is called on 2n nodes in the
first call (n nodes for the left side, and n nodes for the right side). After that the algorithm branches left or
right, at which point c overs will be called on 2rz nodes, then 2X, and so on. This results in a runtime
ofO(n).
We know at this point that we cannot do better than that in terms of the asymptotic runtime since we need
to potentially look at every node in the tree. However, we may be able to improve it by a constant multiple.
"""

"""
reference other than the book:
python ternary operator
https://en.wikipedia.org/wiki/%3F:#Python
"""