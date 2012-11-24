'''
Created on Nov 13, 2012

@author: test
'''

from pybrain.rl.environments.episodic import EpisodicTask
import grid, const, math, random

def state(node, period):
    return node * const.TIME_PERIODS + period

def action(edge):
    return const.DOWN if edge[1][0] > edge[0][0] else const.RIGHT

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
        self.prev_time = random.uniform(0,24)
        node = random.randint(0, const.NODES)
        self.reset(self.prev_time, node)
        EpisodicTask.reset(self)
        
    def getReward(self):
        return self.prev_time - self.current_time
    
    def getObservation(self):
        self.prev_time = self.current_time
        sensors = self.env.getSensors()
        self.current_time = sensors[const.SENSOR_TIME_POS]
        node = sensors[const.SENSOR_NODE_POS]
        period = math.floor(self.current_time * const.PERIODS / const.HOURS)
        state = state(node, period)
        return state
        
        #filter here
        
    def isFinished(self):
        return self.current_state == const.DESTINATION
    
    
        