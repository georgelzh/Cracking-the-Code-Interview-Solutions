

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev


class Queue:
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, value):
		if self.head is None:
			self.head = self.tail = Node(value)
			print(self.head.value)
		elif self.head is not None:
			temp = self.tail
			self.tail.next = Node(value)
			self.tail = self.tail.next
			self.tail.prev = temp
			print(self.tail.value)

	def remove(self):
		if self.head is None:
			print("Queue is empty")
			return
		if self.head == self.tail:
			print(self.head.value)
			self.top = self.tail = None
			return
		else:
			print(self.head.value)
			self.head = self.head.next
			self.head.prev = None

	def peek(self):
		if self.head is None:
			print("empty queue")
			return
		else:
			print(self.head.value)
			return self.head.value
	
	def isEmpty(self):
		return self.head is None

	def __str__(self):
		arr = []
		temp = self.head
		while temp is not None:
			arr.append(str(temp.value))
			temp = temp.next
		return ' <- '.join(arr)

# main
if __name__ == "__main__":
	q = Queue()
	q.isEmpty()
	q.add(1)
	q.add(2)
	q.add(3)
	print(q)
	q.remove()
	print(q)


"""
It is especially easy to mess up the updating of the first and last nodes 
in a queue. Be sure to double check this. 
One place where queues are often used is in breadth-first search or in implementing a cache.
In breadth-first search, for example, we used a queue to store a list of 
the nodes that we need to process. Each time we process a node, we add its 
adjacent nodes to the back of the queue. This allows us to process nodes 
in the order in which they are viewed.
"""