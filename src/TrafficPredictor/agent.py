'''
Created on Nov 13, 2012

@author: Benjamin
'''

from pybrain.rl.agents.learning import LearningAgent

class DrivingAgent(LearningAgent):
    '''
    classdocs
    '''


    def __init__(self, controller, learner):
        '''
        Constructor
        '''
        LearningAgent.__init__(self, controller, learner)