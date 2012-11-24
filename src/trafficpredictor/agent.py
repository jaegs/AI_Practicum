'''
Created on Nov 13, 2012

@author: Benjamin
'''

from pybrain.rl.agents.learning import LearningAgent, LoggingAgent

class DrivingLearningAgent(LearningAgent):
    '''
    classdocs
    '''


    def __init__(self, controller, learner):
        '''
        Constructor
        '''
        LearningAgent.__init__(self, controller, learner)
        
class DrivingBaselineAgent(LoggingAgent):
    def __init__(self, controller, learner):
        '''
        Constructor
        '''
        LoggingAgent.__init__(self, controller, learner) 