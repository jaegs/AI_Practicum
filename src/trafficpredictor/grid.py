'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import networkx as nx
from random import *
from edge import Edge
import const
import time
import numpy as np
#from pybrain.rl.environments import Environment

from pybrain.rl.environments.environment import Environment

U_POS = 0
V_POS = 1
EDGE_DATA_POS = 2
EDGE_KEY = "object"
WEIGHT_KEY = "weight"

def node_number(node):
    a, b = node
    return a + const.GRID_SIZE * b
def int_to_node(node_num):
    a = node_num % const.GRID_SIZE
    b = int(np.floor(node_num / const.GRID_SIZE))
    return (a,b)

def action(edge):
    return const.DOWN if edge[1][0] > edge[0][0] else const.RIGHT

class InvalidActionException(Exception):
    def __init__(self, node, action):
        Exception.__init__(self)
        self.action = action
        self.node = node
    def __str__(self):
        return "Node: " + repr(self.node) + " Action: " + repr(self.action)

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
        
        self.grid = nx.grid_2d_graph(const.GRID_SIZE, const.GRID_SIZE)
        
        #Makes the graph directed so that edges either go in increasing x or y
        self.grid = self.grid.to_directed()
        to_remove = []
        for e in self.grid.edges_iter():
            ((ax, ay), (bx, by)) = e
            if(bx < ax or by < ay):
                to_remove.append(e)
        self.grid.remove_edges_from(to_remove)
        
        edges = self.grid.edges(data = True)
        shuffle(edges)
        
        division = int(len(edges) * const.PERCENT_SEED_EDGES)
        seeds = edges[:division]
        rest = edges[division:]
        for u, v, data in seeds:

            weight = randint(1, const.MAX_WEIGHT)
            intensity = randint(1, const.MAX_INTENSITY)
            duration = randint(1, const.MAX_DURATION)

            #makes the node object a property of the edge
            data[EDGE_KEY] = Edge(weight, duration, intensity)
            data[WEIGHT_KEY] = weight #so networkx shortest path can work
            
        get_gradient = lambda : (1 + choice((-1,1)) * const.EDGE_GRADIENT)
        rest = dict([((e[U_POS], e[V_POS]), e[EDGE_DATA_POS]) for e in rest]) #(u,v) : data dictionary
        
        while(rest):
            for (u,v), data in rest.items():
                #get adjacent edges from both u and v nodes that have params initialized
                outgoing_neighbors = [edge for edge in self.grid.out_edges_iter(nbunch=[u, v], data = True) if edge[EDGE_DATA_POS]]
                incoming_neighbors = [edge for edge in self.grid.in_edges_iter(nbunch=[u, v], data = True) if edge[EDGE_DATA_POS]]
                neighbor_edges = outgoing_neighbors + incoming_neighbors
#                print (u,v)
#                print "Neighbor edges: ", neighbor_edges
                if (neighbor_edges):
                    neighbor_data = choice(neighbor_edges)[EDGE_DATA_POS][EDGE_KEY]
                    weight = get_gradient() * neighbor_data.weight
                    intensity = get_gradient() * neighbor_data.intensity
                    duration = get_gradient() * neighbor_data.duration
                    data[EDGE_KEY] = Edge(weight, intensity, duration)
                    data[WEIGHT_KEY] = weight
                    del rest[(u,v)]
        

    
    def all_shortest_path_lengths(self):
        """
            Finds the shortest travel time from every node in the graph to the const.DESTINATION
            node assuming there is no traffic.
            :rtype (node, length)
        """
        lengths = []
        for n in self.grid.nodes_iter():
            length = nx.shortest_path_length(self.grid, n, const.DESTINATION, WEIGHT_KEY)
            lengths.append((n, length))
        return lengths
   
    def getSensors(self):
        """
            Return: (current time of the day, current node) tuple
        """
        return (self.time_of_day, node_number(self.current_node))
    
    def performAction(self, action):
        """
            :key action: An action that should be executed in the environment
            :type action:A string: "up" | "down" | "left" | "right"
        """
        def jump(node1, node2):
            self.total_jumps += 1
            self.time_of_day += self.grid.get_edge_data(node1,node2)[EDGE_KEY].travelTime(self.time_of_day) / const.PERIOD_IN_MINS

        #print ("Action", action)
        (i,j) = self.current_node
        if action == "up":
            jump((i-1,j),self.current_node)
            self.current_node = (i-1,j)
        elif action == const.DOWN:
            if i+1 < const.GRID_SIZE:
                jump(self.current_node, (i+1,j))
                self.current_node = (i+1,j)
            else:
                raise InvalidActionException(self.current_node, action)
        elif action == "left":
            if j-1 >= 0:
                jump((i,j-1) ,self.current_node)
                self.current_node = (i,j-1)
            else:
                raise InvalidActionException(self.current_node, action)
        elif action == const.RIGHT:
            if j+1 >= 0:
                jump(self.current_node, (i,j+1))
                self.current_node = (i,j+1)
            else:
                raise InvalidActionException(self.current_node, action)
        else:
            raise InvalidActionException(self.current_node, action)
            
        
    
    def reset(self):
        pass
    
    def reset_grid(self, time_of_day, start_node):
        self.time_of_day = time_of_day
        self.current_time = self.time_of_day
        self.current_node = int_to_node(start_node)
        self.total_jumps = 0
        #print("Start node", self.current_node)

         
    def printVerticalEdges(self,gridWidth):
        printedLine = '  |'
        for i in range(gridWidth-1):
            printedLine = printedLine + '                   |'  
        print printedLine
        
    def findAppropriateEdge(self,i,j,time, isTraffic):
        if isTraffic:
            weight = "%.5f" % self.grid.get_edge_data((i,j),(i,j+1))[EDGE_KEY].travelTime(time)
        else:
            weight = "%.5f" % self.grid.get_edge_data((i,j),(i,j+1))[EDGE_KEY].weight 
        return weight
    
    def findAppropriateVerticalEdge(self,i,j,k,l,time, isTraffic):
        if isTraffic:
            weight = "%.5f" % self.grid.get_edge_data((i,j),(k,l))[EDGE_KEY].travelTime(time)
        else:
            weight = "%.5f" % self.grid.get_edge_data((i,j),(k,l))[EDGE_KEY].weight
        return weight
    
    def toString(self, time, isTraffic):
        i = 0
        while i < const.GRID_SIZE:
            j=0
            currentLine = '('+str(i)+',0)' + "----" + self.findAppropriateEdge(i,0,time,isTraffic) + "----" + '('+str(i)+',1)'
            while j < const.GRID_SIZE - 2:
                j += 1
                currentLine = currentLine + '----' + self.findAppropriateEdge(i,j,time, isTraffic) + "----" + '('+str(i)+','+str(j+1)+')'
                
            print currentLine
            
            if i+1 < const.GRID_SIZE:
                self.printVerticalEdges(const.GRID_SIZE)
                verticalEdges = str(self.findAppropriateVerticalEdge(i, 0, i+1, 0,time, isTraffic))
                a = 1
                while a < const.GRID_SIZE:
                    verticalEdges = verticalEdges + '            ' + \
                        str(self.findAppropriateVerticalEdge(i, a, i+1, a,time,isTraffic))
                    a += 1
                print verticalEdges 
                self.printVerticalEdges(const.GRID_SIZE)
            i += 1



###Create the grid
#g = Grid()
#
##Print the whole grid
#g.toString(2,False)
#g.toString(2,True)








    
  
    
    





