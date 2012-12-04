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
import matplotlib.pyplot as plt


if __name__ == '__main__':
    iterations = 0
    environment = Grid()
    controller = GPSActionValueTable()
    controller.initialize(environment)
    
    learner = GPSLearner()
    
    agent = DrivingLearningAgent(controller, learner)
    task = GPS(environment)
    
    experiment = TripExperiment(task, agent)
    travel_times, iteration_nums = [], []
    for _ in range(const.TRIALS):
        experiment.doEpisodes()
#        print "Iteration:", iterations
#        print "Total Jumps:", environment.total_jumps
#        print "Total Time:", task.total_time, "\n\n\n"
        travel_times.append(task.total_time / environment.total_jumps)
        iteration_nums.append(iterations)
        if task.total_time < 0:
            print "It's negative"
            raise Exception()
        
        agent.learn()
        agent.reset()
        
        iterations += 1
        if iterations % 100 == 0:
            print iterations
    
    
    scatter = plt.scatter(iteration_nums, travel_times, label="Travel times")
    
    plt.setp(scatter, linewidth =.1)
    plt.title("Measured Travel Times vs Learning")
    plt.legend()
    plt.show()
    