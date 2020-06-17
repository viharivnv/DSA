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
class Node:

    def __init__(self, data=None):

        self.left = None
        self.right = None
        self.data = data

#finds the minimum node in the tree
    def minnode(self):
        current=self
        while(self.left is not None):
            current = current.left
        return current

#delete function
    def delete(self,data):
        if self is None:
            #if tree is empty
            print("empty tree. Unable to Delete!!!")
        else:
            #if tree is not empty
            if data<self.data:
                self.left.delete(data)
            elif data>self.data:
                self.right.delete(data)

            else:
                if self.left is None and self.right is None:
                    #if it is the only node
                   self.data=None
                elif self.left is None:
                    #if there is no left subtree
                    self.data=self.right.data
                    self.right.data=None
                elif self.right is None:
                    #if there is no right subtree
                    self.data = self.left.data
                    self.left.data = None

                else:
                    #if the tree has both the subtrees
                    temp=self.right.minnode()
                    self=temp
                    self.right.delete()

#Insert function
    def insert(self, key):

        if self.data:
            #if there is already a node present
            #compare if the new value is smaller than the root
            if key < self.data:
                #data is smaller than the data present
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key>self.data:
                #executes if greater than the root

                    if self.right is None:
                           #if there is no right child to the node
                        self.right = Node(key)
                    else:
                         #if there is a right child
                         self.right.insert(key)


        else:
            self.data = key

# Print the tree using Inorder Traversal
    def PrintTree(self):
        if self.left:
            #traverse through left subtree
            self.left.PrintTree()

        #prints the data of the node if present
        if self.data:
            print('node:')
            print( self.data)




        if self.right:
            #traverse through right sub tree
            self.right.PrintTree()



#returns the total internal path of the tree
    def internalpath(self, depth=0):

        d1=d2=depth
        if self.left and self.right is None:
            #if there is a single node
            return 0
        else:
            #if there is atleast one node
            if self.left:
                #if there is a left subtree
               depth = self.left.internalpath(d1+1)
            if self.right:
                #if a right subtree exists
                depth += self.right.internalpath(d2+1)

            return depth


def main():
   # size=int(input("Enter the number of nodes(Less than 1000 to avoid 'RecursionError: maximum recursion depth exceeded' error):"))
    size=10
    while size<1000:
        sorted_mean = 0
        shuffled_mean = 0
        n = 100
        for i in range(0, n):
            arr = []
            arr2 = []
            for l in range(1, size + 1):
                arr.append(l)

            root1 = Node()

            for x in arr:
                root1.insert(x)

            c = root1.internalpath(0)

            sorted_mean += c / size

            arr2 = arr
            random.shuffle(arr)
            root2 = Node()
            for y in arr:
                root2.insert(y)

            c1 = root2.internalpath(0)
            shuffled_mean += c1 / size
        print("The average path length for N=",size,'nodes, for Shuffled insertion is',shuffled_mean / 100,'and for sorted insertion is',sorted_mean / 100)
        size+=100


if __name__ == "__main__":
    main()