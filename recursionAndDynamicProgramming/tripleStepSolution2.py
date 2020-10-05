

"""
from bottom up approach
"""

def numberOfWaysRunStairs(n):
    if n <= 0:
        return 0
    ways = helper(0, n)
    print(ways)

def helper(walkedSteps, remSteps):
    # base case
    if remSteps < 0:
        return 0
    # only when we walked all the steps, we return 1 // add 1 to the number of ways
    # else we don't do anything. eventually, this recursion method walks all the ways
    # once and add 1 to the result. when its done walking every way, it returns the sum. 
    if remSteps == 0: 
        return 1
    return helper(walkedSteps + 1, remSteps - 1) + helper(walkedSteps + 2, remSteps - 2) + helper(walkedSteps + 3, remSteps - 3)

"""
find ways 
"""

numberOfWaysRunStairs(5)