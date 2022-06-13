class FeedForward():
    def train(self, Inputs=[], Target=0, Epochs=1):
        self.Inputs = Inputs
        self.Target = Target
        self.Epochs = Epochs

    def gradientDescent(self, n=0):
        return n * (1 - n)
    
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
            output = round(tanh(_sum), 4)

            error = abs(self.Target - output)
            j = 0
            while j < len(self.Inputs):
                weights[j] += self.Inputs[j] * self.gradientDescent(error)
                j += 1
            epoch = str(i).rjust(7, '0')

            print(f'period: {epoch} - error tx: {error:.4f} - out: {output:.4f}')
            i += 1
