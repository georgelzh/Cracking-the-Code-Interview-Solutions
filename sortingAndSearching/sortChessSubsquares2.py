"""
given a chessboard, there's white, black colored spots on the board,
each spot has a number on it. 
sort the matrix in black, white color within the square 
starting at upper left corner "row", "col"


solution, 
get the square needed to sort. then
put black, white val into hashmap, sort it and then put 
it back in the matrix.

similar problem
https://leetcode.com/problems/sort-the-matrix-diagonally/

helpful resource:
https://www.youtube.com/watch?v=0FheWgwnG-w&t=159s

extra thoughts:
It is possible to sort it in place. but it seems really difficult to 
get the next black / white location. its possible, think about the
loc for the same color horizontally and diagonally. it's possible but kinda crazy to think about.


anothe way to do this is to store all the white, black spot location in two different list,
sort those two list one by one using bubble sort. that's will be in place but it requires extra memory
"""
from collections import defaultdict
def sortChessBoard(mat, r, c, size):
    d = defaultdict(list)

    for x in mat:
        print(x)

    for row in range(r, r + size):
        for col in range(c, c + size):
            # if black
            if (row - col) % 2 == 0:    # this is the pattern here, write out you will see
                d[0].append(mat[row][col])
            else:                   
                d[1].append(mat[row][col])

    # sort them
    d[0].sort(reverse = True)
    d[1].sort(reverse = True)

    print(d)

    # put them back
    for row in range(r, r + size):
        for col in range(c, c + size):
            # if black
            if (row - col) % 2 == 0:
                mat[row][col] = d[0].pop()
            else:
                mat[row][col] = d[1].pop()
    for x in mat:
        print(x)
    return mat


m1 = [[4,5,6],
[7,8,9],
[1,2,3]]

m2 = [[5,6,7,8],
        [1,2,3,4],
        [13,14,15,16],
        [9,10,11,12]]

sortChessBoard(m2, 1, 1, 3)
print("\n")

sortChessBoard(m2, 2, 0, 2)
print("\n")