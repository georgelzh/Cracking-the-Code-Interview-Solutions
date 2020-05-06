"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
Hints: #98, #7 74
"""

class MyQueue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []
	
	def add(self, value):
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			self.stack1.append(value)
			return value
		else:
			self.stack2.append(value)
			return value
	
	def remove(self):
		if len(self.stack1) == 0:
			self.reverseStackElement()
			if len(self.stack1) == 0:
				return None
			else:
				return self.stack1.pop()
		elif len(self.stack1) > 0:
			return self.stack1.pop()
	
	def peek(self):
		self.reverseStackElement()
		if len(self.stack1) > 0:
			return self.stack1[-1]
		else:
			return None

	def isEmpty(self):
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			return True
		else:
			return False
	def reverseStackElement(self):
		while len(self.stack2) > 0:
			self.stack1.append(self.stack2.pop())


if __name__ == "__main__":
	q = MyQueue()
	assert q.add(4) == 4, "Failed"
	assert q.add(5) == 5, "Failed"
	assert q.add(6) == 6, "Failed"
	assert q.add(7) == 7, "Failed"
	assert q.remove() == 4, "Failed"
	assert q.remove() == 5, "Failed"
	assert q.peek() == 6, "Failed"
	assert q.isEmpty() == False, "Failed"
	
