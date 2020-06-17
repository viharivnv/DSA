#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

text=input("enter the file name excluding .txt as Farthest_pair_data (OR you can create another txt file) (OR Use the code in the comments to enter data manually):\n")
text=text+".txt"
try:
    f = open(text, "r")
    nums = f.readlines()

    nums = [int(i) for i in nums]

    # init
    '''
    n=int(input("enter size"))
    nums=[]
    for i in range(0,n-1):
        y=int(input())
        nums.append(y)

    '''
    # Required Algorithm
    mini = nums[0]
    maxi = nums[0]
    # finds minimum and maximum value of the array
    for x in nums:
        if (x > maxi):
            maxi = x;
        if (x < mini):
            mini = x;
    print('The farthest pair is', maxi, ',', mini, 'has a distance of ', abs(maxi - mini))

except:
    print('File Not Found!!!')