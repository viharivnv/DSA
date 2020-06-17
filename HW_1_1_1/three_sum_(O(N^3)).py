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
    s = len(nums1)
    nums2 = nums1
    nums2.sort()
    count = 0
    # setting counters to 0
    c = 0
    # prompts the user to enter a sum for the triplet
    sum = int(input("Enter the sum:"))
    # execute three for loops to get the three values
    for x in range(0, s - 2):
        for y in range(x + 1, s - 1):
            for z in range(y + 1, s):
                # increments the counter for each iteration
                c += 1
                # condition to eliminate duplicate values
                if nums2[y] != nums2[y - 1] and nums2[z] != nums2[z - 1] and nums2[x] != nums2[x - 1]:

                    if nums1[x] + nums1[y] + nums1[z] == sum:
                        # increments if the triplet sum up to the entered value
                        count += 1

    print("Total Number of numbers having the three-sum :", sum, " is ", int(count))
    print("Total number of Instructions/statements run : ", c)

except :
    print('File not found!!!')
