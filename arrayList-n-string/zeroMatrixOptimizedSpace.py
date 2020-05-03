"""
1.8 Zero Matrix: Write an algorithm such that if an element 
in an MxN matrix is 0, its entire row and column are set to 0.
Hints:#17, #74, #702

use first row and columns to store zero values of its row and column for zeroing.
uses only O(1) space

"""

def ZeroMatrix(matrix):
	firstRowHasZero = False
	firstColumnHasZero = False
	# check if there is any zero in first row
	for i in range(len(matrix[0])):
		if matrix[0][i] == 0:
			firstRowHasZero = True
	# check if there is any zero in first column
	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			firstColumnHasZero = True

	# check the whole matrix and if the row or column has zero, 
	# store it on the first column or row.
	for row in range(len(matrix)):
		for column in range (len(matrix[0])):
			if matrix[row][column] == 0:
				matrix[row][0] = 0
				matrix[0][column] = 0

	# zero rows based on the values in first row
	for row in range(len(matrix)):
		if matrix[row][0] == 0:
			setRowZero(matrix, row)

	# zero columns based on the values in first row
	for column in range(len(matrix[0])):
		if matrix[0][column] == 0:
			setColumnZero(matrix, column)

	# zero out first row it has any zero value originally
	if firstRowHasZero:
		for row in zeroRow:
			setRowZero(matrix, 0)

	# zero out first column it has any zero value originally
	if firstColumnHasZero:
		for column in zeroColumn:
			setColumnZero(matrix, 0)

	return True

def setRowZero(matrix, row):
	for i in range(len(matrix[0])):
		matrix[row][i] = 0
	return True

def setColumnZero(matrix, column):
	for i in range(len(matrix)):
		matrix[i][column] = 0
	return True

# main
arr = [
		[1,2,3],
		[4,0,6],
		[7,9,9]
		]

ZeroMatrix(arr)
print(arr[0])
print(arr[1])
print(arr[2])