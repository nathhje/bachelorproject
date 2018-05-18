"""
12 April 2018 by Nathalie van Sterkenburg.
The class contains a list of all properties necessary for simulating a photon
in tissue.
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import analytical
import csv

class Properties:
    """ A list of all the necessary properties. """
    
    def __init__(self, mua, r):
        
        # Used for keeping up with total amounts.
        self.reflects = []
        # Used for pathlength distribution.
        self.pathlengths = []
        self.weights = []
        self.photonstates = []
        
        # The tissue properties.
        self.mu_a = mua
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
        self.r = r
        self.rmin = self.r - 10.**-3
        self.rmax = self.r + 10.**-3
        
        # Magic numbers for number of bins and the values that handle absorption.
        self.BINS = 200
        self.TRESHOLD = 10. ** -4
        self.CHANCE = 0.1
        
        # The number of photons emitted and the number of photons running at once.
        self.N = 500000
        self.Nt = 50000
        
        # This is the result of the simulation.
        # R is the amount of reflection at the measured distance.
        self.R = 0
        
        # abcounter is the number of photons absorped.
        self.abcounter = 0
        # madecounter is the number of photons made.
        self.madecounter = 0
        self.photon_list = []
        
    
    def oneOutput(self):
        """
        Generates the output of the simulation and the analytical solution.
        Generates an R vs r graphs, that contains the graph of the analytical
        solution and a point for the reflectance at the chosen r.
        """ 
        
        AREA = math.pi * (self.rmax ** 2 - self.rmin ** 2)
        print(self.R)
        # Reflection is normalized.
        self.R = self.R / (AREA * self.N)
        print(self.R)
        # Analytical solution is generated and R vs r plotted.
        analyticalprops = analytical.main()
    
        # Plot combining R vs r of analytical solution and simulation.
        plt.figure()
        plt.plot(self.r, self.R, 'go')
        plt.plot(analyticalprops.rlist, analyticalprops.Rlist)
        plt.yscale("log")
        plt.axis([0, 0.35, 10**-2, 10**2])
        #plt.xlim(0.01, 0.35)
        #plt.ylim(10**-2, 10**2)
        plt.show()
        
    def RvsMua(self, mualist, Rlist):
        """ Generates a plot of R vs mua. """
        
        # The reflectances are normalized
        AREA = math.pi * (self.rmax ** 2 - self.rmin ** 2)
        
        for R in Rlist:
            
            R = R / (AREA * self.N)
    
        # Plot combining R vs r of analytical solution and simulation.
        plt.figure()
        plt.plot(mualist, Rlist, 'go')
        plt.title("Reflectance as a function of absorption coefficient")
        plt.xlabel("mu_a (cm^-1)")
        plt.ylabel("photons / mm^2")
        plt.show()
        
    def savePhotons(self):
        
        filename = 'photonsformua' + str(self.mu_a) + '.csv'
        
        with open(filename, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            for row in self.photonstates:
                writer.writerow(row)
                
        self.photonstates = []