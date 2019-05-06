# This class represents a Neural Network that will be instantiated
# separately in each of the Birds. The Architecture is 4 input nodes, 30 hidden nodes,
# and 1 output node.
# Inputs: Distance to next obstacle, height difference from next obstacle, height from ground, velocity
# Output: If output node > 0.5, jump, else don't jump
#
# The Neural Network is a very simple FeedForward Neural network implemented without the use of a NN library.
# The main reason for this is for the learning experience of implementing a NN 'from scratch'
# Numpy and Scipy are used for easy mathematical computation
import numpy as np
import scipy.special
import random


class NeuralNetwork:

    # initializing the Neural Net, parent1 and parent2 are Bird objects. If no parent, use 'None'
    def __init__(self, parent1, parent2):
        # Set number of nodes for each layer
        self.i_nodes = 4              # node 1 is horizontal distance from next obstacle, node 2 is height difference
        self.h_nodes = 100            # node 3 is heignt from ground. Node 4 is velocity. H node is from the top obstacle rectangle's bottom edge
        self.o_nodes = 1              # bottom edge. If output node > .5 flap, else do nothing

        # Link weight matrices
        # input to hidden, and hidden to output
        # if creating a brain with no parents, then randomly initialize weights and biases
        if parent1 == 'None' and parent2 == 'None':
            self.w_ih = (np.random.rand(self.h_nodes, self.i_nodes) - 0.5)   # weights input to hidden
            self.b_h = (np.random.rand(self.h_nodes) - 0.5).reshape(self.h_nodes, 1)  # biases of hidden layer
            self.w_ho = (np.random.rand(self.o_nodes, self.h_nodes) - 0.5)   # weights hidden to output
            self.b_o = (np.random.rand(self.o_nodes) - 0.5).reshape(1, 1)    # biases of output
        # else if bird has a parent1, make it a clone of it's parent1
        elif parent1 != 'None':
            self.w_ih = parent1.brain.w_ih.copy()
            self.b_h = parent1.brain.b_h.copy()
            self.w_ho = parent1.brain.w_ho.copy()
            self.b_o = parent1.brain.b_o.copy()
        # if the bird also has a parent2, perform crossover with its parent1 and parent2
        if parent2 != 'None':
            self.crossover(parent1, parent2)

        # sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

    # take the input to a neural network and returns the network's output
    def query(self, inputs_list):
        # .T means inputs with be the transposed matrix of inputs_list
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_inputs = np.add(np.dot(self.w_ih, inputs), self.b_h)
        # print(hidden_inputs.shape, " ", self.b_h.shape)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.add(np.dot(self.w_ho, hidden_outputs), self.b_o)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

    # mutates 15% of the weights
    def mutate(self):
        for weight in self.w_ih:
            if random.randint(0, 100) < 10:
                weight += random.uniform(-.2, .2)
        for weight in self.w_ho:
            if random.randint(0, 100) < 10:
                weight += random.uniform(-.2, .2)
        for bias in self.b_h:
            if random.randint(0, 100) < 10:
                bias += random.uniform(-.1, .1)
        for bias in self.b_h:
            if random.randint(0, 100) < 10:
                bias += random.uniform(-.1, .1)

    # a random crossover of weights between 2 parents
    # i is a random int which will be the split point of which parents
    # weights are copied to the child
    def crossover(self, p1, p2):
        for weight, i in zip(self.w_ih, range(len(self.w_ih))):
            if i < random.randint(0, len(self.w_ih)):
                self.w_ih[i] = p1.brain.w_ih[i]
            else:
                self.w_ih[i] = p2.brain.w_ih[i]
        for weight, i in zip(self.w_ho, range(len(self.w_ho))):
            if i < random.randint(0, len(self.w_ho)):
                self.w_ho[i] = p1.brain.w_ho[i]
            else:
                self.w_ho[i] = p2.brain.w_ho[i]
        for bias, i in zip(self.b_h, range(len(self.b_h))):
            if i < random.randint(0, len(self.b_h)):
                self.b_h[i] = p1.brain.b_h[i]
            else:
                self.b_h[i] = p2.brain.b_h[i]
        for bias, i in zip(self.b_o, range(len(self.b_o))):
            if i < random.randint(0, len(self.b_o)):
                self.b_o[i] = p1.brain.b_o[i]
            else:
                self.b_o[i] = p2.brain.b_o[i]
