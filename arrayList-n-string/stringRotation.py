"""
String Rotation:Assumeyou have a method isSubstringwhich checks if one 
word is a substring of another. Given two strings, sl and s2, write code 
to check if s2 is a rotation of sl using only one call to isSubstring 
(e.g.,"waterbottle" is a rotation of"erbottlewat").
Hints:#34,#88, #104
51 = xy = waterbottle
x = wat
y = erbottle
s2 = yx = erbottlewat
So, we need to check if there's a way to split s1 into x andy such 
that xy = s1 andyx = s2. Regardless of where the division between x 
andy is, we can see thatyx will always be a substring of xyxy.That is, 
s2 will always be a substring of s1s1.

And this is precisely how we solve the problem: simply do isSubstring(slsl, s2).
"""


def isRotation(s1, s2):
	return (s2 in s1*2)

# main
s1 = "hiyou"
s2 = "youhi"

assert isRotation(s1, s2) == True, "failed test"
