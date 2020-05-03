"""
String Compression: Implement a method to perform basic string compression using 
the counts of repeated characters. For example, the string aabcccccaaa would become 
a2blc5a3. If the "compressed" string would not become smaller than the original string, 
your method should return the original string. You can assume the string has only 
uppercase and lowercase letters (a - z).
Hints:#92, #110

runtime - O(n)

write a program to check whether the compression is worth it, if the length of compressedString
is not shorter than original string, we will not compress it. it saves avoids the extra work.
the downside is that it causes a second loop through the characters and also adds nearly duplicated code.

it can be removed, according to the kind of input string.

"""

def stringCompression(inputString):
	if countCompression(inputString) > len(inputString):
		return inputString

	compressedString = []
	count = 0
	for i in range(len(inputString)):
		count += 1
		currentChar = inputString[i]

		# if current char is different than next one, append the result
		# Attention!
		#if (i+1 == len(inputString)) or (currentChar != inputString[i+1]): is different from
		# if (currentChar != inputString[i+1]) or (i+1 == len(inputString)):

		if (i+1 == len(inputString)) or (currentChar != inputString[i+1]):
			compressedString.append(currentChar) 
			compressedString.append(str(count))
			count = 0

	if len(compressedString) < len(inputString):
		return ''.join(compressedString)
	else:
		return inputString

def countCompression(inputString):
	count = 0
	for i in range(len(inputString)):
		compressionLength = 0
		count += 1
		currentChar = inputString[i]
		# if current char is different than next one, append the result
		# Attention!
		#if (i+1 == len(inputString)) or (currentChar != inputString[i+1]): is different from
		# if (currentChar != inputString[i+1]) or (i+1 == len(inputString)):

		if (i+1 == len(inputString)) or (currentChar != inputString[i+1]):
			compressionLength += count
			count = 0
	return compressionLength


if __name__ == "__main__":
	result = stringCompression("ffffffffffuuckyou")
	print(result)


"""
string.isalpha() : https://www.geeksforgeeks.org/python-string-isalpha-application/

"""

		