# Return an array of linked lists containing all elements on each depth
# of a binary tree.
# BFS needs to go to each node, we use a queue to store all the Node object rather
# than a value

from collections import deque

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.depth = None

    def insert(self, value):
        if value != None:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

def createListOfDepths(root):
    if root is None:
        return []
    lists = []
    root.depth = 0
    curr = root
    currDepth = -1
    queue = deque()

    while curr != None:
        if currDepth != curr.depth:
            currDepth += 1
            lists.append([curr.value])
        else:
            lists[currDepth].append(curr.value)

        # add the children to the queue and write their depth
        for child in [curr.left, curr.right]:
            if child != None:
                child.depth = currDepth+1
                queue.append(child)
        try:
            curr = queue.popleft()
        except:
            curr = None
    return lists

if __name__ =="__main__":
    root = Node(10)
    root.insert(8)
    root.insert(15)
    root.insert(6)
    root.insert(9)
    root.insert(13)
    root.insert(16)

    lists = createListOfDepths(root)
    print(lists)
