'''
Created on Nov 23, 2012

@author: Benjamin
'''

#edge
NOISE_STD_DEV = 2.0

#actions
DOWN = 0
RIGHT = 1
LEFT = 2
UP = 3

#grid
GRID_SIZE = 10
NODES = GRID_SIZE**2
PERIODS = 3 #48
MAX_WEIGHT = 10
MAX_INTENSITY = 100
MAX_DURATION = 10
MID_DAY = 24
DESTINATION = (GRID_SIZE - 1, GRID_SIZE - 1)
EDGE_GRADIENT = .005 #percent change in coeff's between edges
PERCENT_SEED_EDGES = .1
SENSOR_TIME_POS = 1
SENSOR_NODE_POS = 0
MINS_IN_A_DAY = 1440
PERIOD_IN_MINS = MINS_IN_A_DAY/PERIODS


#Q Learning
ALPHA = 0.5 #learning rate
ALPHA_ADJ_PERIOD = 0.3 #learning rate for states with adjacent time periods
GAMMA = 1.0 #discount factor 

#Epsilon Greedy Explorer
EPSILON = .4 #0.1
DECAY = 0.99999 #0.9999

#task
STATES = NODES * PERIODS
POSSIBLE_ACTIONS = 4

#main
TRIALS = 1000
