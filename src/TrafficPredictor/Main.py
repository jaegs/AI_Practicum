'''
Created on Nov 22, 2012

@author: Benjamin Jaeger
'''

from grid import Grid
from task import GPS
from agent import DrivingAgent
from q import GPSLearner
from experiment import TripExperiment
from actionValueTable import GPSActionValueTable
import const

if __name__ == '__main__':
    environment = Grid()
    controller = GPSActionValueTable()
    controller.initialize(environment)
    learner = GPSLearner()
    agent = DrivingAgent(controller, learner)
    task = GPS(environment)
    
    experiment = TripExperiment(task, agent)
    