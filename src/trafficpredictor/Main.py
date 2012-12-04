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
import math
import matplotlib.pyplot as plt
import scipy.stats as sps


if __name__ == '__main__':
    
    environment = Grid()
    controller = GPSActionValueTable()
    controller.initialize(environment)
    
    learner = GPSLearner()
    agent = DrivingLearningAgent(controller, learner)
    task = GPS(environment)
    experiment = TripExperiment(task, agent)
    
    #Initialize the variables for statistical analysis
    travel_times, iteration_nums = [], []
    iterations = []
    for i in range(const.TIME_PERIODS):
        travel_times.append([])
    for i in range(const.TIME_PERIODS):
        iteration_nums.append([])
    for i in range(const.TIME_PERIODS):
        iterations.append(0)
    counter = 0
    
    for _ in range(const.TRIALS):
        experiment.doEpisodes()

        for i in range(const.TIME_PERIODS):
            if math.floor(task.start_time) == i:
                travel_times[i].append(task.total_time / environment.total_jumps)
                iteration_nums[i].append(iterations[i])
                iterations[i] += 1
                break
        
        agent.learn()
        agent.reset()
        
        
        if counter % 100 == 0:
            print counter
        counter += 1
    
    
    
    #print the correlation values
    for i in range(const.TIME_PERIODS):
        print "(Correlation,p-value) for time of day %d" % i
        correlation,pval = sps.pearsonr(iteration_nums[i], travel_times[i])
        print sps.pearsonr(iteration_nums[i], travel_times[i])
    
    #Plot one for a constant time of day
    plt.title("Measured Travel Times vs Learning")
    scatter = plt.scatter(iteration_nums[16], travel_times[16], label="Travel times")
    plt.setp(scatter, linewidth =.1)
    plt.show()