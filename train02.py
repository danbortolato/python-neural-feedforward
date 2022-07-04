from feedforward import FeedForward

net = FeedForward()
# net .train([0], 0.1, 1000, 'sigmoid') # *ERROR*
# net .train([0], 0.1, 1000, 'binaryStep') # *ERROR*

net .train([0], 0.1, 1000, 'tanh')  # PERIOD = 0000686
# net .train([0], 0.1, 1000, 'relu')  # PERIOD = 0000748
# net .train([0], 0.1, 1000, 'leakyRelu')  # PERIOD = 0000752

net.predict()
