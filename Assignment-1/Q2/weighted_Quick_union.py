#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''
import time
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
    sz = []
    # referred "https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python" for getting time in milliseconds
    start = time.time_ns()
    # initialization of the array
    for i in range(0, 8192):
        id.append(i)
        sz.append(1)
    c = 0


    # defining union function
    def un(o, l):
        i = root(o)
        j = root(l)
        if sz[i] < sz[j]:
            id[i] = j
            sz[j] += sz[i]
        else:
            id[j] = i
            sz[i] += sz[j]


    # defining find function
    def root(i):
        global c1
        while i != id[i]:
            i = id[i]
        return i


    count = 0

    # Weighted Quick-Union Algorithm
    for i in range(0, len(p)):
        f = a[i]
        g = b[i]
        if root(a[i]) == root(b[i]):
            continue

        else:
            c += 1
            un(f, g)
        print('The pairs are :', a[i], b[i],'with root',root(f))

    stop = time.time_ns()
    runtime = stop - start

    print("The Number of instructions executed", c)
    print('time taken to execute', runtime, 'ns')

except:
    print('File Not Found')