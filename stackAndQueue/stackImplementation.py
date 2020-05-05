
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
			print(value)
		else:
			self.top.next = Node(value)
			self.top.prev = self.top
			self.top = self.top.next
			print(value)

	def pop(self):
		if self.top is None:
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
		if self.top is None:
			return True
		else:
			return False

	def __str__(self):
		arr = []
		temp = self.top
		while temp is not None:
			arr.append(str(temp.value))
			temp = temp.prev
		return ''.join(arr)
# main
if __name__ == "__main__":
	s = Stack()
	s.isEmpty()
	s.push(1)
	s.push(2)
	print(s)