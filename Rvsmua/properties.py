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
        
        # The R for which the propagation is measured.
        # Because the situation is point symmetric, no angle is defined.
        self.r = 0.2
        self.rmin = self.r - 10.**-3
        self.rmax = self.r + 10.**-3
        
        # Magic numbers for number of bins and the values that handle absorption.
        self.BINS = 200
        self.TRESHOLD = 10. ** -4
        self.CHANCE = 0.1
        
        # The number of photons emitted and the number of photons running at once.
        self.N = 1000000
        self.Nt = 100000
        
        # This is the result of the simulation.
        # R is the amount of reflection at the measured distance.
        self.R = 0
        
        # abcounter is the number of photons absorped.
        self.abcounter = 0
        # madecounter is the number of photons made.
        self.madecounter = 0
        self.photon_list = []