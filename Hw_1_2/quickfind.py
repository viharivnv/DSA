
#The code was run on PYCHARM IDE on WINDOWS python version 3.x

import time
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

file=input("enter the file name excluding '.txt' extension for example 8pair:\n")
file=file+".txt"
# referred "https://stackoverflow.com/questions/47872237/how-to-read-an-input-file-of-integers-separated-by-a-space-using-readlines-in-py/47872327" for splitting
try:
        # stores each line in the file as a string in the array of strings text
        with open(file, 'r') as f:
                text = f.read()
        text = text.split("\n")
        i = 0
        arr = []
        a = []
        b = []
        p = []
        q = []
        count = 0
        # Stores the two strings sepersted by whitespace as seperate elements of the array
        for i in range(0, len(text) - 1):
                left = text[i].split()
                for x in left:
                        arr.append(x)
        # stores the numbers read to p and q
        for i in range(0, len(arr)):
                if i % 2 == 0:
                        p.append(arr[i])
                else:
                        q.append(arr[i])
        for x in p:
                t = int(x)
                a.append(t)
        for y in q:
                t = int(y)
                b.append(t)
        id = []
        # referred "https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python" for getting time in milliseconds
        start = time.time_ns()
        # initialization of the array
        for i in range(0, 8192):
                id.append(i)
        c = 0
        # quick-find algorithm
        for i in range(0, len(p)):
                if id[a[i]] == id[b[i]]:

                        continue
                else:
                        count += 1
                        for z in range(0, len(id)):

                                if id[z] == id[a[i]]:
                                        id[z] = id[b[i]]
                print('The pairs are :', a[i], b[i],'with root',id[b[i]])

        stop = time.time_ns()
        runtime = stop - start
        print("The number of instructions executed: ")
        print(count)
        print('time taken to execute', runtime, 'ns')

except:
        print('File Not Found!!!')
