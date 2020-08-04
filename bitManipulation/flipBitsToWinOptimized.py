#!python3
"""
5.3 
Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1. Write code to
find the length of the longest sequence of 1 s you could create.

EXAMPLE
input: 1775 (or: 11011101111)
output: 8

Hints: #159, #226, #31 4, #352

optimized space

run time: O(b)
memory O(1)

00100
1101101
"""

def flip_bit(num):
    if num == -1:
        return len(bin(num)[2:])

    max_length = 1
    prev_length = 0
    curr_length = 0

    while num != 0:
        if (num & 1) == 1:
            curr_length += 1
        elif (num & 1) == 0:
            # if next bit is 0, then set prev_length = 0, else set prev_length to curr_length
            # and set curr_length to 0
            if (num & 2) == 0:  # pay attention, 0b111 & 2 = 2 
                prev_length = 0
            else:
                prev_length = curr_length
            curr_length = 0
        max_length = max((prev_length + curr_length + 1), max_length)
        # shift the num to the left
        num >>= 1
    return max_length

print(flip_bit(1775))