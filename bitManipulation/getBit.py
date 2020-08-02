#!python3
# check whether the ith bit is 1 or 0


def getBit(num, i):
    """
    1 in binary is 0b0001
    note that, i can be 0, when i is 0, that means (1 << 0) == 0b0001.
                            when i is 1, we get (1 << 1) == 0b0010
    """
    return (num & (1 << i)) != 0


if __name__ == "__main__":
    assert getBit(3, 1)== True, "should be True"
    assert getBit(5, 0)== True, "(5, 0) should be True"
    assert getBit(5, 1)== False, "(5, 1) should be False"