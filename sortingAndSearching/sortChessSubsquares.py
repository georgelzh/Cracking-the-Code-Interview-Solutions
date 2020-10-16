"""
given a chessboard, there's white, black colored spots on the board,
each spot has a number on it. sort the matrix in black, white color

solution, put black, white val into hashmap, sort it and then put 
it back in the matrix.
"""
from collections import defaultdict
def sortChessBoard(mat):
    d = defaultdict(list)

    for x in mat:
        print(x)

    for row in range(len(mat)):
        for col in range(len(mat[0])):
            # if black
            if (row - col) % 2 == 0:
                d[0].append(mat[row][col])
            else:
                d[1].append(mat[row][col])

    # sort them
    d[0].sort(reverse = True)
    d[1].sort(reverse = True)

    print(d)

    # put them back
    for row in range(len(mat)):
        for col in range(len(mat[0])):
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

sortChessBoard(m1)