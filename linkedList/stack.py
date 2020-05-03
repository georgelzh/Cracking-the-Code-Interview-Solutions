# LIFO First In, Last out
# like the plates in dhall, last in, first out. 
#its on the bottom of the stack
# reference https://realpython.com/linked-lists-python/
# https://dbader.org/blog/python-linked-list

from collections import deque

queue = deque()

# appendleft new ppl in the line
queue.appendleft(1)	# first
queue.appendleft(2)
queue.appendleft(3)
queue.appendleft(4)
queue.appendleft(5) # last
print(queue)

# popleft
queue.popleft()	# 5 is the last, so its first out
print("popleft: ", queue)

# takes O(n) times to remove
del queue[2] # remove at index
queue.remove(3) # remove by value
print(queue)

# you can reverse it, takes O(n) and extra space
queue.reverse()
print(queue)

# return index of a value O(n) times
index = queue.index(4)
print(index)

# for item in queue:
# 	print(item)

# for i in range(len(queue)):
# 	print(queue)
