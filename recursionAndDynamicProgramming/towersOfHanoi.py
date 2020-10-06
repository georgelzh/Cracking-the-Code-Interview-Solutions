"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following
constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk.
Write a program to move the disks from the first tower to the last using stacks.
Hints: #144, #224, #250, #272, #318

"""
class Tower:
    def __init__(self, index):
        self.index = index
        self.disks = []

    def add(self, d):
        print(d)
        if self.disks and self.disks[len(self.disks) - 1] <= d:
            print("error")
        else:
            self.disks.append(d)

    def moveTopTo(self, dest):
        top = self.disks.pop()
        dest.add(top)

    def moveDisks(self, n, dest, buffer):
        if n > 0:
            self.moveDisks(n - 1, buffer, dest)
            self.moveTopTo(dest)
            buffer.moveDisks(n - 1, dest, self)
            # move n - 1 from buffer to dest. destination to buffer. 
            # bc line 31 here we are using dest as buffer, and we

def towersOfHanoi(n):
    towers = []
    for i in range(n):
        towers.append(Tower(i))
    
    for i in range(n, 0, -1):
        towers[0].add(i)
    
    towers[0].moveDisks(n, towers[2], towers[1])
    return towers[2]
    
a = towersOfHanoi(10)
print(a.disks)