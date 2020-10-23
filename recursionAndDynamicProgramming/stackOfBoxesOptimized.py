"""
Stack of Boxes: You have a stack of n boxes, with widths w i , heights h i , and depths d i . The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
Hints:#155, #194, #214, #260, #322, #368, #378

p142

recursion, each time we ask what is the next box we can put on the stack?
in the end, we compare what is the max we can get, return the maxHeight.

use Cache to prevent repeating calculations

Be very careful here with what each spot in the hash table represents. In this code, stackMap [ i] repre­
sents the tallest stack with box i at the bottom. Before pulling the value from the hash table, you have to
ensure that box i can be placed on top of the current bottom.

It helps to keep the line that recalls from the hash table symmetric with the one that inserts. For example, in
this code, we recall from the hash table with bottomindex at the start of the method. We insert into the
hash table with bottomindex at the end.
"""

def createMaxStack(boxes, cache):
    maxHeight = 0
    for i in range(len(boxes)):
        height = createStack(boxes, i, cache)
        maxHeight = max(maxHeight, height)
    return maxHeight

def createStack(boxes, idx, cache):
    if idx in cache:
        return cache[idx]
    bottom = boxes[idx]
    maxHeight = 0
    for i in range(idx + 1, len(boxes)):
        if canBeAbove(bottom, boxes[i]):
            height = createStack(boxes, i, cache)
            maxHeight = max(height, maxHeight)
    maxHeight += bottom[0]      # put it on the stack and return.
    cache[idx] = maxHeight
    # print(maxHeight)
    return maxHeight

def canBeAbove(bottom, top):
    return bottom[0]> top[0] and bottom[1] > top[1] and bottom[2] > top[2]

def getMaxStack(boxes):
    # sort it in descending order by height
    boxes.sort(reverse = True, key = lambda box: box[0])
    cache = {}
    print(boxes)
    result = createMaxStack(boxes, cache)
    print(cache)
    return result
    
boxes = [[100, 100, 100], [25, 25, 25], [20, 5, 30], [17, 4, 28]]
a = getMaxStack(boxes)
print(a)
