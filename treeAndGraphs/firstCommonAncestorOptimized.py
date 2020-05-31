"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Hints: #70, #76, #28, #36, #46, #70, #80, #96

We may recognize that we should only need to search the entire tree once to find p and q. We should then
be able to "bubble up" the findings to earlier nodes in the stack. The basic logic is the same as the earlier
solution.
We recurse through the entire tree with a function called commonAncestor(TreeNode root,
TreeNode p, Tree Node q). This function returns values as follows:
Returns p, if root's subtree includes p (and not q).
Returns q, if root's subtree includes q (and not p).
Returns null, if neither p nor q are in root's subtree.
Else, returns the common ancestor of p and q.
Finding the common ancestor of p and q in the final case is easy. When commonAncestor(n. left, p,
q) and commonAncestor(n. right, p, q) both return non-null values (indicating that p and q were
found in different subtrees), then n will be the common ancestor.


we also need to handle these two cases:
Case 1: p is a child of q (or, q is a child of p)
Case 2: p is in the tree and q is not (or, q is in the tree and pis not)

In either of these cases, c ommonAncestor will return p. In the first case, this is the correct return value, but
in the second case, the return value should be null.
We somehow need to distinguish between these two cases, and this is what the code below does. This
code solves the problem by returning two values: the node itself and a flag indicating whether this node is
actually the common ancestor.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Result:
    def __init__(self, n=None, isAnc=False):
        self.node = n
        self.isAnc = isAnc

def find_common_ancestor(root, n1, n2):
    result = common_anc_helper(root, n1, n2)
    if result.isAnc:
        return result.node
    else:
        return None

def common_anc_helper(root, n1, n2):
    # base case
    if root == None: return Result(None, False) 
    # print(root.value)

    if root == n1 and root == n2: return Result(root, True)

    leftResult = common_anc_helper(root.left, n1, n2)
    if leftResult.isAnc:    # found common ancestor
        # print("found ancestor at L: ", leftResult.node.value)
        return leftResult
    
    rightResult = common_anc_helper(root.right, n1, n2)
    if rightResult.isAnc:   # found common ancestor
        # print("found ancestor at R: ", rightResult.node.value)
        return rightResult
    
    # check if it's common ancestor
    if leftResult.node != None and rightResult.node != None:
        # print("found ancestor node here is root: ", root.value)
        return Result(root, True)   # found common ancestor
    elif root == n1 or root == n2:
        # print("root: ", root.value)
        """If we're currently at p or q, and we also found one of those nodes in a
        subtree, then this is truly an ancestor and the flag should be true. """
        is_ancestor = leftResult.node != None or rightResult.node != None
        # print("is ancestor: ", is_ancestor)
        return Result(root, is_ancestor)
    else:
        found_one_node = leftResult.node if leftResult.node != None else rightResult.node
        # print("found one node: ", found_one_node.value)
        # print("root: ", root.value)
        return Result(found_one_node, False)


import unittest
class TestFindAncestor(unittest.TestCase):

    def test_find_common_ancestor(self):
        self.assertEqual(1, 1)
        root = Node(10)
        root.left = Node(1)
        root.left.left = Node(7)
        root.left.left.left = Node(1000)
        root.left.left.left.right = Node(200)

        root.left.right = Node(22)
        root.right = Node(5)
        root.right.left = Node(120)
        root.right.left.left = Node(5)
        root.right.left.right = Node(3)

        root.right.right = Node(100)
        root.right.right.right = Node(4)

        # print(find_common_ancestor(root, root.left.left.left.right, root.left.right).value)
        self.assertEqual(find_common_ancestor(root, root.left.left.left.right, root.left.right).value, 1)
        self.assertEqual(find_common_ancestor(root, root.left.left.left.right, root.right).value, 10)
        self.assertEqual(find_common_ancestor(root, root.right.left.left, root.right.left.right).value, 120)

        self.assertEqual(find_common_ancestor(root, root.right, 99), None)


if __name__ == "__main__":
    unittest.main()

"""
how to return using if within one line
https://stackoverflow.com/questions/18669836/is-it-possible-to-write-single-line-return-statement-with-if-statement
"""