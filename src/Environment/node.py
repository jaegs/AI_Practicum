'''
Created on Oct 19, 2012

@author: Benjamin
'''

import math

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, basetime, intensity, duration):
        '''
        Constructor
        '''
        self.basetime = basetime 
        self.intensity = intensity
        self.duration = duration
        
    def travelTime(self, time):
        return self.basetime + self.intensity * math.exp(-1 * self.duration * time^2)
        