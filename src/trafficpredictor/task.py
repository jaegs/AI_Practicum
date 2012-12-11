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
        self.reward = 0
    
    def reset(self):
        self.current_time = self.prev_time = 0.0
        if const.USE_PERIODS:
            self.current_time = self.prev_time = random.uniform(0,const.PERIODS)
        self.current_time = const.MID_DAY
        #print "ST", self.current_time
        self.start_time = self.current_time
        self.counter = 0
        #choose a random node that is not the destination
        node = grid.node_number(const.DESTINATION)
        while(node == grid.node_number(const.DESTINATION)):       
            node = random.randint(0, const.NODES - 1)
        #See what happens
        if const.SAME_START:
            node = 0
        
#        while(node == grid.node_number(const.DESTINATION)):
#            node = random.randint(0, const.NODES - 1)
        self.start_node = node 
        self.env.reset_grid(self.current_time, node)
        EpisodicTask.reset(self)
        
    def getReward(self):
        if self.env.current_time == self.current_time:
            return self.prev_reward
        self.prev_time = self.current_time
        self.current_time = self.env.current_time
        #print "CTT", self.current_time
        self.prev_reward = self.reward
        self.reward = self.prev_time - self.current_time
        #print "R", reward
        assert self.reward <= 0.0
        #pybrain accidently calls this function twice per action, but only uses the value the 2nd time
        return 9001
    
    def getObservation(self):
        self.counter += 1
        assert self.counter < const.GRID_SIZE * 4, "Looping"
        node = self.env.getSensors()
        period = int(self.current_time % const.PERIODS) 
        state = get_state(node, period)
        assert state[0] >= 0 and state[0] < const.STATES
        return state
     
    def isFinished(self):
        if self.env.current_node == const.DESTINATION:
            self.total_time = self.current_time - self.start_time
            return True
        else:
            return False
    
    
        