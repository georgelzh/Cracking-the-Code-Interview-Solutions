"""
Stack of Boxes: You have a stack of n boxes, with widths w i , heights h i , and depths d i . The boxes
cannot be rotated and can only be stacked on top of one another if each box in the stack is strictly
larger than the box above it in width, height, and depth. Implement a method to compute the
height of the tallest possible stack. The height of a stack is the sum of the heights of each box.
Hints:#155, #194, #214, #260, #322, #368, #378

p142

"""

def createMaxStack(boxes, cache):
    return createStack(boxes, None, 0, cache)

def createStack(boxes, bottom, offset, cache):
    # base case
    if offset >= len(boxes):
        return 0

    newBottom = boxes[offset]
    heightWithBottom = 0
    if bottom == None or canBeAbove(bottom, newBottom):
        if offset not in cache:
            cache[offset] = createStack(boxes, newBottom, offset + 1, cache)
            cache[offset] += newBottom[0]
        heightWithBottom = cache[offset]

    heightWithoutBottom = createStack(boxes, bottom, offset + 1, cache)
    result = max(heightWithBottom, heightWithoutBottom)
    print(result)
    return result


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
