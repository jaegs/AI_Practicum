__author__ = "Thomas Rueckstiess, ruecksti@in.tum.de"

from scipy import random, array
import random

from pybrain.rl.explorers.discrete.discrete import DiscreteExplorer

class FeasibleEpsilonGreedyExplorer(DiscreteExplorer):
    """ 
        The default EpsilonGreedyExplorer assumes that every state has the same
        number of actions. - Benjamin
        ==================================================================
        A discrete explorer, that executes the original policy in most cases,
        but sometimes returns a random action (uniformly drawn) instead. The
        randomness is controlled by a parameter 0 <= epsilon <= 1. The closer
        epsilon gets to 0, the more greedy (and less explorative) the agent
        behaves.
    """

    def __init__(self, epsilon = 0.3, decay = 0.9999):
        DiscreteExplorer.__init__(self)
        self.epsilon = epsilon
        self.decay = decay
        
        
    def activate(self, state, action):
        self.state = state
        return DiscreteExplorer.activate(self, state, action)

    def _forwardImplementation(self, inbuf, outbuf):
        """ Draws a random number between 0 and 1. If the number is less
            than epsilon, a random action is chosen. If it is equal or
            larger than epsilon, the greedy action is returned.
        """
        assert self.module

        if random.random() < self.epsilon:
            #only the actions that have a Q value > -infinity are valid
            actionValues = self.module.getActionValues(self.state)
            #print(actionValues)
            actions = [a for a in xrange(len(actionValues)) if actionValues[a] > float("-inf")]
            print "Action values", actionValues
            print "Actions", actions
            outbuf[:] = random.choice(actions)
        else:
            outbuf[:] = inbuf

        self.epsilon *= self.decay


