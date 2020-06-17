#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

text=input("enter the file name excluding '.txt' extension for example 8int:\n")
text=text+".txt"
try:
    # opens the file with the entered filename
    f = open(text, "r")
    # stores the data in nums
    nums = f.readlines()
    nums1 = [int(i) for i in nums]
    # setting counter to 0
    count = 0
    # sorts the array
    nums1.sort()
    s = len(nums1)

    c2 = 0
    # prompts the user to enter a sum for the triplet
    sum = int(input("Enter the sum:"))


    # code for binary search
    def b_s(arr, key):

        l = 0
        global c2
        u = len(arr)
        while l < u:
            c2 += 1
            x = (l + u) / 2
            m = int(x)
            if arr[m] == key:
                return 1
            elif arr[m] > key:
                u = m;
            elif arr[m] < key:
                if l == m:
                    break
                l = m;
        pass


    for x in range(0, s - 1):
        for y in range(x + 1, s):
            # condition to eliminate duplicate values
            if nums1[x] != nums1[x - 1] and nums1[y] != nums1[y - 1]:
                z = sum - nums1[x] - nums1[y]
                # Calls binary search for z on nums1
                if b_s(nums1, z):
                    if z > nums1[x] and z > nums1[y]:
                        count += 1

    print("Total Number of numbers having the three-sum :", sum, " is ", int(count))

    print("Total number of Instructions/statements run : ", c2)

except:
    print('File not found!!!')
