"""
4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Hints: #70, #76, #28, #36, #46, #70, #80, #96


if parent node is permited.


"""
import unittest

def find_common_ancestor(n1, n2):
    n1_depth = get_depth(n1)
    n2_depth = get_depth(n2)
    delta = n1_depth - n2_depth
    first = n1 if delta < 0 else n2
    second = n1 if delta > 0 else n2
    second = go_up_by(second, abs(delta))

    # if first and second equals, that means they are under the same parent
    # in this case, we just return the parent node.
    if first == second and first.parent != None:
        return first.parent

    # print("first value: " , first.value)
    # print("second value: " , second.value)

    # find where path intersect
    while (first != second and first != None and second != None):
        first = first.parent
        second = second.parent
    if first == None or second == None:
        output = None
    else:
        output =  first
    return output


def go_up_by(node, delta):
    while node != None and delta > 0:
        node = node.parent
        delta -=1 
    return node


def get_depth(node):
    depth = 0
    while node != None:
        node = node.parent
        depth += 1
    return depth

class Node:
    def __init__(self, value = None, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class TestFindAncestor(unittest.TestCase):

    def test_find_common_ancestor(self):
        root = Node(10)
        root.left = Node(1, root)
        root.left.left = Node(7, root.left)
        root.left.left.left = Node(1000, root.left.left)
        root.left.left.left.right = Node(200, root.left.left.left)

        root.left.right = Node(22, root.left)
        root.right = Node(5, root)
        root.right.left = Node(120, root.right)
        root.right.left.left = Node(5, root.right.left)
        root.right.left.right = Node(3, root.right.left)

        root.right.right = Node(100, root.right)
        root.right.right.right = Node(4, root.right.right)

#################################################################
        n1 = root.left.left.left.right
        n2 = root.left.right
        # print(n1.value)
        # print(n2.value)
        # print(find_common_ancestor(n1, n2).value)

        self.assertEqual(find_common_ancestor(n1, n2).value, 1)
        n2 = root.right
        self.assertEqual(find_common_ancestor(n1, n2).value, 10)

        n1 = root.right.left.right
        n2 = root.right.left.left

        self.assertEqual(find_common_ancestor(n2, n1).value, 120)


if __name__ == "__main__":
    unittest.main()

"""
python ternary operator
https://en.wikipedia.org/wiki/%3F:#Python
"""