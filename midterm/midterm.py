


import csv


import numpy as np




def main():
    arr = ["AAPL", "AMZN", "FB", "GOOGL", "NFLX", "TRIP", "TSLA", "TWTR", "VAC", "YELP"]



    # order
    M = 3


    w_i = np.random.rand(M, 1)
    mean_abs_err = 0
    tp=tn=fp=fn=0

    for stock in arr:

        stock=stock+'.csv'
        print('\nFor stock:',stock)
        x_train, t_train = [i for i in range(1, M + 1)], []

        t_test = []
        row_count = 1

        with open(stock, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            # next(readFile)
            for row in reader:

                if row_count <= M:
                    t_train.append(float(row['4. close']))
                elif row_count <= 2 * M:
                    t_test.append(float(row['4. close']))

                row_count += 1

        y_i = 0
        for set_no in range(len(t_train)):
            y_i += w_i[set_no] * pow(x_train[set_no], set_no)
        abs_err = abs(t_train[len(t_train) - 1] - y_i)
        for i in range(len(w_i)):
            dw = (- 0.12999 / M) * (t_train[len(t_train) - 1] - y_i) * pow(M + 1, i)
            w_i[i] = w_i[i] - (0.14999 * dw)


        y_t = 0

        for set_no in range(len(t_test)):
            y_t += w_i[set_no] * pow(x_train[set_no], set_no)

        abs_err = abs(t_test[len(t_test) - 1] - y_t)

        print('predicted:',y_t[0])

        a = t_test[len(t_test) - 2]
        b = t_test[len(t_test) - 1]

        if a > y_t[0] and a > b:
            print('Hold it')
            print('tn')
            tn += 1
        if a > y_t[0] and a <= b:
            print('Hold it')
            print('fn')
            fn += 1
        if a < y_t[0] and a < b:
            print('Can Buy')
            print('tp')
            tp += 1
        if a < y_t[0] and a >= b:
            print('Can Buy')
            print('fp')
            fp += 1

        print('Actual:', t_test[len(t_test) - 1])
        print('error of prediction', abs_err[0])
        mean_abs_err += abs_err

    print('\ntp:',tp, 'tn:', tn,'fn:', fn,'fp:', fp)
    tp_rate = tn_rate = 0
    tp_rate = tp / (tp + fn)
    if tn!=0:
        tn_rate = tn / (tn + fp)
    accuracy = (tp + tn) / (tp + tn + fn + fp)
    precision = tp / (tp + fp)
    print('\nThe mean error of predictions is',mean_abs_err[0]/10)
    print('\nAccuracy: ', accuracy, '\nTrue Positive Rate:', tp_rate, '\nTrue Negative Rate:', tn_rate, '\nPrecision:',precision)
# print(rel_avg_err)



if __name__ == "__main__":
    main()