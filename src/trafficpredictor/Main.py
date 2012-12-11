'''
Created on Nov 22, 2012

@author: Benjamin Jaeger
'''

from grid import Grid
from task import GPS, get_state
from agent import DrivingLearningAgent
from q import *
from experiment import TripExperiment
from actionValueTable import GPSActionValueTable
import const
import math
import matplotlib.pyplot as plt
import scipy.stats as sps
import numpy as np


if __name__ == '__main__':
    environment = Grid()
    controller = GPSActionValueTable()
    controller.initialize(environment)
    
    learner = GPSLearnerBasic()#GPSLearner()
    agent = DrivingLearningAgent(controller, learner)
    task = GPS(environment)
    experiment = TripExperiment(task, agent)
    
    #Initialize the variables for statistical analysis
    data = [None] * const.TRIALS
    
    for t in xrange(const.TRIALS):
        experiment.doEpisodes(number = 1)
        i = int(task.start_time)
        data[t] = (i,task.total_time /  environment.total_jumps, t)
        agent.learn()
        agent.reset()
        if t % 100 == 0:
            print t
    
    data_by_period = []
    for i in xrange(const.PERIODS):
        data_by_period.append([d[1:] for d in data if d[0] == i])
    
    
#    #print the correlation values
#    for i in xrange(const.PERIODS):
#        print "(Correlation,p-value) for time of day %d" % i
#        traveltime, itert = zip(*data_by_period[i])
#        print sps.pearsonr(traveltime, itert)
    
    #Plot one for a constant time of day
    plt.title("Measured Travel Times vs Learning")
    if not const.USE_PERIODS:
        traveltime, itert = zip(*data_by_period[0])
    else:
        traveltime, itert = zip(*data_by_period[const.MID_DAY])
    scatter = plt.scatter(itert, traveltime, label="Travel times")
    plt.setp(scatter, linewidth =.1)
    plt.show()
