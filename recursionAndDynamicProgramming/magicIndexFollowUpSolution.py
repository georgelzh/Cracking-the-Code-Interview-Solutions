"""
Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""

# sorted array
# distinct int
# return a magic index if exists


# O(log(n)) time | O(1) space

#         0,  1  2  3  4  5  6
array = [-2, -2, 2, 2, 2, 6, 0]

#array = [-2, -2, 2, 2, 2, 6, 6]

def getMagicIndex(array):
    return magicFast(array, 0, len(array) - 1)

def magicFast(array, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    middleVal = array[middle]
    
    if middle == middleVal:
        return middle
    
    # search left
    leftIndex = min(middle, middleVal)
    left = magicFast(array, left, leftIndex)
    if left >= 0:
        return left

    # search right
    rightIndex = max(middle + 1, middleVal)
    right = magicFast(array, rightIndex, right)
    if right >= 0:
        return right
    return right

print(getMagicIndex(array))