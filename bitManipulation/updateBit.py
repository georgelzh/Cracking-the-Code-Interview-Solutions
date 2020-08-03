#! Python3

"""
To set the ith bit to a value v, we first clear the bit at position i by using a mask that looks like 11101111.
Then, we shift the intended value, v, left by i bits. This will create a number with bit i equal to v and all
other bits equal to 0. Finally, we OR these two numbers, updating the ith bit if v is 1 and leaving it as 0
otherwise
"""

def updateBit(num, i, bitIs1):
    value = 1 if bitIs1 == True else 0
    
    mask = ~(1 << i) # flip the bits

    return (num & mask) | (value << i)

if __name__ == "__main__":
    assert updateBit(7, 1, False) == 5, "it should be 5"

    """
    7 = 0111,
    mask = 1101
    7 & mask = 0101
    0101 | 0000 = 0101
    """

    assert updateBit(5, 1, True) == 7, "it should be 7"
