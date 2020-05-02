"""
Palindrome Permutation: Given a string, write a function to check if it is 
a permutation of a palin­ drome. A palindrome is a word or phrase that is the 
same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
----------------------------------------------------------------
optimized space method with O(n) run time
----------------------------------------------------------------
If you think more deeply about this problem, you might notice that we don't actually need 
to know the counts. We just need to know if the count is even or odd. Think about flipping 
a light on/off (that is initially off). If the light winds up in the off state, we don't know 
how many times we flipped it, but we do know it was an even count.
Given this, we can use a single integer (as a bit vector). When we see a letter, we map it to 
an integer between O and 26 (assuming an English alphabet). Then we toggle the bit at that value.
 At the end of the iteration, we check that at most one bit in the integer is set to 1.
We can easily check that no bits in the integer are 1: just compare the integer to 0. There 
'is actually a very elegant way to check that an integer has exactly one bit set to 1.
Picture an integer like 00010000. We could of course shift the integer repeatedly to check 
that there's only a single 1. Alternatively, if we subtract 1 from the number, 
we'll get 00001111. What's notable about this is that there is no overlap between the 
numbers (as opposed to say 00101000, which, when we subtract 1 from, we get 00100111.) 
So, we can check to see that a number has exactly one 1 because if we subtract 1 from it 
and then AND it with the new number, we should get 0.
00010000 - 1 = 00001111 
00010000 & 00001111 = 0
"""

def is_palindrome_permutation(str) -> bool:
	bit_vector = 0
	return bit_vector == 0 or check_exactly_one_bit_set(bit_vector)	

def get_char_number(char):
	a = ord('a')
	z = ord('z')
	val = ord(char)
	if (a <= val) and (val >= z):
		return val - a
	return -1

def toggble(bit_vector, index):
	if index < 0: return bit_vector
	mask = 1 << index
	if ((bit_vector & mask) == 0):
		bit_vector |= mask
	else:
		bit_vector &= ~mask
	return bit_vector

def create_bit_vector(str):
	bit_vector = 0
	for char in str:
		val = get_char_number(char)
		bit_vector = toggle(bit_vector, val)
	return bit_vector 

def check_exactly_one_bit_set(bit_vector):
	return (bit_vector & (bit_vector -1)) == 0


result = is_palindrome_permutation("duckud")
print(result)

"""
reference
check size of an variable: https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python

bit operator ~: https://www.tutorialspoint.com/java/java_basic_operators.htm
"""
