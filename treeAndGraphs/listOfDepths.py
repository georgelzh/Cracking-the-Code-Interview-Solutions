"""
4.3 List of Depths: Given a binary tree, design an algorithm which creates
a linked list of all the nodes at each depth (e.g., if you have a tree
with depth D, you'll have D linked lists). Hints: #107, #123, #135

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
