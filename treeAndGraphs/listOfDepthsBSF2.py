# iterate all level, append all nodes at current level on a list, and append
# that list to the result Lists.

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

    def __str__(self):
        return str(self.value)


def createListOfDepths(root):
    lists = []
    if root == None:
        return lists
    # visit the root
    currentLevelNodesList = [root]
    while currentLevelNodesList:
        # take last level
        lists.append(currentLevelNodesList)

        # move to next level
        parents = currentLevelNodesList
        currentLevelNodesList = []

        # visit children and add them to the new currentLevelNodesList
        for parent in parents:
            if parent.left != None:
                currentLevelNodesList.append(parent.left)
            if parent.right != None:
                currentLevelNodesList.append(parent.right)
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
    arr = []
    num = -1
    for list in lists:
        num += 1
        arr.append([])
        for node in list:
            arr[num].append(str(node.value))

    print(arr)
