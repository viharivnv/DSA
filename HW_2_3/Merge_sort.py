#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''
import time
def merge(arr,left,mid,right):
    comp=0
    l_arr=[]
    r_arr=[]
    n = mid-left+1
    m = right-mid
    for i in range(0,n):
        l_arr.append(arr[left+i])
    for j in range(0,m):
        r_arr.append(arr[mid+1+j])

    i=j=0
    k=left

#sorts the array while merging
    while i<n and j<m:
        if l_arr[i] <= r_arr[j]:
            comp += 1
            arr[k] = l_arr[i]
            i+=1
            k+=1

        else:
            comp += 1
            arr[k]=r_arr[j]
            j+=1
            k += 1



# adds the elements which are missed while merging
    while i < n:
        arr[k]=l_arr[i]
        i+=1
        k+=1

    while j < m:
        arr[k]=r_arr[j]
        j+=1
        k+=1
    return comp

def recursive_merge(arr, l, r):
    count=0
    if l<r:
        m = (r + l) // 2
        count += recursive_merge(arr,l,m)
        count += recursive_merge(arr,m+1,r)
        count += merge(arr,l,m,r)

    return count

def iterative_merge(arr):
    counts=0
    iter=1
    while iter<=len(arr)-1:
        l=0
        while l<=len(arr)-1:
            m = l + iter-1
            if len(arr)-1 > (2*iter + l -1):
                r = 2*iter +l-1
            else:
                r=len(arr)-1
            counts += merge(arr, l, m, r)
            l += 2*iter

        iter *=2

    return counts

text=input("enter the file name excluding .txt for example data0.1024:\n")
text=text+'.txt'
try:
    # opens the file with the entered filename
    f = open(text, "r")
    # stores the data in nums
    nums = f.readlines()
    nums1 = [int(i) for i in nums]
    nums2 = [int(i) for i in nums]
    n = len(nums1)
    start = time.time_ns()
    c = recursive_merge(nums1, 0, n - 1)
    stop = time.time_ns()
    istart = time.time_ns()
    c1 = iterative_merge(nums2)
    istop = time.time_ns()
    print('Recursive')
    print('The number of Comparisons made is:', c)
    print('The run time is:', stop - start)
    print('Iterative')
    print('The number of Comparisons made is:', c1)
    print('The run time is:', istop - istart)
except:
    print('No such file exists!!!')





