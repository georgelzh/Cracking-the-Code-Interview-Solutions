"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
Hints: #331, #360, #388

So then, to find a path from the origin, we just work backwards like this. Starting from the last cell, we try to
find a path to each of its adjacent cells. The recursive code below implements this algorithm

O(2^(r + c)) time | O(r + c) space
"""
grid = [[0, 0, 0, 0, 0, 0, 1],
        [0, -1, -1, -1, -1, -1, -1],
        [0, 1, 1, 0, 0, -1, 0],
        [1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]]

def findPath(matrix, r, c):
    if len(matrix) == 0:
        return None
    result = []
    if helper(matrix, r, c, result):
        return result
    return None


def helper(matrix, r, c, result):
    print("1",end="")
    if not isInBound(matrix, r, c) or matrix[r][c] == -1:
        return False
    
    isAtOrigin = r == 0 and c == 0

    if isAtOrigin or helper(matrix, r - 1, c, result) or helper(matrix, r, c - 1, result):
        result.append([r, c])
        return True
    return False

def isInBound(matrix, r, c):
    return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0])

if __name__ == "__main__":
    result = findPath(grid, len(grid) - 1, len(grid[0]) - 1)
    print(result)