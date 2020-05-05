"""
3.1 Three in One: Describe how you could use a single array to implement three stacks.
Hints: #2, #12, #38, #58

Fixed Division
"""

class ThreeStack:
	def __init__(self, stackSize=None):
		self.numberOfStack = 3
		self.stackSize = int(stackSize)
		self.arr = [0] * (self.stackSize * self.numberOfStack)
		self.elementOnStack = [0] * self.numberOfStack


	def push(self, stackNum, value):
		if self.isFull(stackNum):
			print("stack is full")
		else:
			# print(self.getTopOfStack(stackNum))
			self.arr[self.getTopOfStack(stackNum)] = value
			self.elementOnStack[stackNum] += 1

	def pop(self, stackNum):
		if self.getTopOfStack(stackNum) == 0:
			print("stack is empty")
		else:
			self.arr[self.getTopOfStack(stackNum)-1] = 0
			self.elementOnStack[stackNum] -= 1

	def peek(self, stackNum):
		print(self.arr[self.getTopOfStack(stackNum)-1])

	def isFull(self, stackNum):
		return self.elementOnStack[stackNum] == self.stackSize

	def getTopOfStack(self, stackNum):
		return stackNum * self.stackSize + self.elementOnStack[stackNum]


	def __str__(self):
		arr = []
		for i in range(self.numberOfStack * self.stackSize):
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

