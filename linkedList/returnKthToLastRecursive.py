"""
2.2 Return Kth to Last: Implement an algorithm to find the kth to 
last element of a singly linked list.

recursive way to do this. takes O(n) space

Regardless of which solution we pick, we need a way to update both 
the node and the counter in a way that all levels of the recursive 
stack will see.
"""


def printKthToLast(node, k):
	# base case, only if node == None, return 0, from here 
	# we recursively go backwards and count up to k
	if node == None:
		return 0
	node = node.next

	# when hit null, starts to increase index by 1, 
	# only print when index hits k
	index = printKthToLast(node, k) + 1
	if index == k:
		print("Found it! {0} is the kth to last node".format(node.value))

	# otherwise, return index, keep recursively going backwards with value index as k
	return index


class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next


if __name__ == "__main__":
	head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
	printKthToLast(head, 3)

