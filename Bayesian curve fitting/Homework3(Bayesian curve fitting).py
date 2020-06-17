# Implementation of Bayesian Curve fitting from Bishop page 31


import csv
import numpy as np


def predict_val(x,t):
    rel_err = 0
    abs_err = 0
    l=len(x)
    N = 5
    alpha = 0.647
    beta = 12
    arr1=np.zeros( (N+1,N+1))
    arr2=np.zeros( (N+1,N+1))
    s=np.zeros((N+1,N+1))
    lt=np.zeros((N+1,1))


    for i in range(0,l-2):
        for j in range(0,N+1):
            temp=float(pow(x[i],j))
            arr1[j][0]+=temp

    for i in range(0,N+1):
        temp1=float(pow(x[l-2],i))
        arr2[0][i]=temp1

    smat=np.dot(arr1,arr2)
    smat *= beta
    #smat=[float(x) for x in smat]

    s=smat
    for i in range(0,N+1):
        for j in range(0,N+1):
            if i==j:
                s[i][j]+=alpha

    smat=np.linalg.inv(smat)
    '''
    for row in smat:
        print([x for x in row])
        '''
    for i in range(0,l-2):
        for j in range(0,N+1):
            lt[j][0]+=pow(x[i],j)*t[i]

    arr3=arr2.dot(smat)
    prediction=np.dot(arr3,lt)
    prediction*=beta

    print("Actual Price is",t[l - 1], "Predicted Price is",prediction[0][0])
    abs_err=abs(t[l-1]-prediction[0][0])
    rel_err=abs_err/t[l-1]
    print("Absolute error is:",abs_err,"and Relative error is",rel_err)
    return  abs_err,rel_err



def main():

    arr = ["AAPL", "AMZN", "FB", "GOOGL", "MA", "NFLX", "TRIP", "TSLA", "TWTR", "VAC","AAPLtest", "AMZNtst", "FBtst", "GOOGLtest", "MAtst", "NFLXtst", "TRIPtst", "TSLAtst", "TWTRtst", "VACtst", "MSFT"]
    rel_err=0
    abs_err=0
    for text in arr:
        print("For the Company ID:",text)
        xarr1 = []
        tarr1 = []
        text = text + '.csv'
        with open(text, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                xarr1.append(row['x'])
                tarr1.append(row['target'])

        xarr = [float(i) for i in xarr1]
        tarr = [float(i) for i in tarr1]
        abs, rel =predict_val(xarr,tarr)
        abs_err+=abs
        rel_err+=rel
    print('For total Estimation:')
    print("Absolute error is:", abs_err/21, "and Relative error is", rel_err/21)

if __name__ == "__main__":
    main()