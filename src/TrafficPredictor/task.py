'''
Created on Nov 13, 2012

@author: test
'''

from pybrain.rl.environments.task import Task
import grid, const

def state_number((node, period)):
    return grid.node_number(node) * const.TIME_PERIODS + period

class GPS(Task):
    '''
    classdocs
    '''


    def __init__(self, environment):
        '''
        Constructor
        '''
        
    def getReward(self):
        pass
    
    def getObservation(self):
        pass
        #filter here
        
    
    
        