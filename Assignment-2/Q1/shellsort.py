#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''
import time
def insertion(arr):
    c= 0
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        j=i

        while j>=1 and arr[j-1]>temp:
            c+=1
            arr[j]=arr[j-1]
            j-=1
        c+=1

        arr[j]=temp

    return c

def shellsort(arr, k):
    c=0
    n=len(arr)
    for i in range(k, n):
        temp = arr[i]
        j = i

        while j >=k and arr[j - k] > temp:
            c += 1
            arr[j] = arr[j - k]
            j -= k
        c += 1

        arr[j] = temp

    return c
text=input("enter the file name excluding '.txt' extension for example data0.1024:\n")
text=text+".txt"

try:
    # opens the file with the entered filename
    f = open(text, "r")
    # stores the data in nums
    nums = f.readlines()
    nums1 = [int(i) for i in nums]
    nums2 = [int(i) for i in nums]
    n = len(nums1)

except:
    print('No such file exists!!!')


comp=0
comp1 = 0
start=time.time_ns()
comp+=shellsort(nums1, 7)
comp+=shellsort(nums1,3)
comp1+=shellsort(nums1,1)
stop=time.time_ns()
com=0
comp2=0
start1=time.time_ns()
com+=shellsort(nums2, 7)
com+=shellsort(nums2,3)
comp2+=insertion(nums2)
stop1=time.time_ns()
print(comp+comp1,comp1)
print(com+comp2,comp2)
print('Time taken when shell sorted all the way',stop-start)
print('Time taken when reverted to insertion',stop1-start1)






