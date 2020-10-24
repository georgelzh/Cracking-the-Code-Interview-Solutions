"""

Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result.
EXAMPLE
countEval("1^0|0|1", false) -> 2
countEval("0&0&0&1^1|0", true) -> 10
Hints: #148, #168, #197, #305, #327

brute force
recursion

"""

def countEval(s, result):
    if len(s) % 2 == 0:
        return "wrong input"
    if len(s) == 0:
        return 0
    # here is important check it with the result
    # check whether the base is the same as result return 1 if true, else 0
    if len(s) == 1:
        return 1 if stringToBool(s) == result else 0    
    ways = 0

    for i in range(1, len(s) - 1, 2):   # here pay attention to the ending
        left = s[:i]                    # end before len(s) - 1. because the last elem can't be in the middle
        char = s[i]
        right = s[i + 1:]

        # eval each side for each result
        leftTrue = countEval(left, True)
        leftFalse = countEval(left, False)
        rightTrue = countEval(right, True)
        rightFalse = countEval(right, False)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
    
        totalTrue = 0
        if char == "^":
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        elif char == "&":
            totalTrue = leftTrue * rightTrue
        elif char == "|":
            totalTrue = (leftTrue * rightFalse) + (leftFalse * rightTrue) + (leftTrue * rightTrue)
        subWays = totalTrue if result else total - totalTrue
        ways += subWays
    # print(ways)
    return ways


def stringToBool(s):
    return s == "1"


s = "0&0&0&1^1|0"
a = countEval(s, True)
print(a)


s = "1^0|0|1"
a = countEval(s, False)
print(a)
