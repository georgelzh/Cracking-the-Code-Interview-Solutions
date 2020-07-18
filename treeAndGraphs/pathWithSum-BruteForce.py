"""
4.12
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

In the brute force approach, we just look at all possible paths. To do this, we traverse to each node. At each
node, we recursively try all paths downwards, tracking the sum as we go. As soon as we hit our target sum,
we increment the total.

a node at depth d will be touched by d nodes above it.
in a balanced binary tree, d will be no more than logN. With N nodes in the tree, 
countPathsWi thSumFromNode will be called O(N log N) times
The runtime is O(N log N)

"""

# random binary tree class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.value != None:
            if self.left == None:
                self.left = Node(value)
            elif self.right == None:
                self.right = Node(value)
            elif self.left != None and self.right != None:
                if self.left.left != None and self.left.right != None:
                    self.right.insert(value)
                else:
                    self.left.insert(value)


def countPathWithSum(root, targetSum):
    if root == None:
        return 0
    
    # count path with sum starting from the root
    pathsFromRoot = countPathWithSumFromNode(root, targetSum, 0)

    # try the nodes on the left and right
    pathOnLeft = countPathWithSum(root.left, targetSum)
    pathOnRight = countPathWithSum(root.right, targetSum)
    
    return pathsFromRoot + pathOnLeft + pathOnRight


def countPathWithSumFromNode(node, targetSum, currentSum):
# Returns the number of paths with this sum starting from this node.
    if node == None:
        return 0
    currentSum += node.value

    # check if current value matches target sum
    totalPaths = 0
    if currentSum == targetSum:
        totalPaths += 1
    
    # traverse to the children and count all the total path
    totalPaths += countPathWithSumFromNode(node.left, targetSum, currentSum)
    totalPaths += countPathWithSumFromNode(node.right, targetSum, currentSum)
    return totalPaths

if __name__ == "__main__":
    root = Node(10)
    root.insert(10)
    root.insert(-10)
    root.insert(-10)
    root.insert(0)
    root.insert(10)

    sum = countPathWithSum(root, 10)
    print(sum)  #6


"""
bruce force solution from cracking the code interview
"""