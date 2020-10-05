"""
Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?


  0,  1  2  3  4  5  6
[-2, -2, 2, 2, 2, 6, 6]

Hints:#170, #204, #240, #286, #340
"""

# sorted array
# distinct int
# return a magic index if exists


# O(log(n)) time | O(1) space

#         0   1  2  3  4  5  6
array = [-2, -1, 0, 1, 2, 3, 6]


def getMagicIndex(array):
    return magicFast(array, 0, len(array) - 1)

def magicFast(array, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    if array[middle] == middle:
        return middle
    elif array[middle] < middle:
        return magicFast(array, middle + 1, right)
    else:
        return magicFast(array, left, middle + 1)


print(getMagicIndex(array))