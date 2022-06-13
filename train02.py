from feedforward import FeedForward

net = FeedForward()
net.train([0, 0], .2, 450)
net.predict()
