"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations

Hints: #166, #203, #227, #234, #246, #280

"""
"""
# solution 1
def minProduct(a, b):
    print(a, b)
    bigger = a if a >= b else b
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)

def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    
    # compute half. if uneven, compute other half. if even double it
    s = smaller >> 1 # divide by 2
    side1 = minProduct(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = minProductHelper(smaller - s, bigger)
    return side1 + side2

# solution 2
# deduce repeated work with cache, we know bigger number is always the same
# in our algorithms so we just need to keep track of the smaller in cache
def minProduct(a, b):
    print(a, b)
    bigger = a if a >= b else b
    smaller = a if a < b else b
    cache = {}
    return minProductHelper(smaller, bigger, cache)

def minProductHelper(smaller, bigger, cache):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    if smaller in cache and cache[smaller] > 0:
        return cache[smaller]

    # compute half. if uneven, compute other half. if even double it
    s = smaller >> 1 # divide by 2
    side1 = minProduct(s, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = minProductHelper(smaller - s, bigger, cache)
    cache[smaller] = side1 + side2
    return cache[smaller]
"""

def minProduct(a, b):
    print(a, b)
    bigger = a if a >= b else b
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)

def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    # compute half. if uneven, compute other half. if even double it
    s = smaller >> 1 # divide by 2
    halfprod = minProduct(s, bigger)

    if smaller % 2 == 0:
        return halfprod + halfprod
    else:
        return halfprod + halfprod + bigger
    
a = minProduct(2, 5)
print(a)