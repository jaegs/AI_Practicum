'''
Created on Nov 13, 2012

@author: Benjamin
'''

from pybrain.rl.agents.learning import LearningAgent

class TrafficAgent(LearningAgent): #maybe use LearningAgent...
    '''
    classdocs
    '''


    def __init__(self, controller, learner):
        '''
        Constructor
        '''
        LearningAgent.__init__(self, controller, learner)