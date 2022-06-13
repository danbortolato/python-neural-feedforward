from feedforward import FeedForward

net = FeedForward()
net.train([0], .1, 700)
net.predict()
