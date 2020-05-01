"""
Is Unique: Implement an algorithm to determine if a string has 
all unique characters. What if you cannot use additional data structures?

Question: check if all the characters in a string are unique in the str.
ask the interviewers whether the string is ASCII code or a Unicode.
"""

def isUniqueChars(str) -> bool:
	if len(str) > 128:
		return False
	char_set_bools = [False for i in range(128)]
	for i in range(0,len(str)):
		ascci_val = ord(str[i])
		if char_set_bools[ascci_val]:
			print("False")
			return False
		else:
			char_set_bools[ascci_val] = True
	print("True")
	return True


isUniqueChars("test")
