"""
A more optimal, but less straightforward, solution is to implement 
this iteratively. We can use two pointers, pl and p2. We place them 
k nodes apart in the linked list by putting p2 at the beginning and 
moving pl k nodes into the list. Then, when we move them at the same 
pace, pl will hit the end of the linked list after LENGTH - ksteps.
Atthatpoint,p2 willbeLENGTH - knodesintothelist,orknodesfromtheend.


This algorithm takes O(n) time and 0(1) space.
"""
class Node:
	def __init__(self, value, next):
		self.value = value
		self.next = next

def returnKthToLast(head, k):
	p1 = head
	p2 = head
	# put p1 kth ahead of p2 in the linked list
	for i in range(k):
		if p1 is not None:
			p1 = p1.next 

	# move both p1 and p2 until p1 hit None
	while p1 is not None:
		p1 = p1.next
		p2 = p2.next
	print(p2.value)

# main
n = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,None))))))


returnKthToLast(n, 6)
