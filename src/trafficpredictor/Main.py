'''
Created on Nov 22, 2012

@author: Benjamin Jaeger
'''

from grid import Grid
from task import GPS
from agent import DrivingLearningAgent
from q import GPSLearner
from experiment import TripExperiment
from actionValueTable import GPSActionValueTable
import const
import grid as gri

if __name__ == '__main__':
    environment = Grid()
    controller = GPSActionValueTable()
    controller.initialize(environment)
    
    learner = GPSLearner()
    
    agent = DrivingLearningAgent(controller, learner)
    task = GPS(environment)
    
    experiment = TripExperiment(task, agent)
    
    for _ in range(const.TRIALS):
        experiment.doEpisodes()
        print "Start Node", gri.int_to_node(task.start_node)
        print "Start Time:", task.start_time
        print "End Time:", task.current_time
        print "Total Time:", task.total_time, "\n\n\n"
        if task.total_time < 0:
            print "It's negative"
            raise Exception()
        
        agent.learn()
        agent.reset()
    