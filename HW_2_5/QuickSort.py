#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

# Referred for error caused due to recursion "https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object"
#Referred "https://www.geeksforgeeks.org/quick-sort/" for partition algorithm
import sys
sys.setrecursionlimit(99999)

import time

def median(arr,l,r):
    #returns median of l,r,m m is midpoint
    m=(l+r-1)//2
    m=int(m)
    if arr[l]<arr[m]:
        if arr[m]<arr[r-1]:
            return m
        elif arr[l]<arr[r-1]:
            return r-1
        else:
            return l

    else:
        if arr[l]<arr[r-1]:
            return l
        elif arr[m]<arr[r-1]:
            return r-1
        else:
            return m

def swap(arr, i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
c=0

def partition(arr, l, r):

    pivot=arr[l]
    i = l + 1
    for j in range(l + 1, r):
        if arr[j] < pivot:
            swap(arr,i,j)
            i += 1
    swap(arr,l,i-1)

    return i - 1




def quicksort(arr, l, r):
    if l<r:
        p_i = median(arr, l, r)
        swap(arr,l,p_i)         #swaps the pivot with the first element
        p=partition(arr,l,r)
        quicksort(arr,l,p)
        quicksort(arr,p+1,r)


def quick_ins_cutoff(arr,l,r, cutoff=7):
    if l<r:

        if r<= l+cutoff-1:
            #Makes Insertion sort and returns when the above condition is true
            for i in range (l,r):
                temp=arr[l]
                j=i
                while j>1 and arr[j-1]>temp:
                    arr[j]=arr[j-1]
                    j-=1
                arr[j]=temp
            return

        p_i = median(arr, l, r) #calls median function
        swap(arr,l,p_i)        #swaps the pivot with the first element
        p = partition(arr, l, r)
        quicksort(arr, l, p)
        quicksort(arr, p + 1, r)



text=input("enter the file name excluding '.txt' extension for example data1.1024:\n")
text=text+".txt"

try:
    # opens the file with the entered filename
    f = open(text, "r")
    # stores the data in nums
    nums = f.readlines()
    nums1 = [int(i) for i in nums]
    n = len(nums1)

except:
    print('No such file exists!!!')


start=time.time_ns()
quick_ins_cutoff(nums1,0,len(nums1))
#quicksort(nums1,0,len(nums1))
stop=time.time_ns()

print('Run time is',stop-start,'ns')




