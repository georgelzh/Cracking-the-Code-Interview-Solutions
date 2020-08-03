#!Python3



def clearBit(num, i):
    """This method operates in almost the reverse of setBit. First, we create a number like 11101111 by creating
    the reverse of it (00010000) and negating it. Then, we perform an AND with num. This will clear the ith bit
    and leave the remainder unchanged."""
    # make a mask
    mask = ~(1 << i)    # negate all the bit to make the mask
    return num & mask



def clearBitsMSBthroughI(num, i):
    """
    To clear all bits from the most significant bit through i (inclusive), we create a mask with a 1 at the ith bit (1
    < < i). Then, we subtract 1 from it, giving us a sequence of 0s followed by i ls. We then AND our number
    with this mask to leave just the last i bits.

    9 = 0b1001
    i = 2 -> 1 << 2 = 0b0100
    0b0100 - 1 = 0b0011

    0b1001 & 0b0011 = 0b0001
    """
    mask = (1 << i) - 1
    return num & mask

def clearBitsIthrough0(num, i):
    """
    To clear all bits from i through 0 (inclusive), we take a sequence of all ls (which is -1) and shift it left by i
    + 1 bits. This gives us a sequence of 1 s (in the most significant bits) followed by i 0 bits.
    """
    mask = -1 << (i+1)
    return num & mask


if __name__ == "__main__":
    assert clearBit(3, 0) == 2, "It should be 2"
    assert clearBitsMSBthroughI(11, 2) == 3, "it should be 3" # 11=  1011, 3 = 0011, i = 2
    assert clearBitsMSBthroughI(9, 2) == 1, "It should be 1"
    assert clearBitsIthrough0(11, 2) == 8, "it should be 8"