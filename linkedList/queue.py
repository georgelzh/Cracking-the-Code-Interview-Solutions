# FIFO 
# like restraunt line, first in first out.
# reference https://realpython.com/linked-lists-python/

from collections import deque

queue = deque()

# add new ppl in the line
queue.append("bob")	#first
queue.append("Mary")
queue.append("George")
queue.append("Susan")
queue.append("Alan") # last
print(queue)

queue.popleft()	# bob is out because he is the first one in
print("popleft: ", queue)

