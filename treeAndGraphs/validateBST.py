"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
Hints: #35, #57, #86, #113, #128
"""

from collections import deque

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value != None:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


def isBST(root):
    if root != None:
        isBST(root.left)
        isBST(root.right)
        leftResult = None
        rightResult = None
        if root.left != None:

            leftResult = (root.left.value <= root.value)
        if root.right != None:
            rightResult = (root.right.value > root.value)
        return leftResult!= False and rightResult!= False

if __name__ == "__main__":
    root = Node(-1)
    root.right = Node(-2)

    assert isBST(root) == False, "Fail to test"
    root.right = None
    assert isBST(root) == True, "Fail to test"
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)
    assert isBST(root) == True, "Fail to test"
