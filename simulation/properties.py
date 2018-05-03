"""
12 April 2018 by Nathalie van Sterkenburg.
The class contains a list of all properties necessary for simulating a photon
in tissue.
"""

import numpy as np

class Properties:
    """ A list of all the necessary properties. """
    
    def __init__(self):
        
        # Used for keeping up with total amounts.
        self.reflects = []
        # Used for pathlength distribution.
        self.pathlengths = []
        # Keeps up with total reflected weight to check if values are right.
        self.totalR = 0
        
        # The tissue properties.
        self.mu_a = 1.
        self.mu_c = 10.
        self.g = 0.8
        self.n = 1.
        self.mu_s = self.mu_c / (1 - self.g)
        self.mu_t = self.mu_a + self.mu_s
        
        # Properties of the front boundary.
        self.z1 = 0.
        self.n1 = 1.
        
        # The area where the propagation is measured.
        # Because the situation is point symmetric, no angle is defined.
        self.rmax = 0.35
        self.zmax = 0.1
        
        # Magic numbers for number of bins and the values that handle absorption.
        self.BINS = 200
        self.TRESHOLD = 10. ** -4
        self.CHANCE = 0.1
        
        # The size of the bins.
        self.dr = self.rmax / self.BINS
        self.dz = self.zmax / self.BINS
        
        # The number of photons emitted and the number of photons running at once.
        self.N = 500000
        self.Nt = 10000
        
        # This is the result of the simulation.
        # Each bin saves the amount of weight that was absorped in range of that bin.
        self.A = np.zeros([self.BINS, self.BINS])
        self.R = [0 for i in range(self.BINS)]
        
        # abcounter is the number of photons absorped.
        self.abcounter = 0
        # madecounter is the number of photons made.
        self.madecounter = 0
        self.photon_list = []