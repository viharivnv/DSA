#The code was run on PYCHARM IDE on WINDOWS python version 3.x
'''
Steps to recreate:
1)Open PYCHARM
2)Create a new project
3) Add a new python file and paste the code
4) Run the code
'''

file=open("Dataset.txt", "w")
data=[]
for i in range(0,1024):
    data.append(1)
for j in range(1024, 3072):
    data.append(11)
for c in range(3072, 7168):
    data.append(111)
for d in range( 7168, 8192):
    data.append(1111)


for i in data:
    file.write(str(data[i]) + '\n')

file.close()


c=0
for i in range(0, 8192):
    for j in range(0,8191):
        if data[j]>data[j+1]:
            c+=1

    if c == 0:
        print('Data is already sorted')
        break

