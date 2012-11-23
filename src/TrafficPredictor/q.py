'''
Created on Nov 23, 2012

@author: bgj9
'''
from pybrain.rl.learners.valuebased.q import Q

class GPSLearner(Q):
    def __init__(self, alpha=0.5, gamma=0.99, epsilon = 0.3, decay = 0.9999):
        Q.__init__(self, alpha, gamma)
        self.explorer.epsilon = epsilon
        self.explorer.decay = decay
        