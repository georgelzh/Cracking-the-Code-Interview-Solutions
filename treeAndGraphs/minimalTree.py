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


"""
To create a tree of minimal height, we need to match the number of nodes in the left subtree to the number
of nodes in the right subtree as much as possible. This means that we want the root to be the middle of the
array, since this would mean that half the elements would be less than the root and half would be greater
than it.
We proceed with constructing our tree in a similar fashion. The middle of each subsection of the array
becomes the root of the node. The left half of the array will become our left subtree, and the right half of
the array will become the right subtree.
One way to implement this is to use a simple root. insertNode(int v) method which inserts the
value v through a recursive process that starts with the root node. This will indeed construct a tree with
minimal height but it will not do so very efficiently. Each insertion will require traversing the tree, giving a
total cost ofO ( N log N) to the tree.
Alternatively, we can cut out the extra traversals by recursively using the createMinimalBST method.
This method is passed just a subsection of the array and returns the root of a minimal tree for that array.
The algorithm is as follows:
1. Insert into the tree the middle element of the array.
2. Insert (into the left subtree) the left subarray elements.
3. Insert (into the right subtree) the right subarray elements.
4. Recurse.
"""
