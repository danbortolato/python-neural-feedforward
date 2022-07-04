from feedforward import FeedForward

net = FeedForward()
net .train([0], 0.1, 1000, 'tanh')
net.predict()
