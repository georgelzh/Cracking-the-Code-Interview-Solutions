"""
4.3 List of Depths: Given a binary tree, design an algorithm which creates
a linked list of all the nodes at each depth (e.g., if you have a tree
with depth D, you'll have D linked lists). Hints: #107, #123, #135

the concept is to use an arr that's outside of the recursive function to store
the change of list. Since we do not know the depth of the array, we will just
start with empty list. whenerver we reach a new level, we create a new list in
the original list. so we have [[]* number of depths]

1. we use pre Order Traversal to approach this problem because this way,
we keep track of the depth we are at.

2. we need a function that pass down the list, and number of depths to append
values at the right list. eg: if we have a value 5 at depth 8 (start counting
from 0). then we will have list[5].append(5) so that we have this value.

process :
start from root, we append the root value list[0].append(root.value),
then we check the if the root have left if it does, we pass depth number as 0+1,
and pass down the list that has root value in it. this time list[0+1].append(node.value)
will happen. then we move to right node and do the same thing. recursively,
all the node will be added at the right level into the list.

in the end we return the arr.
"""
class Node:
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value != None:
            if self.value > value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif self.value < value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # pre-order: visit current, left, then right
    def printTree(self):
        if self.value != None:
            print(self.value)
            if self.left != None:
                self.left.printTree()
            if self.right != None:
                self.right.printTree()

# You have to know how many depths are there
def createListOfDepths(root):
    return listOfDepths([], root, 0)

def listOfDepths(arr, root, depthNum):
    if root == None:
        return
    if len(arr) < depthNum+1:
        arr.append([])
    # pre order traversal
    if root != None:
        arr[depthNum].append(root.value)
    nextDepthNum = depthNum +1
    if root.left != None:
        listOfDepths(arr, root.left, nextDepthNum)
    if root.right != None:
        listOfDepths(arr, root.right, nextDepthNum)
    return arr



if __name__ == "__main__":
    root = Node(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)

    arr = createListOfDepths(root)
    print(arr)
