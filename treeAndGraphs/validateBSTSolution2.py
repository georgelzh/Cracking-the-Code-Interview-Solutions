"""
use pre-order traversal. everytime we traverse, we pass down range for min and max

make sure the left value and right values of subtrees of root are withing the range.
if within the range, visit next node and and update the (min, max) range.

"""

def isBST(root):
    return checkBST(root, None, None)

def checkBST(root, min, max):
    # base case
    if root is None:
        return True
    
    # visit current
    if (min != None and root.value <= min) or (max != None and root.value > max):
        return False
    
    # visit left, (min = None, max = root.value)
    if (not checkBST(root.left, min, root.value)):
        return False
    

    # visit right (min = root.value, max)  
    # Attention: its important here to pass min and max because it changes
    # as we traverse. I made mistake here. Now it's corrected.

    if (not checkBST(root.right, root.value, max)):
        return False
    
    return True



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


if __name__ == "__main__":
    root = Node(-1)
    root.right = Node(-2)

    assert isBST(root) == False, "Fail to test"
    root.right = None
    assert isBST(root) == True, "Fail to test"
    root.insert(8)
    assert root.right.value == 8, "Fail to test"

    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)
    assert isBST(root) == True, "Fail to test"

    root.insert(-9)
    root.insert(-10)
    # print((root.left).value)
    # print((root.left.left).value)
    root.left.right = Node(99)
    print((root.left.right).value)
    assert isBST(root) == False, "Fail to test"