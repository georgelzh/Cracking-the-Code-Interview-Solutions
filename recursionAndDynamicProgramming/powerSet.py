"""
Power Set: Write a method to return all subsets of a set.
Hints: #273, #290, #338, #354, #373

How can you build all subsets of {a, b, c} from the subsets of {a, b}?

Anything that is a subset of {a, b} is also a subset of {a, b, c}. Which sets are
subsets of{a, b, c}but not{a, b}?

Subsets that contain c will be subsets {a, b, c} but not {a, b}. Can you build these
subsets from the subsets of {a, b}?

You can also do this by mapping each subset to a binary number. The ith bit could
represent a "boolean"flag for whether an element is in the set.
"""
"""
recursion way to solve it. we solved this backwards. which is also fine.

def getSubsets(arr, idx):
    allSubsets = []
    if len(arr) == idx:
        allSubsets.append([])
    else:
        allSubsets = getSubsets(arr, idx + 1)
        item = arr[idx]
        moreSubsets = []
        for subset in allSubsets:
            newSubset = [value for value in subset]
            newSubset.append(item)
            moreSubsets.append(newSubset)
        allSubsets.extend(moreSubsets)
    return allSubsets

a = getSubsets([1,2,3], 0)
print(a)
"""


def getSubsets(arr):
    allSubsets = []
    # this generates a number as 2^len(arr), because of the leftshift, operator.
    maxNum = 1 << len(arr)
    for k in range(maxNum):
        subset = convertIntToSet(k, arr)
        allSubsets.append(subset)
    return allSubsets

def convertIntToSet(k, arr):
    subset = []
    index = 0
    while k > 0:
        print(subset)
        # if the element the index is pointed to, is selected, and it's not in setset already.
        if k & 1 == 1 and arr[index] not in subset:
            subset.append(arr[index])
        index += 1
        k >>= 1
    return subset

a = getSubsets([1,2,3])
print(a)
