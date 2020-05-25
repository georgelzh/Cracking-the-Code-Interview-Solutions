
# variable could be changed within a function using a function.
# and the changes remains.
def sum():
    a = [None for i in range(5)]
    add_one(a)
    return a

def add_one(num):
    num[3] = 9

print(sum())