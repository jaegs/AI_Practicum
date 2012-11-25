'''
Created on Oct 19, 2012

@author: Benjamin Jaeger
'''

import math
import random
import const
import scipy.stats as ss

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

        #normal dist generator truncated on [0,+inf]
        noise = ss.truncnorm.rvs(0.0, float("inf"), scale = const.NOISE_STD_DEV)
        return self.weight + \
            (self.intensity + noise) * math.exp(-1. * ((time - float(const.PERIODS) / 2.) / self.duration) ** 2.) \


