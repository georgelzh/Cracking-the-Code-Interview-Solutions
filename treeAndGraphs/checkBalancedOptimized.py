"""
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

O(N) time
O(H) space

We need to cut out some of the calls to getHeight.
If we inspect this method, we may notice that getHeight could actually check if the tree is balanced at
the same time as it's checking heights. What do we do when we discover that the subtree isn' t balanced?
Just return an error code.

This improved algorithm works by checking the height of each subtree as we recurse down from the root.
On each node, we recursively get the heights of the left and right subtrees through the checkHeight
method. If the subtree is balanced, then checkHeight will return the actual height of the subtree. If the
subtree is not balanced, then c h ec kHeight will return an error code. We will immediately break and
return an error code from the current call.
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


def checkHeight(root):
    if root == None:
        return -1

    leftHeight = checkHeight(root.left)
    if leftHeight == -99:
        return -99      # pass error code
    rightHeight = checkHeight(root.right)
    if rightHeight == -99:
        return -99

    if abs(leftHeight - rightHeight) > 1:
        return -99      # pass error code
    else:
        # when the root get left and right nodes height, and they are balanced,
        # return the maximum height
        return max(leftHeight, rightHeight) + 1

# here we check the return value
# it's very important here to have two functions,
# otherise, it seems hard to manage the return and final check.
# it's possible to return many variables at the same time, like a tuple(a, b)

def checkBalanced(root):
    return checkHeight(root) != -99

if __name__ == "__main__":
    root = Node(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)
    root.insert(19)
    root.insert(20)

    assert checkBalanced(Node()) == True, "faled"
    assert checkBalanced(root) == False, "faled"
