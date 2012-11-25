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
        #may want to make scale change throughout day
        noise = ss.truncnorm.rvs(0.0, float("inf"), scale = const.NOISE_STD_DEV)
        return self.weight + \
            self.intensity * math.exp(-1. * ((time - float(const.PERIODS) / 2.) / self.duration) ** 2.) \
            + noise
            
            
#ex = Edge(30., 10., 10.)
#for i in xrange(48):
#    print ex.travelTime(float(i))
