'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import networkx as nx

GRID_SIZE = 100
MAX_BASETIME = 10
MAX_INTENSITY = 100
MAX_DURATION = 10
#percent change in coeff's between edges
EDGE_GRADIENT = .005

class Grid(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.grid = nx.Graph()
        
F = Grid()