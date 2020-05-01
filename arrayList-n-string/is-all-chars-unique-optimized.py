# For understanding the algorithm - bit operation,
"""
bin: binary
0 - bin: 00000000
1 - bin: 00000001
2 - bin: 00000010
3 - bin: 00000011
4 - bin: 00000100
8 - bin: 00001000

for 26 letters, we an just use 26 bits to represent each letter.
a - 00000000000000000000000001
b - 00000000000000000000000010
c - 00000000000000000000000100
d - 00000000000000000000001000

if we want to check if any letters repeated in the string,
we first,  use | operation to combine all the binary of occured letters.
for eg:
a - 00000000000000000000000001
b - 00000000000000000000000010
a | b = 00000000000000000000000011
a | b | c = 00000000000000000000000111
if all letters occured only once, the final result will be 
11111111111111111111111111
zyxwvutsrqpomilkjihgfedcba
at this point, if one more a occurs in the str,

we check 00000000000000000000000001 & 11111111111111111111111111
the result will be 1, and that means a occured at least more than once.
in this case, we return false.

# eg code for better understanding
r = 0
for i in range(0,26):
	r = r | (1 << i)
	# when reperition occurs, return false, then break
	# if (r & (1<<11)):
	# 	print("false")
	# 	break
	print(format(1<<i, "32b"))
	print(format(r, "32b"), "\n")
"""

def is_all_chars_unique(str):
	str = str.lower()
	binary_checker = 0
	letter_a_ascii = ord('a')
	for i in range(0, len(str)):
		letter_ascii_val =  ord(str[i])
		if (letter_ascii_val < 97) or (letter_ascii_val > 122): # take non letter characters out
			continue
		val = ord(str[i]) - letter_a_ascii # ord convert char to ascci code
		letter_binary_val = (1 << val)
		if (binary_checker & (letter_binary_val)) > 0:
			print("False")
			return False
		else:
			binary_checker = binary_checker | letter_binary_val
	print("True")
	return True

is_all_chars_unique("hello world")


"""
reference:
ascii table: http://www.asciitable.com/
print binary in python: https://stackoverflow.com/questions/10411085/converting-integer-to-binary-in-python
bitwise operator in python: https://data-flair.training/blogs/python-bitwise-operators/
"""
