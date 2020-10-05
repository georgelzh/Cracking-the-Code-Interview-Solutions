"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs
Hints: #152, #178, #217, #237, #262, #359

100 steps

#(100)
99 - 1 , 98 - 2 , 97 - 3

                #(99) +                     #(98) + #(97)
      98,        97,      96
   |97 96 95 |96 95 94| 95 94 93|      . .. . . . . . 

we are walking backwords here, from n, we walk all different ways to 0.

"""

def numberOfWaysRunStairs(n):
    cache = {0: 1, 1: 1, 2: 2, 3: 3}
    if n < 0:
        return 0
    return helper(n, cache)

def helper(n, cache):
    if n < 0:
        return 0
    if n in cache:
        return cache[n]
    cache[n] = helper(n - 1, cache) + helper(n - 2, cache) + helper(n - 3, cache)
    return cache[n]

print(numberOfWaysRunStairs(5))


