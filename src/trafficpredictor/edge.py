'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import math
import random
import const 

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
        return  self.weight + max(0,random.normalvariate(\
                self.intensity * math.exp(-1 * self.duration * (time - const.MID_DAY)**2), \
                const.NOISE_STD_DEV))