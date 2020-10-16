"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
Hints: #331, #360, #388

# use hashmap to improve the time complexity

If we picture this grid, the only way to move to spot ( r, c) is by moving to one of the adjacent spots:
( r -1, c) or ( r, c -1). So, we need to find a path to either ( r-1, c) or ( r, c -1).
How do we find a path to those spots? To find a path to ( r-1, c) or ( r, c -1), we need to move to one
of its adjacent cells. So, we need to find a path to a spot adjacent to ( r-1, c), which are coordinates
( r- 2, c) and ( r-1, c -1). or a spot adjacent to ( r, c -1). which are soots ( r- L c -1) and ( r. c -2).
Observe that we list the point ( r-1, c -1) twice; we'll discuss that issue later

O(2^(n+m)) time | O(nm) space
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

arr = [[0, 0, 1, 0], 
 [0, 1, 0, 0],
 [0, 0, 0, 1],
 [0, 0, 0, 0]]

def findPath(matrix, r, c):
    hashmap = {}
    result = helper(matrix, r, c, [], hashmap)
    return result


def helper(matrix, r, c, result, hashmap):
    print("1", end="")
    # base
    if not isInBound(matrix, r, c):
        return None
    if matrix[r][c] == -1:
        return None
    
    loc = str(r) + "-" + str(c)
    if loc in hashmap:
        return None
    if r == len(matrix) - 1 and c == len(matrix[0]) - 1:
        result.append([r, c])
        return result
    
    hashmap[loc] = True
    result.append([r, c])
    # down
    downResult = helper(matrix, r + 1, c, result[:], hashmap)
    if downResult != None:
        return downResult

    # right
    rightResult = helper(matrix, r, c + 1, result[:], hashmap)
    if rightResult != None:
        return rightResult
    return None

def isInBound(matrix, r, c):
    return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0])

if __name__ == "__main__":
    result = findPath(grid, 0, 0)
    print(result)