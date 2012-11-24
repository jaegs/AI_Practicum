'''
Created on Nov 22, 2012

@author: test
'''

from pybrain.rl.learners.valuebased import ActionValueTable
import grid, const, task

def state(node, period):
    return grid.node_number(node) + const.PERIODS * period
         

class GPSActionValueTable(ActionValueTable):
    def __init__(self):
        ActionValueTable.__init__(self, const.STATES, const.POSSIBLE_ACTIONS)


    def initialize(self, grid):
        """
            initializes all the (s,a) pairs with the no-traffic travel time
        """
        ActionValueTable.initialize(self, float("-inf")) #not every action is possible from every state
        for node, time in grid.all_shortest_path_lengths():
            in_edges = grid.in_edges([node])
            for edge in in_edges:
                for period in xrange(const.PERIODS):
                    s = task.state(edge[0], period) #state involves node previous to current node
                    a = task.action(edge)
                    self.updateValue(s, a, -time)
    

    
    
        
        
    
        