"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
Hints: #300, #324, #343, #380, #394

first time I have 4 options to pick. 
for each of those options, if I am not running out of the rest "n".
they will still have 4 options to pick.

the number of ways to represent it will increase by 1 if the rest "n" is 0
"""


def numOfWaysCoins(coins, n):
    if n == 1:
        return 1
    cache = {}
    ways = helper(coins, n, cache, [])
    return ways

def helper(coins, n, cache, arr):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        # print(arr)    # uncomment this line and comment out one below to see combo
        return 1

    # comment this below to see all combo
    if n in cache:
        return cache[n]
    # comment this above

    sums = 0
    for coin in coins:
        sums += helper(coins, n - coin, cache, arr[:] + [coin])
    cache[n] = sums
    return cache[n]


coins = [1, 5, 10, 25]
ways = numOfWaysCoins(coins, 10)
print(ways)

"""
1111111111
511111
151111
115111
111511
111151
111115
5, 5
10
"""