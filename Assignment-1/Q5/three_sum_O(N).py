#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

print("Only one test data was added 8int.txt")
text=input("enter the file name excluding '.txt' extension as 8int:\n")
text=text+".txt"
try:
    f = open(text, "r")
    nums = f.readlines()
    nums = [int(i) for i in nums]
    s = len(nums)
    nums.sort()
    sum = int(input("Enter the sum value"))


    # function to check if a pair of numbers sum up to '0'
    def linear_pairs(arr):
        l = 0
        r = len(arr) - 1
        c = 0
        while l < r:
            if arr[l] + arr[r] == 0:
                c += 1
                l += 1
            elif arr[l] + arr[r] < 0:
                l = l + 1
            else:
                r = r - 1
        return c


    count = 0
    # Counting the number of triplets, that sum up to a given value
    for i in range(0, len(nums)):
        if nums[i] == sum:
            count += linear_pairs(nums)

    print('The number of triplets with sum', sum, 'is', count)

except:
    print('File not found!!!')
