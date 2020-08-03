#!Python3

"""Set Bit shifts 1 over by i bits, creating a value like 00010000. By performing an OR with num, only the
value at bit i will change. All other bits of the mask are zero and will not affect num."""

def setBit(num, i):
    return num | (1 << i)


if __name__ == "__main__":
    assert setBit(2, 0) == 3, "It should be 3"
