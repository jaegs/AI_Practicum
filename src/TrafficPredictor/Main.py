'''
Created on Nov 22, 2012

@author: Benjamin Jaeger
'''

from pybrain.rl.learners import Q
from pybrain.rl.learners.valuebased import ActionValueTable

from grid import Grid
from task import ObservableGrid


if __name__ == '__main__':
    environment = Grid()
    controller = ActionValueTable(GRID_SIZE**2, 2)
    
    controller.initialize(.1) #init with estimated time
    learner = Q()
    
    task = ObservableGrid(environment)
    
    experiment = Experiment(task, agent)
    