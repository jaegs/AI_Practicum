'''
Created on Nov 23, 2012

@author: Benjamin
'''

#edge
NOISE_STD_DEV = 1.0

#actions
DOWN = 0
RIGHT = 1
LEFT = 2
UP = 3

#grid
GRID_SIZE = 3#10
NODES = GRID_SIZE**2
PERIODS = 1 #48
MAX_WEIGHT = 1.5
MIN_WEIGHT = .5
MAX_DURATION = 9.
MAX_DURATION = 5.
MAX_INTENSITY = 75. / PERIODS
MIN_INTENSITY = 25. / PERIODS
MID_DAY = PERIODS / 2 - 1
DESTINATION = (GRID_SIZE - 1, GRID_SIZE - 1)
EDGE_GRADIENT = .005 #percent change in coeff's between edges
PERCENT_SEED_EDGES = .1
SENSOR_TIME_POS = 1
SENSOR_NODE_POS = 0


#Q Learning
ALPHA = .2 #0.5 #learning rate
ALPHA_ADJ_PERIOD = 0.3 #learning rate for states with adjacent time periods
GAMMA = 1.0 #discount factor 

#Epsilon Greedy Explorer
EPSILON = 0.0 #0.1
DECAY = 0.9 #0.9999

#task
STATES = NODES * PERIODS
POSSIBLE_ACTIONS = 2

#main
TRIALS = 4000
