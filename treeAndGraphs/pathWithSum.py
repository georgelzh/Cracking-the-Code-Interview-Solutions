"""
4.12
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
Hints:#6, #14, #52, #68, #77, #87, #94, #103, #108, #115


BFS + DFS
1. visit start node, and then add all children nodes to a queue
2. check if current path is the given number if yes, add 1 to the path num
        else continue traverse from start node to each children and repeat
        process of 1, 2. 
        (During the process, 
            a. keep track of the current value
            b. need to pass the number of path back when it's finished
                (is it better to traverse or use recursion?)
        )

"""
