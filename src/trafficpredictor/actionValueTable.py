'''
Created on Nov 22, 2012

@author: test
'''

from pybrain.rl.learners.valuebased import ActionValueTable
import const, task
import grid as g

# TEST
from grid import Grid

class GPSActionValueTable(ActionValueTable):
    def __init__(self):
        ActionValueTable.__init__(self, const.STATES, const.POSSIBLE_ACTIONS)

    def initialize(self, grid):
        """
            initializes all the (s,a) pairs with the no-traffic travel time
        """
        ActionValueTable.initialize(self, float("-inf")) #not every action is possible from every state
        for node, time in grid.all_shortest_path_lengths():
            in_edges = grid.grid.in_edges([node])
            for edge in in_edges:
                for period in xrange(const.PERIODS):
                    s = task.get_state(g.node_number(edge[0]), period) #state involves node previous to current node
                    a = g.action(edge)
                    q = - time - grid.grid.get_edge_data(*edge)["weight"]
                    self.updateValue(s, a, q)

        #Q(s_final, a) for all actions is 0
        for p in xrange(const.PERIODS):
            s = task.get_state(const.NODES - 1, p)
            for a in xrange(const.POSSIBLE_ACTIONS):
                self.updateValue(s, a, 0)

# TEST
if __name__ == '__main__':
    newGrid = Grid()
    GPSActionValueTable().initialize(newGrid)
   
    
        
        
    
        