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
         
def printVerticalEdges(gridWidth):
    printedLine = '  |'
    for i in range(gridWidth-1):
        printedLine = printedLine + '                   |'  
    print printedLine
    
def findAppropriateEdge(i,j):
    weight = ""
    if ((i,j),(i,j+1)) in edgeDict:
        weight = "%.5f" % edgeDict[((i,j),(i,j+1))]
    else:
        weight = "%.5f" % edgeDict[((i,j+1),(i,j))]
    return weight

def findAppropriateVerticalEdge(i,j,k,l):
    weight = ""
    if ((i,j),(k,l)) in edgeDict:
        weight = "%.5f" % edgeDict[((i,j),(k,l))]
    else:
        weight = "%.5f" % edgeDict[((k,l),(i,j))]
    return weight



#Create the grid

F = Grid()
dictionaryBuilder = []
counter = 0
for edge in (F.grid.edges(data=True)):
    (source,sink,data) = edge
    dictionaryBuilder[len(dictionaryBuilder):] = [((source,sink),data[EDGE_KEY].travelTime(2))]
    counter += 1
edgeDict = dict(dictionaryBuilder)


#Print the whole grid

i = 0
while i < GRID_SIZE:
    j=0
    currentLine = '('+str(i)+',0)' + "----" + findAppropriateEdge(i,0) + "----" + '('+str(i)+',1)'
    while j < GRID_SIZE - 2:
        j += 1
        currentLine = currentLine + '----' + findAppropriateEdge(i,j) + "----" + '('+str(i)+','+str(j+1)+')'
        
    print currentLine
    
    if i+1 < GRID_SIZE:
        printVerticalEdges(GRID_SIZE)
        verticalEdges = str(findAppropriateVerticalEdge(i, 0, i+1, 0))
        a = 1
        while a < GRID_SIZE:
            verticalEdges = verticalEdges + '            ' + \
                str(findAppropriateVerticalEdge(i, a, i+1, a))
            a += 1
        print verticalEdges 
        printVerticalEdges(GRID_SIZE)
    i += 1
    
  
    
    





