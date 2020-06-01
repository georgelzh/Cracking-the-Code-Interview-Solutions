"""
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

eg:
    2
1       3

output: {2,1,3}, {2,3,1}
Hints: #39, #48, #66, #82

"""
from collections import deque
import copy

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data != None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findVal(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + " not found"
            else:
                return self.left.findVal(data)
        if data > self.data:
            if self.right is None:
                return str(data) + " not found"
            else:
                return self.right.findVal(data)
        else:
            return str(data) + " is found"

# in-order traversal: left, current, right
    def printTree(self):
        # there are many ways to print the data, here we use In Order
        if self.data != None:
            if self.left != None:
                self.left.printTree()
            print( self.data)
            if self.right != None:
                self.right.printTree()

def find_BST_sequence(root):
    result = deque()
    if root == None:
        return result
    prefix = deque()
    prefix.append(root.data)

    # recurse on left and right subtrees
    leftSeq = find_BST_sequence(root.left)
    rightSeq = find_BST_sequence(root.right)

    if len(leftSeq) == 0 and len(rightSeq) == 0:
        return deque([prefix])

    # weave together each list from the left and right side
    # print("leftSeq: ", leftSeq)
    # print("rightSeq: ", rightSeq)
    if len(leftSeq) > 0 and len(rightSeq) > 0:
        for left in leftSeq:
            for right in rightSeq:
                if len(right) == 0:
                    right = deque()
                weaved = deque()
                # print("left and right: ", left, right)
                weave_list(left, right, weaved, prefix)
                result += weaved
        return result
    else:
        left_has_element = True if len(leftSeq) > 0 else False
        if left_has_element == True:
            right = deque()
            for left in leftSeq:
                weaved = deque()
                # print("left and right: ", left, right)
                weave_list(left, right, weaved, prefix)
                result += weaved
            return result
        else:
            left = deque()
            for right in rightSeq:
                weaved = deque()
                # print("left and right: ", left, right)
                weave_list(left, right, weaved, prefix)
                result += weaved
            return result

def weave_list(first, second, results, prefix):
    # print("prefix: ", prefix)
    # if one of the list is empty add remainder to [a cloned] prefix and store result
    if len(first) == 0 or len(second) == 0:
        result = copy.deepcopy(prefix)
        result += first
        result += second
        # print("result: ", result)
        results.append(result)
        return
    
    # resurse with head of first added to the prefix, removing the head will damage 
    # first, so we will need to put it back where we found it afterwards
    head_first = first.popleft()
    prefix.append(head_first)
    weave_list(first, second, results, prefix)
    prefix.pop()
    first.appendleft(head_first)

    # do the same to the second
    head_second = second.popleft()
    prefix.append(head_second)
    weave_list(first, second, results, prefix)
    prefix.pop()
    second.appendleft(head_second)


import unittest

class TestFindBSTSequence(unittest.TestCase):
    def test_find_BST_sequence(self):
        root = Node(-1)
        root.insert(2)
        root.insert(0)
        root.insert(12)
        root.insert(5)
        root.insert(2)
        root.insert(13)

        sequence_list = find_BST_sequence(root)
        print(sequence_list)

if __name__ == "__main__":
    unittest.main()


"""
reference:
https://gist.github.com/kean/40a1e592a608154b117a0dac48baf25f
https://github.com/w-hat/ctci-solutions/blob/master/ch-04-trees-and-graphs/09-bst-sequences.py
"""