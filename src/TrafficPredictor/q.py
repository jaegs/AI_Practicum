 '''
Created on Nov 23, 2012

@author: bgj9
'''
from pybrain.rl.learners.valuebased.q import Q
from pybrain.datasets import ReinforcementDataSet
import const

class GPSLearner(Q):
    def __init__(self, ):
        Q.__init__(self, const.ALPHA, const.GAMMA)
        self.explorer.epsilon = const.EPSILON
        self.explorer.decay = const.DECAY
        self.dataset2 = ReinforcementDataSet(self.agent.indim, self.agent.outdim)
        
    
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
        for seq in self.dataset:
            self.dataset2.newSequence()
            for state, action, reward in seq: #add states of adjacent time periods
                period = state % const.NODES
                node = state / const.PERIODS
                self.dataset2.addSample(node * const.PERIODS + (period + 1) % const.PERIODS, action, reward)
                self.dataset2.addSample(node * const.PERIODS + (period - 1) % const.PERIODS, action, reward)
        self.dataset = self.dataset2
        self.alpha = const.ALPHA_ADJ_PERIOD
        Q.learn()
        self.dataset = self.agent.history