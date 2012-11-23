'''
Created on Nov 23, 2012

@author: test
'''
from pybrain.rl.experiments.episodic import EpisodicExperiment
class TripExperiment(EpisodicExperiment):
    '''
    classdocs
    '''


    def __init__(self, task, agent):
        '''
        Constructor
        '''
        EpisodicExperiment.__init__(self, task, agent)
        