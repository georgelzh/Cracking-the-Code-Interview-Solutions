"""
4.12
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
Hints:#6, #14, #52, #68, #77, #87, #94, #103, #108, #115


DFS
1. visit start node check if curr_node.value + previous value == given value
        add 1 when value matches the given one.
2. then use pre-order traversal to traversal all possible path to the left and right.
    repeat 1 and 2 for each node that's been visited
3. add all path num from left, right and current_path_num and return it

4. find a way to repeat 1-3 steps for each node. find path num that starts from
        every single node and add sum the num together

        (During the process, we need to
            a. keep track of the current value
            b. need to pass the number of path back when it's finished
            (is it possible to save space?)
        )

What work is duplicated in the current brute-force algorithm?

Consider each path that starts from the root (there are N such paths) as an array. What
our brute-force algorithm is really doing is taking each array and finding all contiguous
subsequences that have a particular sum. We're doing this by computing all subarrays
and their sums. It might be useful to just focus on this little subproblem. Given an array,
how would you find all contiguous subsequences with a particular sum? Again, think
about the duplicated work in the brute-force algorithm.


Right now we have a brute force solution.

the same path are being traversed over and over again
the runtime is probably O(n^2) for now
"""
from collections import deque

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


# sum all path num for a node
def pathWithSum(node=None, curr_value=0, value=None):
    if node == None or value==None:
        return 0
    # initialization
    # path_num will be return back to the function call for final return
    path_num = 0
    # num_left is used to track all possible path when the node move to the left
    num_left = 0
    # num_left is used to track all possible path when the node move to the right
    num_right = 0
    
    # pre-order traversal - root - left - right
    # use traversal to traverse all the possible path,
    # and then check whether the path has identical value as the given value
    # path num += 1 if yes.
    curr_value = (node.value + curr_value)
    if curr_value == value:
        path_num += 1
    if root.left != None:
        num_left = pathWithSum(node.left, curr_value=curr_value, value=value)
    if root.right != None:
        num_right = pathWithSum(node.right, curr_value=curr_value, value=value)
    
    # add up the left path num and right path num back to the sum path num
    # then return it
    path_num += num_left
    path_num += num_right
    return path_num

# BFS
# visit start node, then, add children to a queue. and run the pathWithSum function
# for each one of the node, sum return value. return sum when everything is done
def AllPathWithSum(root, value):
    if root == None or value == None:
        return 0
    queue = deque()
    sum = 0
    
    curr = root
    while curr:
        if curr.left != None:
            queue.append(curr.left)
        if curr.right != None:
            queue.append(curr.right)
        path_num = pathWithSum(curr, value=value)
        sum += path_num
        if len(queue) > 0:
            curr = queue.popleft()
        else:
            return sum

if __name__ == "__main__":
    root = Node(10)
    root.insert(10)
    root.insert(-10)
    root.insert(-10)
    root.insert(0)
    root.insert(10)
    # num = pathWithSum(root, value=10)
    # print(num) #3

    sum = AllPathWithSum(root, value=10)
    print(sum)  #6
