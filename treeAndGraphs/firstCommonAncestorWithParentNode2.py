"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Hints: #70, #76, #28, #36, #46, #70, #80, #96


if parent node is permited.

Similar to the earlier approach, we could trace p's path upwards and check if any of the nodes cover q.
The first node that covers q (we already know that every node on this path will cover p) must be the first
common ancestor.

Observe that we don't need to re-check the entire subtree. As we move from a node x to its parent y, all the
nodes under x have already been checked for q. Therefore, we only need to check the new nodes "uncovered';
which will be the nodes under x's sibling.

the code might explain itself. check it out
"""
import unittest

def find_common_ancestor(root, n1, n2):
    """
    check if both node exists in the tree
    check if either one of the node covers the other node.
    """
    if not covers(root, n1) or not covers(root, n2):
        return None
    if covers(n1, n2):
        return n1
    elif covers(n2, n1):
        return n2
    
    sibling = get_sibling(n1)
    parent = n1.parent

    while not covers(sibling, n2):
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent


def get_sibling(n):
    if n == None or n.parent == None:
        return None
    parent = n.parent
    return parent.left if parent.left != n else parent.right

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
python ternary operator
https://en.wikipedia.org/wiki/%3F:#Python
"""