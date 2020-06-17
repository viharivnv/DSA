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
        if self.data:
            self.N=1
        else:
            self.N=0

#finds the minimum node in the tree
    def minnode(self):
        current=self
        while(self.left is not None):
            current = current.left
        return current

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

    def insert(self, key):

        if self.data:
            #if there is already a node present
            #compare if the new value is smaller than the root
            if key < self.data:
                self.N+=1
                #data is smaller than the data present
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key>self.data:
                self.N += 1
                #executes if greater than the root

                if self.right is None:
                    # if there is no right child to the node
                    self.right = Node(key)

                else:
                    # if there is a right child
                    self.right.insert(key)


        else:
            self.data = key
            self.N+=1

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


    def size(self):
        if self.data is not None:
            return self.N
        else:
            return 0

    def search(self,key):
        if self.data:
            if self.data == key:
                print('found')
            elif self.data < key:
                if self.left:
                    self.left.search(key)
            else:
                if self.right:
                    self.right.search(key)

#stores the keys/values into the list passed using inorder traversal
def inorder(self,q):
    if not self:
        return -1
    inorder(self.left,q)
    q.append(self.data)
    inorder(self.right, q)


# returns the index of the value present
def rank(self, key):
    q = []
    inorder(self,q)
    return q.index(key)


# returns the value present in the tree with rank as the index
def select(self, rank):
      q = []
      inorder(self, q)
      return q[rank]






def main():

    f = open("select-data.txt", "r")
    nums=[]
    # stores the data in nums
    for line in f.readlines():
        nums.append(int(line))

    nums1 = [int(i) for i in nums]

    root=Node()
    for i in nums:
        root.insert(i)

    print('rank(7) is',rank(root,7))
    print('select(7) is',select(root,7))
if __name__ == "__main__":
    main()