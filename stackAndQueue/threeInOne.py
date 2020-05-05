"""
3.1 Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #12, #38, #58
"""

class ThreeStack:
	def __init__(self):
		self.arr = []
		self.stackDict = {
			1: None,
			2: None,
			3: None
		}


	def push(self, n, value):
		n = int(n)
		self.arr.append(value)
		if [index == None for index in self.stackDict.values()]:
			self.stackDict[n] = 0
		else:
			self.stackDict[n] += 1
		print(self.arr[self.stackDict[n]])


# main
t = ThreeStack()
t.push(1, 99)
t.push(2, 1)
t.push(1, 22)

print(t.arr)