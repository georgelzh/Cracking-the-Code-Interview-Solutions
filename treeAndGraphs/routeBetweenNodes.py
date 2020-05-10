# Find a route from the first node to the second node in a directed graph.
# reference: https://github.com/w-hat/ctci-solutions/blob/master/ch-04-trees-and-graphs/01-route-between-nodes.py
import unittest
from collections import deque


class Node:
    def __init__(self, value=None, adjacencyList=[]):
        self.value = value
        self.adjacencyList = adjacencyList
        self.shortestPath = None

    def addEdgeTo(self, node):
        self.adjacencyList += [node]

    def __str__(self):
        return self.value


def findPath(startNode, endNode):
    foundPath = None
    queue = deque()
    node = startNode
    node.shortestPath = [node]
    allVisitedNodes = [node]
    while node:
        # print("node: ", node.value)
        for adjacent in node.adjacencyList:
            if adjacent not in allVisitedNodes:
                adjacent.shortestPath = node.shortestPath + [adjacent]
                # print([item.value for item in node.shortestPath])
                if adjacent == endNode:
                    # print(adjacent.value)
                    # print([item.value for item in node.shortestPath])
                    foundPath = node.shortestPath + [adjacent]
                    # print("path length: ", len(foundPath))
                    # print([item.value for item in foundPath])
                    break
                queue.append(adjacent)
                # print("after append: ", [item.value for item in queue])
                allVisitedNodes.append(adjacent)
        try:
            node = queue.popleft()
            # print("after pop:", [item.value for item in queue])
        except:
            node = None
    for node in allVisitedNodes:
        node.shortestPath = None
    return foundPath

def stringfyPath(path):
    if path is None:
        return "None"
    arr = []
    for node in path:
        arr.append(node.value)
    return ''.join(arr)

class Test(unittest.TestCase):
    def testFindRoute(self):
        node_j = Node('J')
        node_i = Node('I')
        node_h = Node('H')
        node_d = Node('D')
        node_f = Node('F', [node_i])
        node_b = Node('B', [node_j])
        node_g = Node('G', [node_d, node_h])
        node_c = Node('C', [node_g])
        node_a = Node('A', [node_b, node_c, node_d])
        node_e = Node('E', [node_f, node_a])
        node_d.addEdgeTo(node_a)
        self.assertEqual(stringfyPath(findPath(node_a, node_i)), 'None')
        self.assertEqual(stringfyPath(findPath(node_a, node_j)), 'ABJ')
        node_h.addEdgeTo(node_i)
        print([node_i in node_h.adjacencyList])
        self.assertEqual(stringfyPath(findPath(node_a, node_i)), 'ACGHI')

if __name__ == "__main__":
    unittest.main()
