# Minimal Tree: Given a sorted (increasing order) array with
# unique integer elements, write an algorithm to create a
# binary search tree with minimal height.
# reference https://github.com/w-hat/ctci-solutions/blob/master/ch-04-trees-and-graphs/02-minimal-tree.py

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
            return False

    def inOrderTraversal(self):
        arr = []
        if self.value is None:
            return None
        else:
            if self.left != None:
                arr = self.left.inOrderTraversal()
            arr.append(self.value)
            if self.right != None:
                arr += self.right.inOrderTraversal()
            return arr

    def __str__(self):
        arr = self.inOrderTraversal()
        arr = list(map(str, arr))
        return ' '.join(arr)

def createMinimalBST(arr):
    # base case
    if len(arr) == 0:
        return None
    middle = int(len(arr)/2)
    middleNode = Node(arr[middle])
    left = createMinimalBST(arr[:middle])
    right = createMinimalBST(arr[(middle+1):])
    middleNode.left = left
    middleNode.right = right
    return middleNode

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    n = createMinimalBST(arr)
    print(n)
