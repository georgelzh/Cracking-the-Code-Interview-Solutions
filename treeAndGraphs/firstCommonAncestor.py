"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Hints: #70, #76, #28, #36, #46, #70, #80, #96


if parent node is permited.

Here I will try to use a two while loop to tackle this problem.

the concept is to start with the two nodes' parents nodes.

1. first search through the entire tree to make sure that both nodes exist.

2. we go to the first node's parent node,
3. then check if right node's parent node equal to the first. if yes return, else: loop until the root. 
4. if first common ancestor is not found,  then we come back to the first node's parent's parent node.
5. repeat the process 2,3,4 until both first and second node reach its root node. if there is still none found, return False.

These two nodes probably are in different tree in this case.

this time, we will approach the problem using post-traversal if we assume the interviewer won't let us store node's parent.
procesures beint said below.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_common_ancestor(root, n1, n2):
    if root == None:
        return None
    if not covers(root, n1) or not covers(root, n2):
        return None
    else:
        return common_anc_helper(root, n1, n2)

def common_anc_helper(root, n1, n2):
    # base case
    if root == None:
        return None
    # base case, if a node has no child node, then check if it's one of the input node,
    # return (True, nodevalue) if found, else return None
    if root.left == None and root.right == None:
        if root.value == n1.value:
            return (True, n1)
        elif root.value == n2.value:
            return (True, n2)
        else:
            return None
    # visit the left
    leftResult = None
    if root.left != None:
        leftResult = common_anc_helper(root.left, n1, n2)
        # if leftResult != None:
            # print(leftResult)
            # print(root.value)
            # return leftResult

    # visit the right
    rightResult = None
    if root.right != None:
        rightResult = common_anc_helper(root.right, n1, n2)
        # if rightResult != None:
            # print(rightResult)
            # print(root.value)
            # return rightResult

    # visit curr, check if we found the ancestor of the two nodes. return curr
    # else return the found value if found any. if found none, return None
    # very important step here. because it needs to pass down the found value to
    # its parent node so that it could use it to compare.
    if leftResult != None and rightResult != None:
        return root
    elif leftResult != None:
        return leftResult
    elif rightResult != None:
        return rightResult
    else:
        return None

def covers(root, node):
    if root == None:
        return False
    if root == node:
        return True
    else:
        return covers(root.left, node) or covers(root.right, node)

import unittest

class TestFindAncestor(unittest.TestCase):

    def test_find_common_ancestor(self):
        self.assertEqual(1, 1)
        root = Node(10)
        root.left = Node(1)
        root.left.left = Node(7)
        root.left.left.left = Node(1000)
        root.left.left.left.right = Node(200)

        root.left.right = Node(22)
        root.right = Node(5)
        root.right.left = Node(120)
        root.right.left.left = Node(5)
        root.right.left.right = Node(3)

        root.right.right = Node(100)
        root.right.right.right = Node(4)

        self.assertEqual(find_common_ancestor(root, root.left.left.left.right, root.left.right).value, 1)
        self.assertEqual(find_common_ancestor(root, root.left.left.left.right, root.right).value, 10)
        self.assertEqual(find_common_ancestor(root, root.right.left.left, root.right.left.right).value, 120)
        self.assertEqual(find_common_ancestor(root, root.right, 99), None)


if __name__ == "__main__":
    unittest.main()