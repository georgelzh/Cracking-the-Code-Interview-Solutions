"""
use of linked List

"""

from collections import deque

llist = deque([1,2,3,4])
print(llist)

llist.append(5)
print(llist)

llist.appendleft(0)
print(llist)

llist.pop()
print(llist)

llist.popleft()
print(llist)

