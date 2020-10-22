"""
Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.
Hints: #308, #350, #371

https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

play by rows - backtracking

check whether it's safe to put it there.
when we done with it, we take the queen back from the board
"""

def placeQueens(board, row, results):
    n = len(board)
    if row >= n:
        printSolution(board)
        print("\n")
        results.append(board[:])
        
    # consider this row and try all cols 1 by 1
    for col in range(n):
        # print(row, col)
        if isSafe(board, row, col):
            board[row][col] = "Q" # place queen
            placeQueens(board, row + 1, results)
            board[row][col] = 0  # if there's no way to arrange it there, take queen back
            
def isSafe(board, row, col):
    n = len(board)
    for r in range(row):
        # check if if r and row share the same col, 
        if board[r][col] == "Q":
            return False
    # check upper left diagonally
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == "Q":
            return False
    # check upper right diagonally
    for r, c in zip(range(row, -1, -1), range(col, n)):
        if board[r][c] == "Q":
            return False
    return True

def printSolution(board): 
    n = len(board)
    for i in range(n): 
        for j in range(n): 
            print (board[i][j], end = " ") 
        print()

def solveNQueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []
    placeQueens(board, 0, results)


solveNQueens(4)
