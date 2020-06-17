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
    swaps=0
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

    while i<n and j<m:
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i+=1
            k+=1

        else:
            swaps += 1
            arr[k]=r_arr[j]
            j+=1
            k += 1




    while i < n:
        arr[k]=l_arr[i]
        i+=1
        k+=1

    while j < m:
        arr[k]=r_arr[j]
        j+=1
        k+=1
    return swaps

def sort(arr, l, r):
    swap=0
    if l<r:
        m = (r + l) // 2
        swap += sort(arr,l,m)
        swap += sort(arr,m+1,r)
        swap += merge(arr,l,m,r)

    return swap


text=input("enter the file name excluding .txt for example as data0.1024:\n")
text=text+'.txt'
try:
    # opens the file with the entered filename
    f = open(text, "r")
    # stores the data in nums
    nums = f.readlines()
except:
    print('No such file exists!!!')
nums1 = [int(i) for i in nums]
n = len(nums1)
start=time.time_ns()
c=sort(nums1,0,n-1)
stop=time.time_ns()
print ('The number of Inversion pairs is:',c)
print ('The run time is:',stop-start)






