"""
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index)which performs a pop operation on a specific sub-stack.
Hints:#64, #87

"""

class stackOfPlates:
	def __init__(self, capacity):
		self.capacity = capacity
		self.stack =[]

	def push(self, value):
		if len(self.stack) == 0 or len(self.stack[-1]) == self.capacity:
			self.stack.append([value])
			return value
		else:
			self.stack[-1].append(value)
			return value

	def pop(self):
		if len(self.stack) ==0:
			return None
		if len(self.stack) > 0 and len(self.stack[-1]) > 0:
			self.stack[-1].pop()

		if len(self.stack[-1]) == 0:
			self.stack.pop()

	def __str__(self):
		arr = []
		for stack in self.stack:
			for item in stack:
				arr.append(str(item))
		return ' -> '.join(arr)

	def popAt(self, stackNum):
		n = len(self.stack) - 1
		if stackNum <= n and stackNum >= 0:
			self.stack[stackNum].pop()
		else:
			return None

# main
if __name__ == "__main__":
	s = stackOfPlates(3)
	s.push(1) == 1, "failed"
	s.push(2) == 2, "failed"
	s.push(3)
	s.push(3)
	print(s)

	s.push(99)
	print(s)

	s.pop()
	print(s)

	s.popAt(1)
	print(s)
	s.push(9)
	s.push(8)
	s.push(8)
	s.push(100)
	print(s)
	s.popAt(2)
	print(s)
# reference: https://github.com/w-hat/ctci-solutions/blob/master/ch-03-stacks-and-queues/03-stack-of-plates.py

