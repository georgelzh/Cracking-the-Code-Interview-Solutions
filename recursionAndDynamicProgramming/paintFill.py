"""
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
Hints: #364, #382

"""
# dfs - O(nm + 3nm) | O(1) space
# amazing! 

def paintFill(screen, row, col, newColor):
    if screen[row][col] == newColor:
        return False
    print("\n", screen[row][col], row, col)
    return helper(screen, row, col, screen[row][col], newColor)

def helper(screen, row, col, color, newColor):
    if not isInBound(screen, row, col):
        return
    # print("color", color, "curr", screen[row][col], "row", row, "col", col)
    
    # if curr color is the one we want to change
    # change curr color to new color and check curr's neighbours
    if screen[row][col] == color:
        screen[row][col] = newColor
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r, c in dirs:
            newRow, newCol = row + r, col + c
            helper(screen, newRow, newCol, color, newColor)

def isInBound(arr, row, col):
    return row >= 0 and row < len(arr) and col >= 0 and col < len(arr[0])




image1 = [[10, 10, 10, 10, 10, 10, 10, 40],
            [30, 20, 20, 10, 10, 40, 40, 40],
            [10, 10, 20, 20, 10, 10, 10, 10],
            [10, 10, 30, 20, 20, 20, 20, 10],
            [40, 40, 10, 10, 10, 10, 10, 10]]
image2 = [[30, 30, 30, 30, 30, 30, 30, 40],
            [30, 20, 20, 30, 30, 40, 40, 40],
            [10, 10, 20, 20, 30, 30, 30, 30],
            [10, 10, 30, 20, 20, 20, 20, 30],
            [40, 40, 30, 30, 30, 30, 30, 30]]
image3 = [[30, 30, 30, 30, 30, 30, 30, 40],
            [30, 20, 20, 30, 30, 40, 40, 40],
            [30, 30, 20, 20, 30, 30, 30, 30],
            [30, 30, 30, 20, 20, 20, 20, 30],
            [40, 40, 30, 30, 30, 30, 30, 30]]


def test(screen, row, col, newColor):
    print("before")
    for pixel in screen:
        print(pixel)
    paintFill(screen, row, col, "x")
    print("\nAfter\n")
    for pixel in screen:
        print(pixel)
    print("\n")

test(image1, 1, 3, "x")
test(image2, 2, 3, "x")
