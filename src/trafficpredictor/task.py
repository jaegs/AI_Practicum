'''
Created on Nov 13, 2012

@author: test
'''

from pybrain.rl.environments.episodic import EpisodicTask
import const, math, random, grid

def get_state(node, period):
    return [node * const.PERIODS + (period % const.PERIODS)]


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
    
    def reset(self):
        self.prev_time = random.uniform(0,const.PERIODS)
        self.start_time = self.prev_time
        #choose a random node that is not the destination
        node = grid.node_number(const.DESTINATION)
        
        #See what happens
        node = 0
        
#        while(node == grid.node_number(const.DESTINATION)):
#            node = random.randint(0, const.NODES - 1)
        self.start_node = node 
        self.env.reset_grid(self.prev_time, node)
        EpisodicTask.reset(self)
        
    def getReward(self):
        return self.prev_time - self.current_time
    
    def getObservation(self):
        self.prev_time = self.current_time
        self.current_time, node = self.env.getSensors()
        period = math.floor(self.current_time) 
        state = get_state(node, period)
        return state
        
    def isFinished(self):
        if self.env.current_node == const.DESTINATION:
            self.total_time = self.current_time - self.start_time
            return True
        else:
            return False
    
    
        