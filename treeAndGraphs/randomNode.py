#!Python3
"""
4.11
Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
Hints: #42, #54, #62, #75, #89, #99, #112, #119

possible solution 1:
random traversal
Run time for traversal:
Average run time O((n+1)/2) because 1+2+3+4+...+n = n(n+1)/2
worst scenario O(n)

possible solution 2:
store all the nodes in a list, and get an random int(0, number_of_nodes)
return node_list[random_int]
Run time: O(1)

Option #1 [Slow & Working]
One solution is to copy all the nodes to an array and return a random element in the array. This solution will
take O(N) time and O(N) space, where N is the number of nodes in the tree.
We can guess our interviewer is probably looking for something more optimal, since this is a little too
straightforward (and should make us wonder why the interviewer gave us a binary tree, since we don't
need that information).
We should keep in mind as we develop this solution that we probably need to know something about the
internals of the tree. Otherwise, the question probably wouldn't specify that we're developing the tree class
from scratch.

Option #2 [Slow & Working)
Returning to our original solution of copying the nodes to an array, we can explore a solution where we
maintain an array at all times that lists all the nodes in the tree. The problem is that we'll need to remove
nodes from this array as we delete them from the tree, and that will take O ( N) time.

Option #3 [Slow & Working]
We could label all the nodes with an index from 1 to N and label them in binary search tree order (that
is, according to its inorder traversal). Then, when we call getRandomNode, we generate a random index
between 1 and N. If we apply the label correctly, we can use a binary search tree search to find this index.
However, this leads to a similar issue as earlier solutions. When we insert a node or a delete a node, all of the
indices might need to be updated. This can take O(N) time.

Option #4 [Fast & Not Working]
What if we knew the depth of the tree? (Since we're building our own class, we can ensure that we know
this. It's an easy enough piece of data to track.)
We could pick a random depth, and then traverse left/right randomly until we go to that depth. This
wouldn't actually ensure that all nodes are equally likely to be chosen though.
First, the tree doesn't necessarily have an equal number of nodes at each level. This means that nodes on
levels with fewer nodes might be more likely to be chosen than nodes on a level with more nodes.
Second, the random path we take might end up terminating before we get to the desired level. Then what?
We could just return the last node we find, but that would mean unequal probabilities at each node.

Option #5 [Fast & Not Working]
We could try just a simple approach: traverse randomly down the tree. At each node:
with 1/3 odds, we return the current node.
with 1/3 odds, we traverse left.
with 1/3 odds, we traverse right.

This solution, like some of the others, does not distribute the probabilities evenly across the nodes. The root
has a 1/3 probability of being selected-the same as all the nodes in the left put together


Option #6 [Fast & Working]
Rather than just continuing to brainstorm new solutions, let's see if we can fix some of the issues in the
previous solutions. To do so, we must diagnose-deeply-the root problem in a solution.
Let's look at Option #5. It fails because the probabilities aren't evenly distributed across the options. Can we
fix that while keeping the basic algorithm the same?
We can start with the root. With what probability should we return the root? Since we have N nodes, we
must return the root node with 1/n probability. (In fact, we must return each node with 1/n probability.
After all, we have N nodes, and each must have equal probability. the total must be 1(100%), therefore, 
each must have 1/n probability.

We've resolved the issue with the root. Now what about the rest of the problem? With what probability
should we traverse left versus right? It's not 50/50. Even in a balanced tree, the number of nodes on each
side might not be equal. If we have more nodes on the left than the right, then we need to go left more
often.
One way to think about it is that the odds of picking something-anything-from the left must be the sum
of each individual probability. Since each node must have probability 1/n, the odds of picking something
from the left must have probability LEFT _SIZE * 1/n. This should therefore be the odds of going left.
Likewise, the odds of going right should be RIGHT _SIZE * 1/n

This means that each node must know the size of the nodes on the left and the size of the nodes on the
right. Fortunately, our interviewer has told us that we're building this tree class from scratch. It's easy to
keep track of this size information on inserts and deletes. We can just store a size variable in each node.
Increment size on inserts and decrement it on deletes.

# In a balanced tree, this algorithm will be O(log N), where N is the number of nodes.
"""

# bST Node class
from random import randint

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.size = 0
        if self.val != None:
            self.size += 1

    def insert(self, val):
        if self.val != None:
            if val > self.val:
                if self.right == None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
            elif val <= self.val:
                if self.left == None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            self.size += 1
        else:
            self.val = val
            self.size += 1

    def get_random_node(self):
        left_size = self.left.size if self.left != None else 0
        index = randint(0, self.size-1)
        if index < left_size:
            return self.left.get_random_node()
        elif index == left_size:
            return self.val
        else:
            return self.right.get_random_node()
        
    
    def find(self, val):
        if val == self.val:
            return self
        elif val < self.val:
            if self.left == None:
                return None
            else:
                return self.left.find(val)
        elif val > self.val:
            if self.right == None:
                return None
            else:
                return self.right.find(val)
        else:
            return None

if __name__ == "__main__":
    root = Node(-1)
    root.insert(2)
    root.insert(0)
    root.insert(12)
    root.insert(5)
    root.insert(2)
    print(root.get_random_node())