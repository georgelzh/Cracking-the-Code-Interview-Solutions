#!python3
"""
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
EXAMPLE
Input:
N 10000000000, M 10011,
Output: 
N = 10001001100
 i = 2, j = 6
Hints: #137, #169, #215


It seems like a shifting, addition and clearbits problem.
we gonna leftshift M ith.
then return M+N
"""

def insert(n, m, i, j):
    # clear the bits j through i in N
    
    # clear right bits that has index less than j
    n_right = n & (-1 << (j+1))

    # clear left bits that has index higher than i
    n_left = ((1 << i) - 1) & n

    # merge N and M
    return n_left + n_right + (m << i)

if __name__ == "__main__":
    print(insert(0b10000000000, 0b1011, 2, 6)) #0b10000101100