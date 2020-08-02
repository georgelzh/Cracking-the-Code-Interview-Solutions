"""
1. Track its runningSum. We'll take this in as a parameter and immediately increment it by node. value.
2. Look up runningSum - targetSum in the hash table. The value there indicates the total number. Set
totalPaths to this value.
3. If runningSum == targetSum, then there's one additional path that starts at the root. Increment
totalPaths.
4. Add runningSum to the hash table (incrementing the value if it's already there).
5. Recurse left and right, counting the number of paths with sum targetSum.
6.
After we're done recursing left and right, decrement the value of runningSum in the hash table. This is
essentially backing out of our work; it reverses the changes to the hash table so that other nodes don't
use it (since we're now done with node).
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
    return countPathWithSumFromNode(root, targetSum, 0, {})

def countPathWithSumFromNode(node, targetSum, runningSum, pathCount):
    if node == None:    # base case
        return 0
    
    # Count paths with sum ending at the current node.
    runningSum += node.value
    sum = runningSum - targetSum
    totalPaths = pathCount.get(sum, 0)

    # /* If runningSum equals targetSum, then one additional path starts at root.
    # * Add in this path.*/
    if runningSum == targetSum:
        totalPaths += 1

    # /* Increment pathCount, recurse, then decrement pathCount. */
    # increment pathCount, store the new sum for current node position
    incrementHashTable(pathCount, runningSum, 1) 
    totalPaths += countPathWithSumFromNode(node.left, targetSum, runningSum, pathCount)
    totalPaths += countPathWithSumFromNode(node.right, targetSum, runningSum, pathCount)
    incrementHashTable(pathCount, runningSum, -1) 
    # decrement pathCount, take the sum of the current node position away from the hashtable
    
    return totalPaths

def incrementHashTable(hashTable, key, delta):
    newCount = hashTable.get(key, 0) + delta
    if newCount == 0:
        if key in hashTable:
            del hashTable[key]
    else:
        hashTable[key] = newCount

if __name__ == "__main__":
    root = Node(10)
    root.insert(10)
    root.insert(-10)
    root.insert(-10)
    root.insert(0)
    root.insert(10)

    sum = countPathWithSum(root, 10)
    print(sum)  #6
