# -*- coding: utf-8 -*-

# Name: Naga Venkata V Vinnakota
# Netid: nvv13
# Ran on Pycharm
#Submitted date: 04/17/2020

import math
import random

random.seed(0)

# Sigmoid activation and deactivation functions
def sigmoid(x):

    return 1.0 / (1.0 + math.exp(-x))


def desigmoid(x):

    return x * (1 - x)


# Random number creation for weight matrices
def randomNum(a, b):

    return (b - a) * random.random() + a


# construction and randomizing the weight matrices
def create_matrix(in_matrix, out, fill=0.0):

    m = []
    for i in range(in_matrix):
        m.append([fill] * out)
    return m


def randomize_Matrix(matrix, lower, upper):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = random.uniform(lower, upper)


# creation of neural networks class
class NN:
    def __init__(self, n_i, n_h, n_o):

        self.layer_in = n_i + 1
        self.hidden_layer = n_h
        self.layer_out = n_o


        self.a_in = [1.0] * self.layer_in
        self.a_hidden = [1.0] * self.hidden_layer
        self.a_out = [1.0] * self.layer_out

        # weight matrices

        # Theta1
        self.w1 = create_matrix(self.layer_in, self.hidden_layer)

        # Theta2
        self.w2 = create_matrix(self.hidden_layer, self.layer_out)

        randomize_Matrix(self.w1, -1, 1)
        randomize_Matrix(self.w2, -1, 1)
        print ("\n" + 'Initial print_weights before training:')
        print ('Theta1: ')
        for i in range(self.layer_in):
            print (self.w1[i])
        print ('Theta2: ')
        for j in range(self.hidden_layer):
            print (self.w2[j])

        self.c_in = create_matrix(self.layer_in, self.hidden_layer)
        self.c_out = create_matrix(self.hidden_layer, self.layer_out)

    # computes the prediction
    def predict(self, inputs):

        for i in range(self.layer_in - 1):
            self.a_in[i] = inputs[i]

        for j in range(self.hidden_layer):
            sum = 0.0
            for i in range(self.layer_in):
                sum += (self.a_in[i] * self.w1[i][j])
            self.a_hidden[j] = sigmoid(sum)

        for k in range(self.layer_out):
            sum = 0.0
            for j in range(self.hidden_layer):
                sum += (self.a_hidden[j] * self.w2[j][k])
            self.a_out[k] = sigmoid(sum)

        return self.a_out

    # reduces the errors by BackPropagation
    def Back_Propagate(self, targets, N, M):

        # calculates the delta for output layer
        output_layer_deltas = [0.0] * self.layer_out
        for k in range(self.layer_out):
            error = targets[k] - self.a_out[k]
            output_layer_deltas[k] = error * desigmoid(self.a_out[k])

        # updates the Theta2
        for j in range(self.hidden_layer):
            for k in range(self.layer_out):

                change = output_layer_deltas[k] * self.a_hidden[j]
                self.w2[j][k] += N * change + M * self.c_out[j][k]
                self.c_out[j][k] = change

        # calculates the delta for hidden layer
        hidden_layer_deltas = [0.0] * self.hidden_layer
        for j in range(self.hidden_layer):
            error = 0.0
            for k in range(self.layer_out):
                error += output_layer_deltas[k] * self.w2[j][k]
            hidden_layer_deltas[j] = error * desigmoid(self.a_hidden[j])

        # updates the Theta1
        for i in range(self.layer_in):
            for j in range(self.hidden_layer):
                change = hidden_layer_deltas[j] * self.a_in[i]
                self.w1[i][j] += N * change + M * self.c_in[i][j]
                self.c_in[i][j] = change

        error = 0.0
        for k in range(len(targets)):
            error = 0.5 * (targets[k] - self.a_out[k]) ** 2
        return error

    # prints the print_weights i.e Theta1 and Theta2
    def print_weights(self):

        print( 'Theta 1: ')
        for i in range(self.layer_in):
            print(self.w1[i])
        print ('Theta 2: ')
        for j in range(self.hidden_layer):
            print (self.w2[j])
        print ('')



    # Trains the print_weights based for the given inputs and learning rate
    def train(self, patterns,N, expectedError, max_iterations=1000):

        M = N / 2

        for i in range(max_iterations):
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.predict(inputs)
                error = self.Back_Propagate(targets, N, M)

            if i == 0:
                print ("\n" + 'First-batch error before training:', error)

            if error < expectedError:
                print("\n" + 'Final print_weights after training the data set:')
                self.print_weights()
                print ('Final error after training:', error)
                print ('The total number of batches run in the training for achieving the expected error:', i + 1)
                break



def main():
    XOR = [
        [[0, 0], [0]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [0]]
    ]

    expectedError = float(input('Please enter the expected error: '))
    learningRate = float(input('Please enter the learning rate: '))
    neural = NN(2, 2, 1)
    neural.train(XOR,learningRate,expectedError)



if __name__ == "__main__":
    main()