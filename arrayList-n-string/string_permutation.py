"""
compute string permutation

Reference: https://stackoverflow.com/questions/13109274/python-recursion-permutations

becareful about the parameter you are passing. it might cause your program stuck.
I used to change the remain_chars and pass it to the recurssive function, it did not workout.
I tried to have a new variable rem to store the remained_char and it works fine.
"""


def compute_permutation(prefix, remain_chars):
	if len(remain_chars) == 0:
		print(prefix)
		return
	else:	
		for i in range(len(remain_chars)):
			rem = remain_chars[0:i] + remain_chars[i + 1:]
			# print("compute_permutation({0} , {1})".format(prefix, remain_chars))
			compute_permutation(prefix + remain_chars[i], rem)

compute_permutation("","cat")