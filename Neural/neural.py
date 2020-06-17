

# Software Engineering Project - Group 14
# written and debugged by: Priya, Lasya, Varun

import json, time
from datetime import datetime
from time import mktime
import sys
import csv

#from neuralnetwork import NeuralNetwork
#import neuralnetwork

import math, random, string

random.seed(0)


## ================================================================

# calculate a random number a <= rand < b
def rand(a, b):
    return (b - a) * random.random() + a


def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m


def sigmoid(x):
    return math.tanh(x)


# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y ** 2


## ================================================================

class NeuralNetwork:
    def __init__(self, inputNodes, hiddenNodes, outputNodes):
        # number of input, hidden, and output nodes
        self.inputNodes = inputNodes + 1  # +1 for bias node
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes

        # activations for nodes
        self.inputActivation = [1.0] * self.inputNodes
        self.hiddenActivation = [1.0] * self.hiddenNodes
        self.outputActivation = [1.0] * self.outputNodes

        # create weights
        self.inputWeight = makeMatrix(self.inputNodes, self.hiddenNodes)
        self.outputWeight = makeMatrix(self.hiddenNodes, self.outputNodes)
        # set them to random vaules
        for i in range(self.inputNodes):
            for j in range(self.hiddenNodes):
                self.inputWeight[i][j] = rand(-0.2, 0.2)
        for j in range(self.hiddenNodes):
            for k in range(self.outputNodes):
                self.outputWeight[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum
        self.ci = makeMatrix(self.inputNodes, self.hiddenNodes)
        self.co = makeMatrix(self.hiddenNodes, self.outputNodes)

    def update(self, inputs):
        if len(inputs) != self.inputNodes - 1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.inputNodes - 1):
            self.inputActivation[i] = inputs[i]

        # hidden activations
        for j in range(self.hiddenNodes):
            sum = 0.0
            for i in range(self.inputNodes):
                sum = sum + self.inputActivation[i] * self.inputWeight[i][j]
            self.hiddenActivation[j] = sigmoid(sum)

        # output activations
        for k in range(self.outputNodes):
            sum = 0.0
            for j in range(self.hiddenNodes):
                sum = sum + self.hiddenActivation[j] * self.outputWeight[j][k]
            self.outputActivation[k] = sigmoid(sum)

        return self.outputActivation[:]

    def backPropagate(self, targets, N, M):
        if len(targets) != self.outputNodes:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.outputNodes
        for k in range(self.outputNodes):
            error = targets[k] - self.outputActivation[k]
            output_deltas[k] = dsigmoid(self.outputActivation[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.hiddenNodes
        for j in range(self.hiddenNodes):
            error = 0.0
            for k in range(self.outputNodes):
                error = error + output_deltas[k] * self.outputWeight[j][k]
            hidden_deltas[j] = dsigmoid(self.hiddenActivation[j]) * error

        # update output weights
        for j in range(self.hiddenNodes):
            for k in range(self.outputNodes):
                change = output_deltas[k] * self.hiddenActivation[j]
                self.outputWeight[j][k] = self.outputWeight[j][k] + N * change + M * self.co[j][k]
                self.co[j][k] = change

        # update input weights
        for i in range(self.inputNodes):
            for j in range(self.hiddenNodes):
                change = hidden_deltas[j] * self.inputActivation[i]
                self.inputWeight[i][j] = self.inputWeight[i][j] + N * change + M * self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5 * (targets[k] - self.outputActivation[k]) ** 2

        return error

    def test(self, inputNodes):
        # print(inputNodes, '->', self.update(inputNodes))
        return self.update(inputNodes)[0]

    def weights(self):
        print('Input weights:')
        for i in range(self.inputNodes):
            print(self.inputWeight[i])
        print()
        print('Output weights:')
        for j in range(self.hiddenNodes):
            print(self.outputWeight[j])

    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate, M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            # if i % 100 == 0:
            # print('error %-.5f' % error)
## ================================================================
from pip._vendor.msgpack.fallback import xrange


def normalizePrice(price, minimum, maximum):
    return ((2 * price - (maximum + minimum)) / (maximum - minimum))


def denormalizePrice(price, minimum, maximum):
    return (((price * (maximum - minimum)) / 2) + (maximum + minimum)) / 2


## ================================================================

def rollingWindow(seq, windowSize):
    it = iter(seq)
    win = [next(it) for cnt in xrange(windowSize)]  # First window
    yield win
    for e in it:  # Subsequent windows
        win[:-1] = win[1:]
        win[-1] = e
        yield win


def getMovingAverage(values, windowSize):
    movingAverages = []

    for w in rollingWindow(values, windowSize):
        movingAverages.append(sum(w) / len(w))

    return movingAverages


def getMinimums(values, windowSize):
    minimums = []

    for w in rollingWindow(values, windowSize):
        minimums.append(min(w))

    return minimums


def getMaximums(values, windowSize):
    maximums = []

    for w in rollingWindow(values, windowSize):
        maximums.append(max(w))

    return maximums


## ================================================================

def getTimeSeriesValues(values, window):
    movingAverages = getMovingAverage(values, window)
    minimums = getMinimums(values, window)
    maximums = getMaximums(values, window)

    returnData = []

    # build items of the form [[average, minimum, maximum], normalized price]
    for i in range(0, len(movingAverages)):
        inputNode = [movingAverages[i], minimums[i], maximums[i]]
        price = normalizePrice(values[len(movingAverages) - (i + 1)], minimums[i], maximums[i])
        outputNode = [price]
        tempItem = [inputNode, outputNode]
        returnData.append(tempItem)

    return returnData


## ================================================================

def getHistoricalData(stockSymbol):
    historicalPrices = []
    histprice=0
    if stockSymbol=='AAPL':

        with open("AAPL.csv", newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                historicalPrices.append(row['target'])

        histprice = [float(i) for i in historicalPrices]

    return histprice


## ================================================================

def getTrainingData(stockSymbol):
    historicalData = getHistoricalData(stockSymbol)

    # reverse it so we're using the most recent data first, ensure we only have 9 data points
    historicalData.reverse()
    del historicalData[9:]

    # get five 5-day moving averages, 5-day lows, and 5-day highs, associated with the closing price
    trainingData = getTimeSeriesValues(historicalData, 5)

    previousdata=historicalData[1]
    currentdata=historicalData[0]

    return trainingData,previousdata,currentdata


def getPredictionData(stockSymbol):
    historicalData = getHistoricalData(stockSymbol)

    # reverse it so we're using the most recent data first, then ensure we only have 5 data points
    historicalData.reverse()
    del historicalData[5:]

    # get five 5-day moving averages, 5-day lows, and 5-day highs
    predictionData = getTimeSeriesValues(historicalData, 5)
    # remove associated closing price
    predictionData = predictionData[0][0]

    return predictionData


## ================================================================

def analyzeSymbol(stockSymbol):
   # startTime = time.time()

    trainingData, previousdata, currentdata = getTrainingData(stockSymbol)


    network = NeuralNetwork(inputNodes=3, hiddenNodes=3, outputNodes=1)

    network.train(trainingData)

    # get rolling data for most recent day
    predictionData = getPredictionData(stockSymbol)

    # get prediction
    returnPrice = network.test(predictionData)

    # de-normalize and return predicted stock price
    predictedStockPrice = denormalizePrice(returnPrice, predictionData[1], predictionData[2])

    # create return object, including the amount of time used to predict
    tp=0
    tn=0
    fn=0
    fp=0
    if previousdata>currentdata and previousdata>predictedStockPrice:
        tn+=1
    else:
        fp+=1
    if previousdata<currentdata and previousdata<predictedStockPrice:
        tp+=1
    else:
        fn+=1

    return tp, fp


## ================================================================

if __name__ == "__main__":
    stock=input('Enter stock')
    print(analyzeSymbol(stock))

