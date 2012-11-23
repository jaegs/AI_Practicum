'''
Created on Nov 23, 2012

@author: Benjamin
'''

#edge
NOISE_STD_DEV = 0.5

#actions
DOWN = 0
RIGHT = 1

#grid
GRID_SIZE = 5
NODES = GRID_SIZE**2
TIME_PERIODS = 48
MAX_WEIGHT = 10
MAX_INTENSITY = 100
MAX_DURATION = 10
DESTINATION = (GRID_SIZE - 1, GRID_SIZE - 1)
EDGE_GRADIENT = .005 #percent change in coeff's between edges
PERCENT_SEED_EDGES = .1


#Q Learning
ALPHA = 0.5 #learning rate
ALPHA_ADJ_PERIOD = 0.3 #learning rate for states with adjacent time periods
GAMMA = 1.0 #discount factor 

#Epsilon Greedy Explorer
EPSILON = 0.3
DECAY = 0.9999

#task
PERIODS = 48 #number of time periods in a day
STATES = NODES * PERIODS
POSSIBLE_ACTIONS = 2