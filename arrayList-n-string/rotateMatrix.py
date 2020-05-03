"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the 
image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints:#51, #100

This algorithm is O(N^2), which is the best we can do since any algorithm must touch all N2 elements.

under this condition, the algorithm fails to check whether its a n*n matrix
arr = [
		["1"],
		['3','4']
		]

"""



arr = [
		["1",'2','3'],
		['4','5','6'],
		['7','8','9']
		]

def rorateMetrix(matrix):
	if len(matrix) == 0 or len(matrix)!= len(matrix[0]):
		return False
	n = len(matrix)
	for layer in range(int(n/2)):
		first = layer
		last = n - 1 - layer
		for i in range(first, last):
			offset = i - first
			top = matrix[first][i] # SAVE top
			# top = left
			matrix[first][i] = matrix[last - offset][first]

			# left = bottom
			matrix[last - offset][first] = matrix[last][last - offset]

			# bottom = right
			matrix[last][last - offset] = matrix[i][last - offset]

			# right = top
			matrix[i][last - offset] = top

			# for understanding
			# print("top: ", first, " ", [i])
			# print("left: ", last - offset, " ", [first])
			# print("bottom: ", last, " ", last - offset)
			# print("right: ", i, " ", last - offset)
	return arr

assert rorateMetrix(arr) == [['7', '4', '1'], ['8', '2', '6'], ['9', '5', '3']], "code is not doing the job"
