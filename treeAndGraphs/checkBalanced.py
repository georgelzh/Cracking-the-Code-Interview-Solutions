"""
4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

solution one:
This has O(N) time
and O(height) space
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

def checkBalanced(root):
    if root == None:
        return True
    else:
        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)
        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return checkBalanced(root.left) and checkBalanced(root.right)
            # return True is wrong, I should use recursive function here.
            # return max(leftHeight, rightHeight) + 1 this line is my mistake,
            # keeps in mind that I will need an extra function that help me get
            # the height of the root. the logic of returning it's balanced or not,
            # and returning the height of a node's all subnodes would not work well


def getHeight(root):
    if root is None:
        return -1
    else:
        # return the max height of the root
        output = max([getHeight(root.left), getHeight(root.right)]) + 1
        return output


if __name__ == "__main__":
    root = Node(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)

    checkBalanced(root)
