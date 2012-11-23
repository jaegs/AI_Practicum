'''
Created on Nov 22, 2012

@author: Sercan
'''
from grid import Grid

'''
A Traveler on the grid
params:
    path: list of ((int,int),(int,int))
    start_time: double
    grid: grid of type Grid that the traveler is going to travel on
'''
TIME_INTERVAL = 30
class Traveler(object):
    
    def __init__(self,path, start_time, grid):
        self.path = path
        self.start_time = start_time
        self.grid = grid
    
    def findEdge(self,edgeKey):
        (firstTuple, secondTuple) = edgeKey
        if edgeKey in self.grid.edgeDict:
            return self.grid.edgeDict[edgeKey]
        else:
            return self.grid.edgeDict[(secondTuple,firstTuple)]
    
    def travel(self):
        current_time = self.start_time
        total_time = 0
        interval_time = 0
        traversed_path = []
        for edge in self.path:
            traversed_path.append((edge,current_time))
            current_travel_time = self.findEdge(edge).travelTime(current_time)
            total_time += current_travel_time
            interval_time += current_travel_time
            current_time += current_travel_time / TIME_INTERVAL #We can always cast to int in case we want discrete
            
        return (traversed_path, total_time)

# Some code for testing
#g = Grid()
#t = Traveler([((1,1),(1,2)),((1,2),(2,2)),((2,2),(3,2)),((3,2),(4,2)),((4,2),(4,3))],2.0,g)
#print t.travel()
#g.toString(2)
    
