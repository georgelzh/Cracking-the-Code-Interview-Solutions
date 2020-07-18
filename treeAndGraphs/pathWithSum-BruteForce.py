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

def countPathWithSum(root, targetSum):
    if root == None:
        return 0
    
    # count path with sum starting from the root
    pathsFromRoot = countPathWithSumFromNode(root, targetSum, 0)

    # try the nodes on the left and right
    pathOnLeft = countPathWithSum(root.left, targetSum)
    pathOnRight = countPathWithSum(root.right, targetSum)
    
    return pathsFromRoot + pathOnLeft + pathOnRight

# Returns the number of paths with this sum starting from this node.

def countPathWithSumFromNode(node, targetSum, currentSum):
