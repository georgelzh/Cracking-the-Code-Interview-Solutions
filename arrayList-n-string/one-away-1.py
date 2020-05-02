"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Solution
This is one of those problems where it's helpful to think about the "meaning" of each of these 
operations. What does it mean for two strings to be one insertion, replacement, or removal away 
from each other?
Replacement: Consider two strings, such as bale and pale, that are one replacement away. Yes, that 
does mean that you could replace a character in bale to make pale. But more precisely, it means that 
they are different only in one place.
• Insertion: The strings apple and aple are one insertion away. This means that if you compared the 
strings, they would be identical-except for a shift at some point in the strings.
• Removal: The strings apple and aple are also one removal away, since removal is just the inverse of 
insertion.
We can go ahead and implement this algorithm now. We'll merge the insertion and removal check into one 
step, and check the replacement step separately.
Observe that you don't need to check the strings for insertion, removal, and replacement edits. 
The lengths of the strings will indicate which of these you need to check.
"""
import unittest

def is_one_edit_away(str_a, str_b):
	len_a = len(str_a)
	len_b = len(str_b)
	if len_a == len_b:
		return is_one_replacement_away(str_a, str_b)
	elif (len_a + 1) == len_b:
		return is_one_insert_away(str_a, str_b)
	elif (len_b + 1) == len_a:
		return is_one_insert_away(str_b, str_a)
	return False


def is_one_replacement_away(str_a, str_b):
	found_difference = False
	for i in range(len(str_a)):
		if str_a[i] != str_b[i]:
			if found_difference:
				return False
			else: 
				found_difference = True
	return True


# the while loop that tracks two index at the same time is really cool!
# worth learning and practice
def is_one_insert_away(short_str, long_str):
	index1 = 0
	index2 = 0
	edited = False
	while index1 < len(short_str) and index2 < len(long_str):
		if short_str[index1] != long_str[index2]:
			# base case, the second time chars are not the same, return False
			if edited:
				return False
			edited = True
			index2 += 1
		else:
			index1 += 1
			index2 += 1
	return True


class Test(unittest.TestCase):
	'''Test Case'''
	data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
	]

	def test_one_edit_away(self):
		for [s1, s2, expected] in self.data:
			actual = is_one_edit_away(s1, s2)
			self.assertEqual(actual, expected, "Failed test")


if __name__ == "__main__":
	unittest.main()

"""
unittest reference: https://docs.python.org/2/library/unittest.html
github code: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/5_One%20Away/OneAway.py
"""