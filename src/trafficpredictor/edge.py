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
        
    def travelTime(self, time, addNoise = True):
        exp = math.exp(-1. * ((time - float(const.PERIODS) / 2.) / self.duration) ** 2.)
        #normal dist generator truncated on [0,+inf]
        noise = ss.truncnorm.rvs(self.intensity * -1, float("inf"), scale = const.NOISE_STD_DEV)
        return self.weight + \
            (self.intensity + noise*addNoise) * exp \
         
#ex = Edge(30., 10., 10.)
#for i in xrange(48):
#    print ex.travelTime(float(i))

#Plots travel time scatter plot.
"""
import matplotlib.pyplot as plt
import numpy as np
edge = Edge(30., 10., 10.)
x, y = [], []
for t in xrange(100):
    x_t = t/100. * const.PERIODS
    y_t = edge.travelTime(x_t, addNoise = False)
    x.append(x_t)
    y.append(y_t)
    
s1, s2 = [], []
for i in xrange(1000):
    x_i = random.uniform(0., const.PERIODS)
    y_i = edge.travelTime(x_i)
    s1.append(x_i)
    s2.append(y_i)

avg_line = plt.plot([0,const.PERIODS], [np.mean(s2)]*2, label = "Daily average")
weight_line = plt.plot([0, const.PERIODS], [edge.weight]*2, label="No traffic")
scatter = plt.scatter(s1,s2, label="Travel times")
line = plt.plot(x,y, label = "Mean")
plt.setp(scatter, linewidth =.1)
plt.setp(line, color = 'r', linewidth=6.0)
plt.title("Daily Measured Travel Times For One Segment")
plt.legend()
plt.show()
"""