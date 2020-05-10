# https://www.tutorialspoint.com/python_data_structure/python_heaps.htm
# heap in python

import heapq

# creating a heap

# make a list that you want to use as a heap
H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)    # [1, 3, 5, 78, 21, 45]


# insert into a heap
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,8)
print(H)       # [1, 3, 5, 78, 21, 45, 8]


heapq.heappush(H,6)
# heapq.heapify(H)
print(H)


"""
Removing from heap
This algorithm will also take 0( log(base 2)n) time.

You can remove the element at first index by using this function.
In the below example the function will always remove the element
at the index position 0.
"""
print("remove from heap")
H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
heapq.heappop(H)

print(H)


"""
Replacing in a Heap
This algorithm will also take 0( log(base 2)n) time.

The heapreplace function always removes the smallest element
of the heap and inserts the new incoming element at some
place not fixed by any order.
"""
H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
heapq.heapreplace(H,6)
print(H)
