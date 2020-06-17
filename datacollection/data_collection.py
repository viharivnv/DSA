import requests
import pandas as pd
import mysql.connector
from datetime import date
import datetime
from alpha_vantage.timeseries import TimeSeries
import schedule
import time

API_URL = "https://www.alphavantage.co/query"
# list of 10 stocks
stocks = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'NFLX', 'TSLA', 'TWTR', 'YELP', 'VAC', 'TRIP']

# connect to mysql database
mydb = mysql.connector.connect(
    host="localhost",
    user="Admin",
    passwd="Password1$"
)

mycursor = mydb.cursor()
mycursor.execute("USE stocks")


# get historical stock data
def get_hist():
    i = 1
    for symbol in stocks:
        sid = []
        if i % 3 != 0:
            data = {"function": "TIME_SERIES_DAILY",
                    "symbol": symbol,
                    "outputsize": "compact",
                    "datatype": "json",
                    "apikey": "B8FD7DBR7ZE592RP"}

            response = requests.get(API_URL, data)
            response_json = response.json()

            data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient='index').sort_index(axis=1)
            data = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close',
                                        '5. volume': 'Volume'})
            # parse response to get required fields
            open = data.iloc[1, :]['Open']
            close = data.iloc[1, :]['Close']
            low = data.iloc[1, :]['Low']
            high = data.iloc[1, :]['High']
            vol = data.iloc[1, :]['Volume']
            curr_day = date.today()
            dat = datetime.date.strftime(curr_day, "%y-%m-%d")  # convert to yyyy-mm-dd format
            #dat = "2020-03-27"
            # retrieve sid for this specific stock
            mycursor.execute("SELECT sid from stock_symbs where stock_symb='" + symbol + "'")
            result = mycursor.fetchall()
            sid = result[0][0]
            # insert into historical data table
            sql = "INSERT INTO hist_stocks (sid,dat,open_value,high,low,close_value) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (sid, dat, open, high, low, close)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted for", symbol)
        else:
            print("sleeping")
            time.sleep(60)
            i += 1


# get real-time stock data
def get_real():
    count = 0
    mycursor.execute("delete from realtime_stocks;")
    for symbol in stocks:
        if count == 5:
            print("sleeping")
            time.sleep(60)
        mycursor.execute("SELECT sid from stock_tickers where ticker='" + symbol + "'")
        result = mycursor.fetchall()
        sid = result[0][0]
        data = {"function": "TIME_SERIES_INTRADAY",
                "symbol": symbol,
                "interval": "1min",
                "outputsize": "compact",
                "datatype": "json",
                "apikey": "B8FD7DBR7ZE592RP"}

        response = requests.get(API_URL, data)
        response_json = response.json()

        data = pd.DataFrame.from_dict(response_json['Time Series (1min)'], orient='index').sort_index(axis=1)
        data = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close',
                                    '5. volume': 'Volume'})
        for i in range(len(data)):
            timestamp = data.iloc[i, :].name
            timestamp_array = str(timestamp).strip().split(" ")
            dat = timestamp_array[0]
            tim = timestamp_array[1]
            open_value = data.iloc[i, :]['Open']
            close_value = data.iloc[i, :]['Close']
            low = data.iloc[i, :]['Low']
            high = data.iloc[i, :]['High']
            volume = data.iloc[i, :]['Volume']
            sql = "INSERT INTO realtime_stocks (sid,dat,tim,open_value,low,high,close_value,volume) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (str(sid), str(dat), str(tim), str(open_value), str(low), str(high), str(close_value), str(volume))
            mycursor.execute(sql, val)
            mydb.commit()
        print("Data inserted for: ", symbol)
        count += 1



get_hist()
get_real()




