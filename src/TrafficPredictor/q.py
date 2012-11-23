'''
Created on Nov 23, 2012

@author: bgj9
'''
from pybrain.rl.learners.valuebased.q import Q
import const

class GPSLearner(Q):
    def __init__(self, ):
        Q.__init__(self, alpha, gamma)
        self.explorer.epsilon = const.EPSILON
        self.explorer.decay = const.DECAT
        self.alpha = const.ALPHA
        self.gamma = const.GAMMA
        