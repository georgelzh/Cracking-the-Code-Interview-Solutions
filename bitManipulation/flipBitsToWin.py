#!python3
"""
5.3 
Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1. Write code to
find the length of the longest sequence of 1 s you could create.

EXAMPLE
input: 1775 (or: 11011101111)
output: 8

Hints: #159, #226, #31 4, #352

run time: O(b)
memory O(b)
"""

# process the num and get an array of sequences of numbers of 1s and 0s
def get_sequence(num):
    # look into each bits and get the sequence
    seq = []
    binaryStr = bin(num)[2:]

    searchFor = 0
    counter = 0

    for _ in range(0, len(binaryStr)):
        # take the most right bit check if it equals to the search for value
        if (num & 1) != searchFor:
            # add the counter to seq
            seq.append(counter)
            # flip the searchFor variable
            searchFor = num & 1
            # reset the counter
            counter = 0
        # important steps that made sure that that whenever the bit was flipped,
        # the coming bit will be gone bc it will be shifted, so the counter +=1 made sure
        # that bit was also counted!!
        counter += 1    
        # shift the num to the left by 1 so that we can process next bit
        num >>= 1
        print(seq)

    seq.append(counter)
    return seq

# find the max num
def find_max_seq(seq):
    # the first element of the sequence represents num of 0s
    max_1s = 1

    for i in range(0, len(seq), 2): # we loop through all the 0s counts
        # merge condition
        zeros_seq = seq[i]
        # since arr index starts at 0, i+1 should be be less than len(seq) -1
        ones_seq_left = seq[i+1] if i < len(seq)-1 else 0
        ones_seq_right = seq[i-1] if i > 0 else 0

        ones_this_seq = 0
        if zeros_seq == 1:
            ones_this_seq = ones_seq_left + 1 + ones_seq_right 
            max_1s = max(max_1s, ones_this_seq) # update the max_1s
        
        # no merge condition
        if zeros_seq > 1:
            ones_this_seq = max(ones_seq_left, ones_seq_right) + 1
            max_1s = max(max_1s, ones_this_seq) # update the max_1s

        # no zeros, take the bigger side
        elif zeros_seq == 0:
            ones_this_seq = max(ones_seq_left, ones_seq_right)
    return max_1s


def get_longest_sequence(num):
    # if it's -1, it's already the longest sequence of 1s
    if num == -1:
        return len(bin(num)[2:])
    
    seq = get_sequence(num)
    return find_max_seq(seq)

if __name__ == "__main__":
    print(get_longest_sequence(1775))
    print(get_sequence(1775))
