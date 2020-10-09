"""
Permutations with Dups: Write a method to compute all permutations of a string whose charac­
ters are not necessarily unique. The list of permutations should not have duplicates.
Hints:#161, #190, #222, #255
"""
def perm(s):
    arr = []
    from collections import Counter
    counts = Counter(s)
    printPerm(counts, "", len(s), arr)
    print(counts)
    return arr

def printPerm(counts, pre, rem, result):
    print(pre)
    if rem == 0:
        result.append(pre)
    for char in counts.keys():
        print(pre, rem)
        count = counts.get(char)
        if count > 0:
            counts[char] -= 1
            printPerm(counts, pre + char, rem - 1, result)
            counts[char] += 1

a = perm("abc")
print(a)

a = perm("aabc")
print(a)
