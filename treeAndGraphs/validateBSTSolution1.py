"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.

Notice: if no duplicated node is allowed. we could use in order traversal to add all
nodes to an array. If they are sorted, that means it's a BST. However, since we do 
inorder traversal, we could just compare the node to previous node visited, 
if previous node value is bigger than than curr node value. than return False. Else True. 
so we don't need arr anymore. 

"""


class LastVisitedNodeValue:
    def __init__(self, data = None):
        self.data = data
    
    def resetValue(self):
        self.data = None

def checkBST(root, lastVisitedNodeValue):
    # base case
    if root is None:
        return True

    # visit left
    if (not checkBST(root.left, lastVisitedNodeValue)):
        return False
    
    # visit current, write the logical statement for checking
    if lastVisitedNodeValue.data != None and lastVisitedNodeValue.data >= root.value:
        return False
    
    lastVisitedNodeValue.data = root.value

    # visit right
    if(not checkBST(root.right, lastVisitedNodeValue)):
        return False
    
    # passed all test
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
    lastVisitedNodeValue = LastVisitedNodeValue()
    root = Node(-1)
    root.right = Node(-2)

    assert checkBST(root, lastVisitedNodeValue) == False, "Fail to test"
    root.right = None


    lastVisitedNodeValue.resetValue()
    assert checkBST(root, lastVisitedNodeValue) == True, "Fail to test"
    root.insert(8)
    
    lastVisitedNodeValue.resetValue()
    assert root.right.value == 8, "Fail to test"

    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)
    
    root.insert(-9)
    root.insert(-10)
    # print((root.left).value)
    # print((root.left.left).value)
    root.left.right = Node(99)
    # print((root.left.right).value)
    lastVisitedNodeValue.resetValue()
    assert checkBST(root, lastVisitedNodeValue) == False, "Fail to test"