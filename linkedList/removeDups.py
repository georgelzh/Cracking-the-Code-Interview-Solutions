"""
Remove Dups! Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40
set/hashtable: https://www.geeksforgeeks.org/sets-in-python

O(N) time, N is the number of the elements in the linked list

In order to remove duplicates from a linked list, we need to be able to track 
duplicates. A simple hash table will work well here.
In the below solution, we simply iterate through the linked list, adding each 
element to a hash table. When we discover a duplicate element, we remove the 
element and continue iterating. We can do this all in one pass since we are 
using a linked list.
"""


def removeDups(n):
	set1 = set()
	prev = None
	while n: 
		if n.value in set1:
			prev.next = n.next
		else:
			set1.add(n.value)
			prev = n
		n = n.next
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
