"""
3.1 Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #12, #38, #58

Fixed Division
"""

class ThreeStack:
	def __init__(self, stackCapacity=None):
		self.numberOfStack = 3
		self.stackCapacity = int(stackCapacity)
		self.arr = [0] * (self.stackCapacity * self.numberOfStack)
		self.size = [0] * self.numberOfStack


	def push(self, stackNum, value):
		if self.isFull(stackNum):
			print("stack is full")
		else:
			# print(self.getElementNumOnStack(stackNum))
			self.arr[self.getElementNumOnStack(stackNum)] = value
			self.size[stackNum] += 1

	def pop(self, stackNum):
		if self.getElementNumOnStack(stackNum) == 0:
			print("stack is empty")
		else:
			self.arr[self.getElementNumOnStack(stackNum)-1] = 0
			self.size[stackNum] -= 1

	def peek(self, stackNum):
		print(self.arr[self.getElementNumOnStack(stackNum)-1])

	def isFull(self, stackNum):
		return self.size[stackNum] == self.stackCapacity

	def getElementNumOnStack(self, stackNum):
		return stackNum * self.stackCapacity + self.size[stackNum]


	def __str__(self):
		arr = []
		for i in range(self.numberOfStack * self.stackCapacity):
			arr.append(str(self.arr[i]))
		return ' - '.join(arr)

# main
if __name__ == "__main__":
	t = ThreeStack(4)
	t.push(0, 99)
	t.push(0, 99)
	t.push(1, 4)
	t.push(0, 99)
	t.push(2,8)
	t.pop(0)
	t.pop(0)
	t.pop(0)
	t.pop(0)
	print(t)
	t.peek(2)
	t.peek(1)


"""
If we had additional information about the expected usages of the stacks, 
then we could modify this algo­rithm accordingly.For example,if we expected 
Stack1 to have many more elements than Stack2,we could allocate more space to 
Stack 1 and lessspace to Stack 2.
"""