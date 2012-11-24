'''
Created on Nov 13, 2012

@author: test
'''

from pybrain.rl.environments.episodic import EpisodicTask
import const, math, random, grid

def state(node, period):
    return node * const.TIME_PERIODS + period



class GPS(EpisodicTask):
    '''
    classdocs
    '''


    def __init__(self, environment):
        '''
        Constructor
        '''
        EpisodicTask.__init__(self, environment)
        self.prev_time = 0
        self.current_time = 0 
        self.reset()
    
    def reset(self):
        self.prev_time = random.uniform(0,const.MINS_IN_A_DAY)
        node = random.randint(0, const.NODES)
        self.reset(self.prev_time, node)
        EpisodicTask.reset(self)
        
    def getReward(self):
        return self.prev_time - self.current_time
    
    def getObservation(self):
        self.prev_time = self.current_time
        self.current_time, node = self.env.getSensors()
        period = math.floor(self.current_time * const.PERIODS / const.MINS_IN_A_DAY)
        state = state(node, period)
        return state
        
        
    def isFinished(self):
        return self.current_state == grid.node_number(const.DESTINATION)
    
    
        