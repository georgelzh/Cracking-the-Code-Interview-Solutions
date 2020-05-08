class treeNode:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children

"""
# you can also have a tree class to wrap this Node class
# it's not needed, because it takes time
# You can if you feel it makes your code simpler or better, but it rarely does.

class Tree:
    def __init__(self, root = None):
        self.root = root
"""
