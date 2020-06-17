#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

#https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

#declaration of class Node
class Node:

    #Initialize a node when a node is created with given data
    def __init__(self, data=None):

        self.left = None
        self.right = None
        self.data = data
        self.r_data=None
        self.down = None

    #retunrs the node with minimum value
    def minnode(self):
        current=self
        while(self.left is not None):
            current = current.left
        return current

    #deletes the node with data as the value
    def delete(self,data):
        if self is None:
            #if no node is present
            print("empty tree. Unable to Delete!!!")
        else:
            #if atleast one node is present
            if data<self.data:
                #if the data to be deleted is less than the root value
                self.left.delete(data) #calls deletion in left subtree
            elif data>self.data:
                #executes if the value is greater than the left value of the node

                if self.r_data is None:
                    #if the node has only one value
                    self.right.delete(data)

                elif self.r_data is not None:
                    #if the node has two values
                    if self.r_data==data:
                        #if the right value is the value to be deleted

                        if self.down:
                            #if the down subtree exists
                            temp = self.down.minnode()
                            self.r_data = temp.data
                            self.down.delete(temp.data)
                        else:
                            #if there is no down subtree
                            self.r_data=None

                    elif self.r_data<data:
                        #if The value to be deleted is greater than the value of the node
                        self.right.delete(data)
                    else:
                        #if the value to be deleted is between the left and right values of the node
                        self.down.delete(data)

            else:
                if self.down is None:
                    #If there is no centre down subtree
                    if self.left is None and self.right is None:
                        #If the node is leaf node
                        if self.r_data:
                            self.data = self.r_data
                            self.r_data = None
                        else:
                            self.data = None

                    elif self.left is None:
                        #if it has right subtree
                        if self.r_data:
                            self.data = self.r_data
                            self.r_data = None
                        else:
                            self.data = self.right.data
                            self.right.data = None
                    elif self.right is None:
                        #if it has left subtree
                        if self.r_data:
                           self.data = self.r_data
                           self.r_data = None

                        else:
                           self.data = self.left.data
                           self.left.data = None

                    else:
                        #if it has both the subtrees (left and right)
                        temp = self.right.minnode()
                        self = temp
                        self.right.delete()

                elif self.down:
                    #if the node has down subtree
                    temp = self.down.minnode()
                    self.data = temp.data
                    self.down.delete(temp.data)

    def insert(self, key):

        if self.data:
            #if there is already a node present
            #compare if the new value is smaller than the root
            if key < self.data:
                #data is smaller than the data present
                if self.r_data is None:
                    self.r_data = self.data
                    self.data = key
                elif self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)

            elif key > self.data:
                #executes if greater than the root

                    if self.r_data is None:
                        #adds a second value to the node
                        self.r_data = key

                    elif self.r_data < key:
                        #if the entered key is greater than the right value of the node
                        if self.right is None:
                            #if there is no right child to the node
                            self.right = Node(key)
                        else:
                            #if there is a right child
                            self.right.insert(key)
                    else:
                        #creates a node if the tree is empty
                        if self.down is None:
                            self.down = Node(key)
                        else:
                            self.down.insert(key)


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

        #checks if the node has a second data in it
        if self.r_data:

            if self.down:
                #traverse through the center node if present
                self.down.PrintTree()
            #print the second data of the node if present
            print('right node:')
            print(self.r_data)


        if self.right:
            #traverse through right sub tree
            self.right.PrintTree()


    def search(self,key):
        if self.left is None and self.right is None:
            #if Leaf node
            if key == self.data or key==self.r_data:
                print("key found!!!")
                return
            else:
                print("Key Not Found!!!")
        else:
            #if the node is not a leaf node
            if key == self.data:
                print("key found!!!")
                return
            elif key < self.data:
                #if the key is less than the node value
                self.left.search(key)
            elif key >= self.data:
                if self.r_data:
                    #if the node has two keys
                    if self.r_data == key:
                        print("key found!!!")
                        return
                    elif self.r_data > key:
                        #if the key is in centre subtree
                        self.down.search(key)
                    else:
                        self.right.search(key)
                else:
                    self.right.search(key)




def main():
    """
    text=input("Enter The file name excluding the .txt extension")
    text=text+'.txt'
    f=open(text,"r")
    nums = f.readlines()
    nums1 = [int(i) for i in nums]
    root= Node()
    for x in nums1:
       root.insert(x)
    """

    """
    text=input("Enter The file name excluding the .txt extension")
    text=text+'.txt'
    f=open(text,"r")
    nums = f.readlines()
    nums1 = [int(i) for i in nums]
    root= Node()
    for x in nums1:
       root.insert(x)

    root.PrintTree()
    t = 1
    while t:
        d=int(input('Enter the element to be deleted'))
        root.delete(d)
        print("After Deletion")
        root.PrintTree()
        t = int(input('Enter 1 to delete another key/value or 0 to exit'))
    """




    """
    # Adding nodes
    root = Node()
    t = 1
    while t:
        add=int(input('Enter the element to be added'))
        root.insert(add)
        root.PrintTree()
        t = int(input('Enter 1 to add another key/value or 0 to exit'))


    s=int(input('Enter an element to be searched:'))
    root.search(s)
    a=1
    while a:
        d = int(input('Enter the element to be deleted'))
        root.delete(d)
        print("After Deletion")
        root.PrintTree()
        a = int(input('Enter 1 to Delete another key/value or 0 to exit'))
        
    """
    # Adding nodes
    root = Node(5)
    root.insert(9)
    root.insert(6)
    root.insert(4)
    root.insert(2)
    root.insert(10)
    root.insert(16)
    root.insert(15)
    root.insert(17)
    root.insert(20)
    root.insert(25)
    root.PrintTree()
    root.search(15)
    print("After Deletion")
    root.delete(5)

    root.PrintTree()

if __name__ == "__main__":
    main()