"""
Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?

brute force

else: return


  0,  1  2  3  4  5  6
[-2, -2, 2, 2, 2, 6, 6]

Hints:#170, #204, #240, #286, #340
"""

# sorted array
# distinct int
# return a magic index if exists


# O(n) time | O(1) space

#         0   1  2  3  4  5  6
array = [-2, -1, 0, 1, 2, 3, 6]


def getMagicIndex(array):
    if len(array) == 0:
        return None
    for index, num in enumerate(array):
        if index == num:
            return index
    return None

print(getMagicIndex(array))