"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.

Hints:#150, #185, #200, #267, #278, #309, #335, #356

O(n^2 * n!) time | O(n! * n) space
"""
"""
# approach 1
def perm(string):
    permutations = []
    if len(string) == 0:
        permutations.append("")
        return permutations
    
    first = string[0]
    rem = string[1:]
    words = perm(rem)
    print(words)
    for word in words:
        for i in range(len(word) + 1):
            newElem = insertCharAt(word, first, i)
            permutations.append(newElem)
    return permutations

def insertCharAt(word, char, idx):
    return word[:idx] + char + word[idx:]

string = "abc"
a = perm("", string, arr)
print(arr)
"""
"""
# approach 2
# think backwards, recursion thinking, build from bottom up
def perm(string):
    if len(string) == 1:
        return [string]
    arr = []
    for i in range(len(string)):
        char = string[i]
        rem = string[:i] + string[i + 1:]
        words = perm(rem)
        for word in words:
            arr.append(char + word)
    return arr

string = "abc"
a = perm("", string, arr)
print(a)
"""
def perm(pre, rem, arr):
    if rem == "":
        arr.append(pre)
        print(pre)
    for i in range(len(rem)):
        char = rem[i]
        newRem = rem[:i] + rem[i + 1:]
        newPre = pre + char
        perm(newPre, newRem, arr)

arr = []
string = "abc"
a = perm("", string, arr)
print(arr)



"""
ab:

ab
ba

abc:
cab
acb
abc
cba
bca
bac



abc
acb
bac
bca
cba
cab

abcd:
add d to each position
to get abcd
abcd
acbd
bacd
bcad
cbad
cabd

abdc
acdb
badc
bcda
cbda
cadb

adbc
adcb
bdac
bdca
cdba
cdab

dabc
dacb
dbac
dbca
dcba
dcab
"""