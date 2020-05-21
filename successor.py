"""
4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) 
of a given node in a binary search tree. You may assume that each node has a link to 
its parent.

Hints: #79, #91

1. handle root node and none.
2. if node.right exists, traverse to the leftmost node of its subtree then return, if no subtree. just return.
3. if node.right does not exist, then traverse back to parent until the curr.value > than the (input) node.value
4. handle case when its the largest node, it has no successor. returns None

"""

def get_in_order_successor(node, value):
    # base case
    if node is None or (node.right is None and node.parent is None):
        return None

    # visit right
    if node.right != None:
        curr = node.right
        # traverse to the leftmost node
        while curr.left != None:
            if curr.left != None:
                curr = curr.left
        if curr.value > value:
            return curr.value
    
    # visit parent if right node does not exist
    curr = node.parent

    # pay attention to the while statement below. it's important. 
    # it uses and AND to connect these two statements, if any of them is false,
    # break out of the while loop
    while (curr.value < value) and (curr.parent is not None):
        curr = curr.parent
        curr.value = curr.value
    # when we reach root node and root.value < value, return None
    if curr.parent == None and curr.value < value:
        return None
    # else return the successor
    return curr.value
    

class Node:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, value, parent=None):
        if self.value != None:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value, self)
                else:
                    self.left.insert(value, self.left)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value, self)
                else:
                    self.right.insert(value, self.right)
        else:
            self.value = value


if __name__ == "__main__":
    # testing
    root = Node()
    root.insert(20)

    assert get_in_order_successor(root, root.value) == None, "Failed test"
    root.insert(10)
    assert get_in_order_successor(root, root.value) == None, "Failed test"
    root.insert(7)
    root.insert(18)
    assert get_in_order_successor(root.left.right, root.left.right.value) == 20, "Failed test"
    root.insert(17)
    root.insert(50)
    root.insert(70)
    assert get_in_order_successor(root.right, root.right.value) == 70, "Failed test"
    assert get_in_order_successor(root.right.right, root.right.right.value) == None, "Failed test"

    root.insert(30)
    root.insert(25)
    root.insert(35)
    root.insert(33)
    root.insert(40)
    assert get_in_order_successor(root.right.left.right, root.right.left.right.value) == 40, "Failed test"
    print("perfecto, everything works fine")