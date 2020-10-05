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
array = [-2, -2, 2, 2, 2, 6, 6]


def getMagicIndex(array):
    return magicFast(array, 0, len(array) - 1)

def magicFast(array, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    num = array[middle]
    newLeft = left
    newRight = right
    while newLeft > 0 and newRight < len(array) - 1:
        if array[newLeft - 1] == num:
            if array[newLeft - 1] == newLeft - 1:
                return newLeft - 1
            newLeft -= 1
        if array[newRight + 1] == num:
            if array[newRight + 1] == newRight + 1:
                return newRight + 1
            newRight += 1
        if array[newLeft] != num and array[newRight] != num:
            break

    if num == middle:
        return middle
    elif num < newRight:
        return magicFast(array, newRight, right)
    else:
        return magicFast(array, left, newLeft)


print(getMagicIndex(array))