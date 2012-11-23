'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import math
import random

NOISE_STD_DEV = 0.5



class Edge(object):
    '''
    classdocs
    '''


    def __init__(self, weight, duration, intensity):
        '''
        Constructor
        '''
        self.weight = weight
        self.intensity = intensity
        self.duration = duration
        
    def travelTime(self, time):
        ##Sometimes we get negative values. Maybe use the absolute value?
        return random.normalvariate(\
                self.weight + self.intensity * math.exp(-1 * self.duration * time), \
                NOISE_STD_DEV)