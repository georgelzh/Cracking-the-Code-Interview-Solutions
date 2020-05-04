from random import randint

class Node:
	def __init__(self, value=None, nextNode=None, prevNode=None):
		self.value = value
		self.next = nextNode
		self.prev = prevNode
	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self, values=None):
		self.head = None
		self.tail = None
		if values is not None:
			self.add_multiples(values)

	def add(self,value):
		if self.head is None:
			self.head = self.tail = Node(value=v)
		else:
			self.tail.next = Node(value=v)
			self.tail = self.tail.next
		return self.tail

	def add_multiple(self, values):
		for v in values:
			self.add(v)

	def __str__(self):
		values = [str[i] for i in self]
		return ' -> '.join(values)

	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next

	def __len__(self):
		result = 0
		node = self.head
		while node:
			result += 1
			node = node.next
		return result

	def add_to_begining(self, value):
		if self.head is None:
			self.head = self.tail = Node(value)
		else:
			self.head = Node(value=value, nextNode=self.head)
		return self.head

	def generate(self, n, min_value, max_value):
		self.head = self.tail = None
		for i in range(n):
			self.add(randint(min_value, max_value))
		return self

	def delete(self, value):
		currNode = self.head
		if currNode.value == value:
			self.head = self.head.next
			return self.head
		while (currNode.next.value != None):
			if(currNode.next.value == value):
				currNode.next = currNode.next.next
				return self.head
			currNode = currNode.next
		return self.head


		

class DoublyLinkedList(LinkedList):
	def add(self, value):
		if self.head is None:
			self.tail = self.head = Node(value=value, prevNode=self.tail)
		else:
			self.tail.next = Node(value=value, prevNode=self.tail)
			self.tail = self.tail.next
		return self

	def delete(self, value):
		currNode = self.head
		if currNode.value == value:
			self.head.next.prev = None
			self.head = self.head.next
			return self.head
		while (currNode.next.value != None):
			if(currNode.next.value == value):
				currNode.next.prev = currNode.prev
				currNode.next = currNode.next.next
				return self.head
			currNode = currNode.next
		return self.head