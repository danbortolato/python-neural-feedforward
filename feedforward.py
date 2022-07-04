class FeedForward():
    def train(self, Inputs=[], Target=0, Epochs=1, activation='sigmoid'):
        import math as m
        self.m = m
        self.activation = activation
        self.Inputs = Inputs
        self.Target = Target
        self.Epochs = Epochs

    def gradientDescent(self, n=0):
        return n * (1 - n)

    # hyperbolic
    def tanh(self, n=0): return self.m.sinh(n) / self.m.cosh(n)
    # sigmoid
    def sigmoid(self, n=0): return 1 / (1 + pow(self.m.e, -n))
    # relu
    def relu(self, n=0): return max([n, 0])
    # leaky relu
    def leakyRelu(self, n=0): return max([n, .01])
    # biary
    def binaryStep(self, n=0):
        if n >= 0: return 1
        else: return 0
    
    def predict(self):
        if self.Target <= 0:
            self.Target = .1
        elif self.Target > 1:
            self.Target = 1

        weights = []
        from math import tanh
        from random import random
        for _ in self.Inputs:
            weights.append(random())

        i = 1
        while i <= self.Epochs:
            multiply = []
            j = 0
            while j < len(self.Inputs):
                if self.Inputs[j] <= 0: self.Inputs[j] = .1
                multiply.append(self.Inputs[j] * weights[j])
                j += 1
            _sum = sum(multiply)
            if self.activation == 'tanh':
                output = round(self.tanh(_sum), 4)
            elif self.activation == 'sigmoid':
                output = round(self.sigmoid(_sum), 4)
            elif self.activation == 'relu':
                output = round(self.relu(_sum), 4)
            elif self.activation == 'leakyRelu':
                output = round(self.leakyRelu(_sum), 4)
            elif self.activation == 'binaryStep':
                output = round(self.binaryStep(_sum), 4)
            else:
                output = round(self.sigmoid(_sum), 4)

            error = abs(self.Target - output)
            j = 0
            while j < len(self.Inputs):
                weights[j] += self.Inputs[j] * self.gradientDescent(error)
                j += 1
            epoch = str(i).rjust(7, '0')

            print(f'period: {epoch} - error tax: {error:.4f} - output: {output:.4f}')
            i += 1
