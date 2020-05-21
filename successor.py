"""
4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) 
of a given node in a binary search tree. You may assume that each node has a link to 
its parent.

Hints: #79, #91
"""

def get_in_order_successor(node, value):
    # base case
    if node is None:
        return None
    value = None
    if node.right != None:
        if node.right.left == None and node.right.right == None:
            get_in_order_successor()
        

class Node:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, data, parent=None):
        if self.data != None:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryNode(data, parent)
                else:
                    self.left.insert(data, parent)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryNode(data, parent)
                else:
                    self.right.insert(data, parent)
        else:
            self.data = data


if __name__ == "__main__":
    root = Node()
    root.insert(20)
    root.insert(10)
    root.insert(7)
    root.insert(18)
    root.insert(17)
    root.insert(50)
    root.insert(70)
    root.insert(30)
    root.insert(25)
    root.insert(35)
    root.insert(33)
    root.insert(40)
    print(root.parent)