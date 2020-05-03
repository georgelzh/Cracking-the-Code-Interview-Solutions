"""
1.8 Zero Matrix: Write an algorithm such that if an element 
in an MxN matrix is 0, its entire row and column are set to 0.
Hints:#17, #74, #702

Notice: here we comparing the value with '0' instead of int(0).
it's adjustitable, depends on the input.

if we keep track of all zero matrix[row][column], the max space complexity will be O(MN).
Instead, we keep track of rows and columns needed to be zeroed seprately. that will need 
O(M+N) space
"""


def ZeroMatrix(matrix):
	zeroRow = []
	zeroColumn = []
	for row in range(len(matrix)):
		for column in range (len(matrix[0])):
			if matrix[row][column] == '0':
				if row not in zeroRow:
					zeroRow.append(row)
				if column not in zeroColumn:
					zeroColumn.append(column)

	if len(zeroRow) > 0:
		for row in zeroRow:
			setRowZero(matrix, row)

	if len(zeroColumn) > 0:
		for column in zeroColumn:
			setColumnZero(matrix, column)
	return True

def setRowZero(matrix, row):
	for i in range(len(matrix[0])):
		matrix[row][i] = '0'
	return True

def setColumnZero(matrix, column):
	for i in range(len(matrix)):
		matrix[i][column] = '0'
	return True

# main
arr = [
		["1",'2','3'],
		['4','5','6'],
		['7','0','9']
		]

ZeroMatrix(arr)
print(arr[0])
print(arr[1])
print(arr[2])