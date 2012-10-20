'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import math

class Edge(object):
    '''
    classdocs
    '''


    def __init__(self, weight, intensity, duration):
        '''
        Constructor
        '''
        self.weight = weight
        self.intensity = intensity
        self.duration = duration
        
    def travelTime(self, time):
        return 