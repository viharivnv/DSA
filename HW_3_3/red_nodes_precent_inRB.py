#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

import random

#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm


# declaration of class Node
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.color = 1  # 1 means red else black


red_counts = 0
counts = 0
RED = True
BLACK = False


# checks if the node passed is red
def is_red(roots):
    if roots is not None:
        if roots.color == 1:
            return 1
        else:
            return 0
    else:
        return 0

# Rotates the entire tree to left
def rotate_left(h):
    x = h.right
    h.right = x.left
    x.left = h
    x.color = h.color
    h.color = 1

    return x

# Rotates the entire tree to right
def rotate_right(h):
    x = h.left
    h.left = x.right
    x.right = h
    x.color = h.color
    h.color = 1

    return x


# flips the red and black nodes
def flip(h):
    h.color = 1
    h.left.color = 0
    h.right.color = 0

# Inserts the node into the tree
def insert(self, value):
    if self is None:
        return Node(value)
    elif self.value > value:
        self.left = insert(self.left,value)
    elif self.value < value:
        self.right = insert(self.right, value)
    elif self.value == value:
        self.value = value

    if (is_red(self.left) == 0 and is_red(self.right) == 1):
        self = rotate_left(self)
    if (is_red(self.left) == 1 and is_red(self.left.left) == 1):
        self = rotate_right(self)
    if (is_red(self.left) == 1 and is_red(self.right) == 1):
        flip(self)

    return self

# gives the count of nodes in the tree
def count(self):
    global counts

    if self is not None:
        count(self.left)
        counts += 1
        count(self.right)

    return counts


# gives the count of red nodes in the tree
def red_count(self):
    global red_counts

    if self is not None:
        red_count(self.left)
        if self.color == 1:
            red_counts += 1
        red_count(self.right)

    return red_counts


def main():
    size = 10000

    while size < 2000000:
        n = 100
        c = 0
        c1 = 0
        c2=0
        # generation of N nodes and calculating the percentage of red nodes created
        for i in range(0, 100):

            arr = []
            for l in range(1, size + 1):
                arr.append(l)
            random.shuffle(arr)
            root = None
            # N random insertions
            for x in range(0, len(arr)):
                root = insert(root, arr[x])

            c += red_count(root)
            c1 += count(root)
            # Ratio of red nodes to total number of nodes
            c2 = c / c1

        print('Percent of red nodes present for N=', size, ':', c2*100, '%')
        size *= 10


if __name__ == "__main__":
    main()