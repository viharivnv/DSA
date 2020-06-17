# -*- coding: utf-8 -*-
import math
import random

random.seed(0)


# Sigmoid activation and deactivation functions
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def dsigmoid(y):
    return y * (1 - y)


# Random number creation
def randomNum(a, b):
    return (b - a) * random.random() + a


def constructMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m


def randomizeMatrix(matrix, a, b):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.uniform(a, b)


class NN:
    def __init__(self, ni, nh, no):

        self.ni = ni + 1
        self.nh = nh
        self.no = no

        #
        self.ai = [1.0] * self.ni
        self.ah = [1.0] * self.nh
        self.ao = [1.0] * self.no

        # weight matrix
        self.wi = constructMatrix(self.ni, self.nh)  # Theta1
        self.wo = constructMatrix(self.nh, self.no)  # Theta2

        randomizeMatrix(self.wi, -1, 1)
        randomizeMatrix(self.wo, -1, 1)
        print("\n" + 'Initial print_weights:')
        print('Theta1: ')
        for i in range(self.ni):
            print(self.wi[i])
        print('Theta2: ')
        for j in range(self.nh):
            print(self.wo[j])

        self.ci = constructMatrix(self.ni, self.nh)
        self.co = constructMatrix(self.nh, self.no)

    def runNN(self, inputs):
        """
        forward propagation
        :param inputs:
        :return:
        """
        if len(inputs) != self.ni - 1:
            print('incorrect number of inputs')

        for i in range(self.ni - 1):
            self.ai[i] = inputs[i]

        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum += (self.ai[i] * self.wi[i][j])
            self.ah[j] = sigmoid(sum)

        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum += (self.ah[j] * self.wo[j][k])
            self.ao[k] = sigmoid(sum)

        return self.ao

    def backPropagate(self, targets, N, M):
        """
        backpropagation
        :param targets:
        :param N: learning rate
        :param M: old learning rate
        :return:
        """

        # calculate the delta for output layer
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k] - self.ao[k]
            output_deltas[k] = error * dsigmoid(self.ao[k])

        # update the Theta2
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] += N * change + M * self.co[j][k]
                self.co[j][k] = change

        # calculate the delta for hidden layer
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error += output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = error * dsigmoid(self.ah[j])

        # update the Theta1
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j] * self.ai[i]
                # print 'activation',self.ai[i],'synapse',i,j,'change',change
                self.wi[i][j] += N * change + M * self.ci[i][j]
                self.ci[i][j] = change

        error = 0.0
        for k in range(len(targets)):
            error = 0.5 * (targets[k] - self.ao[k]) ** 2
        return error

    def weights(self):
        """
        print the weight
        """
        print("\n" + 'Final print_weights:')
        print('Theta 1: ')
        for i in range(self.ni):
            print(self.wi[i])
        print('Theta 2: ')
        for j in range(self.nh):
            print(self.wo[j])
        print('')

    def test(self, patterns):
        """
        test
        :param patterns:test
        """
        print("\n")
        for p in patterns:
            inputs = p[0]
            # print 'Inputs:', p[0], '-->', self.predict(inputs), '\tTarget', p[1]
            print('Inputs:', p[0], '-->', self.runNN(inputs), 'Target'.rjust(10), p[1])

    def train(self, patterns, target,max_iterations=1000, N=0.5, M=0.5):
        """
        train
        :param patterns: the batch
        :param max_iterations:
        :param N: learning rate
        :param M: last time learning rate
        """

        N = learningRate
        M = N / 2
        for i in range(max_iterations):
            for p in patterns:
                inputs = p[0]
                targets = target
                self.runNN(inputs)
                error = self.backPropagate(targets, N, M)

            if i == 0:
                print("\n" + 'first-batch error    ', error)

            if error < expectedError:
                print("\n" + 'final error          ', error)
                print("\n" + 'the total number of batches run through in the training', i + 1)
                break
        # self.test(patterns)


def main():
    pat = [
        [[0, 0]],
        [[0, 1]],
        [[1, 0]],
        [[1, 1]]
    ]
    target=[0,1,1,0]
    global expectedError
    global learningRate
    expectedError = float(input('Please input the expected error: '))
    learningRate = float(input('Please input the learning rate: '))
    myNN = NN(2, 2, 1)
    myNN.train(pat,target)
    myNN.weights()


if __name__ == "__main__":
    main()