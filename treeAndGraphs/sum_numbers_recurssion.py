"""
basic recursion experiment

add from 0 to 10
1 + 2 + 3 + ...
sum = 55
"""
def add_to_ten(sum, index):
    if index == 10:
        sum += index
        return sum
    else:
        sum += index
        sum = add_to_ten(sum, index +1)
        return sum

a = add_to_ten(0, 0)
print("a: ", a)