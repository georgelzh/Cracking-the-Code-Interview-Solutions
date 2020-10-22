"""
Stack of Boxes: You have a stack of n boxes, with widths w i , heights h i , and depths d i . The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
Hints:#155, #194, #214, #260, #322, #368, #378

p142

recursion, each time we ask what is the next box we can put on the stack?
in the end, we compare what is the max we can get, return the maxHeight.

kinda hard to think about in the first place.
"""

def createMaxStack(boxes):
    maxHeight = 0
    for i in range(len(boxes)):
        height = createStack(boxes, i)
        maxHeight = max(maxHeight, height)
    return maxHeight

def createStack(boxes, idx):
    bottom = boxes[idx]
    maxHeight = 0
    for i in range(idx + 1, len(boxes)):
        if canBeAbove(bottom, boxes[i]):
            height = createStack(boxes, i)
            maxHeight = max(height, maxHeight)
    maxHeight += bottom[0]      # put it on the stack and return.
    # print(maxHeight)
    return maxHeight

def canBeAbove(bottom, top):
    return bottom[0]> top[0] and bottom[1] > top[1] and bottom[2] > top[2]

def getMaxStack(boxes):
    # sort it in descending order by height
    boxes.sort(reverse = True, key = lambda box: box[0])
    print(boxes)
    return createMaxStack(boxes)
    
boxes = [[100, 100, 100], [25, 25, 25], [20, 5, 30], [17, 4, 28]]
a = createMaxStack(boxes)
print(a)

