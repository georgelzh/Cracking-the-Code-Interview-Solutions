"""
Check Permutation: Given two strings, write a method 
to decide if one is a permutation of the other.

sort both str and compare, it takes O(n)
"""
import datetime

def check_permutation(str_a, str_b):
	if len(str_a) != len(str_b):
		return False
	str_a = sorted(str_a)
	str_b = sorted(str_b)
	result = (str_a == str_b)
	return result


# main
begin_time = datetime.datetime.now()
a = check_permutation("hello","helb")
print(a)

# run time
print(datetime.datetime.now() - begin_time)
