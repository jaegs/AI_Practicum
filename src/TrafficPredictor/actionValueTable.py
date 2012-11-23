'''
Created on Nov 22, 2012

@author: test
'''

from pybrain.rl.learners.valuebased import ActionValueTable
import grid, const

def state_number(node, period):
    return grid.node_number(node) + grid.TIME_PERIODS * period

def action(edge):
    return const.DOWN if edge[1][0] > edge[0][0] else const.RIGHT
         

class TrafficActionValueTable(ActionValueTable):
    '''
    classdocs
    '''


    def initialize(self, grid):
        """
            initializes all the (s,a) pairs with the no-traffic travel time
        """
        for node, time in grid.all_shortest_path_lengths():
            in_edges = grid.in_edges([node])
            for edge in in_edges:
                for period in time_periods:
                    s = state_number(edge[0], period)
                    a = action(edge)
                    self.updateValue(s, a, time)
    

    
    
        
        
    
        