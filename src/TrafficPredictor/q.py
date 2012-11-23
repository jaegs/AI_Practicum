'''
Created on Nov 23, 2012

@author: bgj9
'''
from pybrain.rl.learners.valuebased.q import Q
import const

class GPSLearner(Q):
    def __init__(self, ):
        Q.__init__(self, const.ALPHA, const.GAMMA)
        self.explorer.epsilon = const.EPSILON
        self.explorer.decay = const.DECAY
        
    
    def learn(self):
        """
            Performs Q learning based on observations but also
            performs learning on states that are adjacent time periods,
            albeit with a slower learning rate.
            
            For example, traffic at 4:30PM on an edge will be somewhat similar to
            traffic at 5:00. Hence, we can use an observation at 4:30 to update 5:00.
        """
        self.alpha = const.ALPHA
        Q.learn() #do normal learning
        samples = self.dataset
        new_samples = []
        for seq in samples:
            new_seq = []
            for state, action, reward in seq: #add states of adjacent time periods
                period = state % const.NODES
                node = state / const.PERIODS
                new_seq[:] = (node * const.PERIODS + (period + 1) % const.PERIODS, action, reward)
                new_seq[:] = (node * const.PERIODS + (period - 1) % const.PERIODS, action, reward)
            new_samples[:] = new_seq
        self.dataset = new_samples
        self.alpha = const.ALPHA_ADJ_PERIOD
        Q.learn()