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
			print(self.top.value)
		elif self.top is not None:
			temp = self.top
			self.top.next = Node(value)
			self.top = self.top.next
			self.top.prev = temp
			print(self.top.value)

	def pop(self):
		if self.top is None:
			return
		if self.top.prev is None:
			print(self.top.value)
			self.top = None
			return
		else:
			print(self.top.value)
			self.top = self.top.prev
			self.top.next = None


	def peek(self):
		if self.top is None:
			return
		else:
			print(self.top.value)
			return self.top.value
	
	def isEmpty(self):
		return self.top is None

	def __str__(self):
		arr = []
		temp = self.top
		while temp is not None:
			arr.append(str(temp.value))
			temp = temp.prev
		return ' <- '.join(arr)

# main
if __name__ == "__main__":
	s = Stack()
	s.isEmpty()
	s.push(1)
	s.push(2)
	s.push(3)

	print(s)

