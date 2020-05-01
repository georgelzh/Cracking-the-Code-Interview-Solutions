# hash set implementation in python
# Author Zhihong Li
# Date: April 30, 2020


class MyHashSet():
    def __init__(self):
        self.maxSize = 100000 # depends on how big the number range is
        self.arr = [None for i in range(self.maxSize)]

    def add(self, key:int) -> None:
        index = key % self.maxSize
        self.arr[index] = key

    def contains(self, key:int) -> bool:
    	index = key % self.maxSize
    	if self.arr[index] == None:
    		return False
    	elif self.arr[index] != None:
    		return True

    def remove(self, key:int) -> None:
        index = key % self.maxSize
        if self.arr[index] != None:
            deleted_value = self.arr[index]
            self.arr[index] = None
            return deleted_value