"""
Palindrome Permutation: Given a string, write a function to check if it is 
a permutation of a palin­ drome. A palindrome is a word or phrase that is the 
same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.

Brute Force method
"""

def is_palindrome_permutation(str):
	# make sure its possible to be palindrome before computing permutation
	# check if the letters are all divisible by 2
	# only one letter is allowed to appear only once
	dict = {}
	arr = []
	occured_once_char_counter = 0
	removed_str_counter = 0
	for char in str:
		if char not in dict.keys():
			dict[char] = 1
		else:
			dict[char] += 1
	for k,v in dict.items():
		if (v % 2) == 0:
			continue
		else:
			occured_once_char_counter += 1
	if occured_once_char_counter > 1:
		return False

	arr = compute_permutation("", str, arr)
	for i in range(len(arr)):
		if not is_palindrme(arr[i - removed_str_counter]):
			arr.remove(arr[i - removed_str_counter])
			removed_str_counter += 1

	if len(arr) > 0:
		print("True, (permutation: {0})".format(arr))
		return True




def compute_permutation(prefix, remains, arr):
	if len(remains) == 0:
		if prefix not in arr:
			arr.append(prefix)
			return
		return
	else:
		for i in range(0, len(remains)):
			rem = remains[:i] + remains[i+1:]	
			compute_permutation(prefix + remains[i], rem, arr)
	return arr


def is_palindrme(str):
	# reverse the str and compare
	if str == str[::-1]:
		print("yes")
		return True
	else:
		return False


if __name__ == "__main__":
	is_palindrome_permutation("baa")