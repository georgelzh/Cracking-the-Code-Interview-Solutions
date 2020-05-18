"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
Hints: #35, #57, #86, #113, #128

O(N) time
O(H) space

If every node on the left must be less than or equal to the current node, then this is really
the same thing as saying that the biggest node on the left must be less than or equal to
the current node.

Rather than validating the current node's value against left T ree. max and
rightTree. min, can we flip around the logic? Validate the left tree's nodes to ensure
that they are smaller than current. value.

Think about the c h e ckBST function as a recursive function that ensures each node is
within an allowable (min, max) range. At first, this range is infinite. When we traverse
to the left, the min is negative infinity and the max is root. value . Can you implement
this recursive function and properly adjust these ranges as you traverse the tree?
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
    # use pre-order traversal to solve this problem
    if root != None:
        # initialize return value
        leftResult = None
        rightResult = None

        # check if the child nodes' values are within the range or not, return False if not.

        # make sure all values in node root.left's nodes and root.left are smaller or equal the root.value
        # so that all the left nodes will be less than or equal to the root.value
        if root.left != None:
            if root.left.value > root.value:
                return False
            leftNode = root.left
            leftLeftResult = None
            leftRightResult = None
            if leftNode.left!= None:
                leftLeftResult = leftNode.value <= root.value
            if root.left.right != None:
                leftRightResult = (leftNode.right.value > leftNode.value) and leftNode.right.value <= root.value
            leftResult = leftLeftResult and leftRightResult
        
        # make sure all values in node root.right's nodes and root.right bigger than the the root.value
        # then, make sure left node's value in rightNode of root is bigger than root's value, smaller than or euqal to rightNode's value
        # right node of root's right value must be bigger than the right node of root's value.
        if root.right != None:    
            if root.right.value < root.value:
                return False
            rightNode = root.right
            rightLeftResult = None
            rightRightResult = None

            if rightNode.left!= None:
                if rightNode.left != None:
                    rightLeftResult = (rightNode.left.value > root.value) and rightNode.left.value <= rightNode.value
            if rightNode.right != None:
                if rightNode.right != None:
                    rightRightResult = rightNode.right.value > rightNode.value
            rightResult = rightLeftResult and rightRightResult

        # return false if left or right node does not match its requirement and stop the program 
        # right away, which saves a lot of time bc there is no need to recursively call the function 
        # if we already know it's not BST
        if leftResult == False or rightResult == False:
            return False

        # if current node is good, then check subnodes
        else:
            if root.left != None:
                leftResult = isBST(root.left)
            if root.right != None:
                rightResult = isBST(root.right)

        # if none of return values are false, then we know it's a BST
        return leftResult!= False and rightResult!= False


if __name__ == "__main__":
    root = Node(-1)
    root.right = Node(-2)

    assert isBST(root) == False, "Fail to test"
    root.right = None
    # assert isBST(root) == True, "Fail to test"
    # root.insert(8)
    # assert root.right.value == 8, "Fail to test"

    # root.insert(15)
    # root.insert(6)
    # root.insert(9)
    # root.insert(13)
    # root.insert(16)
    # assert isBST(root) == True, "Fail to test"

    # root.insert(-9)
    # root.insert(-10)
    # # print((root.left).value)
    # # print((root.left.left).value)
    # root.left.right = Node(99)
    # # print((root.left.right).value)
    # assert isBST(root) == False, "Fail to test"
