"""
One case where stacks are often useful is in certain recursive algorithms. 
Sometimes you need to push temporary data onto a stack as you recurse, but 
then remove them as you backtrack (for example, because the recursive check 
failed). A stack offers an intuitive way to do this.
A stack can also be used to implement a recursive algorithm iteratively. 
(This is a good exercise! Take a simple recursive algorithm and implement 
it iteratively.)

the code in the book used next at the top node to store previous node.
in that case, prev is no longer needed
"""
from collections import deque

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev


class Stack:
	def __init__(self):
		self.top = None

	def push(self, value):
		if self.top is None:
			self.top = Node(value)
			# print("min: ", self.top.value)
		elif self.top is not None:
			temp = self.top
			self.top.next = Node(value)
			self.top = self.top.next
			self.top.prev = temp
			# print("min: ", self.top.value)

	def pop(self):
		if self.top is None:
			return
		if self.top.prev is None:
			# print(self.top.value)
			self.top = None
			return
		else:
			# print(self.top.value)
			self.top = self.top.prev
			self.top.next = None


	def peek(self):
		if self.top is None:
			return
		else:
			return self.top.value
	
	def isEmpty(self):
		return self.top == None

	def __str__(self):
		arr = []
		temp = self.top
		while temp is not None:
			arr.append(str(temp.value))
			temp = temp.prev
		return ' <- '.join(arr)


class StackMin(Stack):
	def __init__(self):
		Stack.__init__(self)
		self.mins = Stack()
		self.top = None

	def push(self, value):
		if self.top is None:
			self.mins.push(value)
			self.top = Node(value)

			print("first node: ", self.top.value)
		else:
			if (value <= self.getMin()):
				self.mins.push(value)

			temp = self.top
			self.top.next = Node(value)
			self.top = self.top.next
			self.top.prev = temp
			print("new node: ", self.top.value)

	def pop(self):
		if self.top is None:
			return "Empty Stack"
		if self.top.prev is None:
			print(self.top.value)
			self.mins.pop()
			self.top = None
			return
		else:
			print(self.top.value)
			self.mins.pop()
			self.top = self.top.prev
			self.top.next = None

	def getMin(self):
		return self.mins.peek()



# main
if __name__ == "__main__":
	s = StackMin()
	s.push(99)
	s.push(78)
	s.push(67)
	print(s.getMin())
	s.push(2)
	print(s.getMin())


"""
override __init__ python: https://help.semmle.com/wiki/display/PYTHON/__init__+method+calls+overridden+method
https://www.geeksforgeeks.org/extend-class-method-in-python/
"""