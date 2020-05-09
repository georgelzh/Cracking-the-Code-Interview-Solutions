# binary search tree implementation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data != None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findVal(self, data):
        if data < self.data:
            if self.left is None:
                return str(data) + " not found"
            else:
                return self.left.findVal(data)
        if data > self.data:
            if self.right is None:
                return str(data) + " not found"
            else:
                return self.right.findVal(data)
        else:
            return str(data) + " is found"

# in-order traversal: left, current, right
    def printTree(self):
        # there are many ways to print the data, here we use In Order
        if self.data != None:
            if self.left != None:
                self.left.printTree()
            print( self.data)
            if self.right != None:
                self.right.printTree()


    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def inorderTraversal(self,root):
        output = []
        if root:
            output = self.inorderTraversal(root.left)
            output.append(root.data)
            output = output + self.inorderTraversal(root.right)
        return output


if __name__ == "__main__":
    root = Node(-1)
    root.insert(2)
    root.insert(0)
    root.insert(12)
    root.insert(5)
    root.insert(2)
    root.printTree()
    print(root.findVal(-1))




"""
# https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm

    # pre-order: visit current, left, then right
    def printTree(self):
        if self.data != None:
            print(self.data)
            if self.left != None:
                self.left.printTree()
            if self.right != None:
                self.right.printTree()


    # post-order: left -> right -> root
    def printTree(self):
        if self.data != None:
            if self.left != None:
                self.left.printTree()
            if self.right != None:
                self.right.printTree()
            print(self.data)

"""
