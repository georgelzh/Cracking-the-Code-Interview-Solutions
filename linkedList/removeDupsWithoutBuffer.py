"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40
set/hashtable: https://www.geeksforgeeks.org/sets-in-python


use runner technique

takes O(N^2) time
"""


def removeDups(head):
	curr = head
	while curr != None:
		runner = curr
		while runner.next != None:
			if curr.value == runner.next.value:
				runner.next = runner.next.next
			else:
				runner = runner.next
		curr = curr.next
	return head

class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next


if __name__ == "__main__":
	head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
	head = removeDups(head)
	n = head
	while n != None:
		print(n.value)
		n = n.next
