"""
5.2
Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
the binary representation. If the number cannot be represented accurately in binary with at most 32
characters, print "ERROR:'
Hints: #143, #167, #173, #269, #297
"""

def printBinary(num):
    """
    first we have a string with '.' in it, that means its decimal, it makes the binary output
    decimal just like how we use '.' to make base 10 number decimal. 
    (since we gonna shift the number in binary form to the left and they are smaller than 1, so
    it has to be decimal, but we leftshift it so that we can tell the binary form. then add it behind
    the decimal to make sure it's still the correct number)

    The rest idea here is to leftshift the number(in binary form) 1 by multiplying the number by 2.
    after shifting, we check if it's bigger than 1, if yes, we add a '1' to the output
    and minus 1 from it.
    Otherwise, we add a 0, repeat the process above. 
    end case is that when the character is equal or greater than 32 and the num is >= than 1,
    we return 'ERROR' in this case. 
    

    for example, the number of 0.5 in binary is 0b0.1. It's 1*2**(-1). 
    0.5(0b0.1) * 2**1 = 0b1
    now we check whether it's equal or bigger than 1, if yes, then it means 
    we can add a '1' to the output string. if no, add a 0, and repeat process above until
    we hit out end case.
    """
    if num >= 1 or num <= 0:
        return "ERROR"
    
    binary = "."
    
    while num > 0:
        # set a limit on length 32 characters
        if len(binary) >= 32:
            return "ERROR"
        
        r = num * 2
        if r >= 1:
            binary += "1"
            num = r - 1
        else:
            binary += "0"
            num = r
    return binary

print(printBinary(0.5)) #0b.1 
print(printBinary(0.75)) #0b.11





def printBinary2(num):
    """
    Alternatively, rather than multiplying the number by two and comparing it to 1, we can compare the
    number to . 5, then . 25, and so on. The code below demonstrates this approach.
    """
    if num >= 1 or num <= 0:
        return "ERROR"
    binary = "."

    frac = 0.5
    while num > 0:
        if len(binary) >= 32:
             return "ERROR"

        if num >= frac:
            binary += "1"
            num -= frac
            frac *= 0.5
        
        else:
            binary += "0"
            frac *= 0.5
    return binary


print(printBinary2(0.5)) #0b.1 
print(printBinary2(0.75)) #0b.11