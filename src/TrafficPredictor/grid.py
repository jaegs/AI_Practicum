'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import networkx as nx
from random import *
from edge import Edge

from pybrain.utilities import Named
from pybrain.rl.environments.environment import Environment

GRID_SIZE = 5
MAX_WEIGHT = 10
MAX_INTENSITY = 100
MAX_DURATION = 10
#percent change in coeff's between edges
EDGE_GRADIENT = .005
PERCENT_SEED_EDGES = .1

U_POS = 0
V_POS = 1
EDGE_DATA_POS = 2
EDGE_KEY = "object"

class Grid(Environment):
    '''
    classdocs
    '''
        
    def __init__(self):
        '''
        Constructor
        
        Makes a basic 2d grid graph with all edge parameters initialized.
        
        To simulate traffic jams, some edges will be seeds with random parameters. 
        The rest of the edges will be filled in slowly so that they have similar 
        parameters to at least one of their adjacent edges.
        '''

        self.grid = nx.grid_2d_graph(GRID_SIZE, GRID_SIZE)
        
        edges = self.grid.edges(data = True)
        shuffle(edges)
        
        division = int(len(edges) * PERCENT_SEED_EDGES)
        seeds = edges[:division]
        rest = edges[division:]
        for _, _, data in seeds:
            weight = randint(0, MAX_WEIGHT)
            intensity = randint(0, MAX_INTENSITY)
            duration = randint(0, MAX_DURATION)
            #makes the node object a property of the edge
            data[EDGE_KEY] = Edge(weight, intensity, duration)
            
        get_gradient = lambda : (1 + choice((-1,1)) * EDGE_GRADIENT)
        rest = dict([((e[U_POS], e[V_POS]), e[EDGE_DATA_POS]) for e in rest]) #(u,v) : data dictionary
        while(rest):
            for (u,v), data in rest.items():
                #get adjacent edges from both u and v nodes that have params initialized
                neighbor_edges = [edge for edge in self.grid.edges_iter(nbunch=[u, v], data = True) if edge[EDGE_DATA_POS]]
                if (neighbor_edges):
                    neighbor_data = choice(neighbor_edges)[EDGE_DATA_POS][EDGE_KEY]
                    weight = get_gradient() * neighbor_data.weight
                    intensity = get_gradient() * neighbor_data.intensity
                    duration = get_gradient() * neighbor_data.duration
                    data[EDGE_KEY] = Edge(weight, intensity, duration)
                    del rest[(u,v)]
                    
    def getSensors(self):
        """
            See pybrain/rl/environments/environment.py
            :rtype: numpy array double
        """
        pass
    
    def performAction(self):
        """
            :key action: an action that should be executed in the Environment. 
            :type action: by default, this is assumed to be a numpy array of doubles
        """
        pass
    
    def reset(self):
        pass
         
        
F = Grid()
print( F.grid.edges(data=True))