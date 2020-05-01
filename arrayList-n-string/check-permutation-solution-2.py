# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

# make a dictionary to record number of each letter occurs
# then go to the string b and decrease numbers in the dictionary
# once it meets a word in the dictionary.
# if any value in the dictionary is bigger than 0 or smaller in the end, return False
# when both str have the same common chars, and all values in the dictionary are zero,
# return true
import datetime

def check_permutation(str_a, str_b):
	dict = {}
	if len(str_a) != len(str_b):
		return False

	for char in str_a:
		if char not in dict.keys():
			dict[char] = 1
		else:
			dict[char] += 1
	
	for char in str_b:
		if char in dict.keys():
			dict[char] = dict[char] - 1

	for char in dict.keys():
		if char not in str_b:
			return False

	for k, v in dict.items():
		if v > 0:
			return False
		if v < 0:
			return False


# main
begin_time = datetime.datetime.now()
a = check_permutation("hello","helb")
print(a)

# run time
print(datetime.datetime.now() - begin_time)

"""
keyError: "key name" Error info: https://realpython.com/python-keyerror/
sort string: https://www.w3schools.com/python/ref_func_sorted.asp
sort list or arr: https://docs.python.org/3/howto/sorting.html
run time: https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
"""