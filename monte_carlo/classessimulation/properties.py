"""
The class contains a list of all properties necessary for simulating a photon
moving through tissue. Also contains functions to store weight the right way
and functions that provide output.
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import helpers.analytical as analytical
import csv

class Properties:
    
    def __init__(self, mua, r, name):
        """ A list of all the necessary properties. """
        
        # How the simulation is run
        self.name = name
        
        # Used to save photons in csv
        self.photonstates = []
        
        # The tissue properties
        self.mu_a = mua
        self.mu_c = 10.
        self.g = 0.8
        self.n = 1.
        self.mu_s = self.mu_c / (1 - self.g)
        self.mu_t = self.mu_a + self.mu_s
        
        # Properties of the front boundary
        self.z1 = 0.
        self.n1 = 1.
        
        # The radial distance for which reflectance is stored in case of RvsMua,
        # because the situation is point symmetric, no angle is defined
        self.r = r
        self.rmin = self.r - 10.**-3
        self.rmax = self.r + 10.**-3
        
        # Defines the area where bins are located and absorptions can be stored
        # in case of Rvsr, because the situation is point symmetric, no angle 
        # is defined
        self.rlim = 0.35
        self.zlim = 0.1
        
        # Magic numbers for number of bins and the values that handle absorption
        self.BINS = 200
        self.TRESHOLD = 10. ** -4
        self.CHANCE = 0.1
        
        # The size of the bins
        self.dr = self.rlim / self.BINS
        self.dz = self.zlim / self.BINS
        
        # The number of photons emitted and the number of photons running at once
        self.N = 1000000
        self.Nt = 1000
        
        # Each bin saves the amount of weight that was absorped in range of that bin
        self.A = np.zeros([self.BINS, self.BINS])
        self.R = [0 for i in range(self.BINS)]
        
        # The reflectance at distance r, used in case of RvsMua
        self.Rr = 0
        
        # abcounter is the number of photons absorped
        self.abcounter = 0
        # madecounter is the number of photons made
        self.madecounter = 0
        
        # the list of all photons
        self.photon_list = []
        
    def RvsrBins(self, photon):
        """ Puts absorped weight in right bin. """
        
        # Calculates r and proper bin indices
        r = (photon.x**2 + photon.y**2) ** 0.5
        ir = round(r/self.dr)
        iz = round(abs(photon.z)/self.dz)
    
        ir, iz = int(ir), int(iz)
    
        # Makes sure indices aren't out of range
        if ir >= self.BINS:
            ir = self.BINS - 1
        
        if iz >= self.BINS:
            iz = self.BINS - 1
    
        # Adds the right photon weight to the right bin.
        self.A[ir][iz] += photon.weight * self.mu_a / self.mu_t
    
    def RvsrReflect(self, r, goneweight):
        """ Puts reflected weight in right bin. 
        
        r: the radial distance of the reflected weight.
        goneweight: the weight that is reflected.
        """
        
        # the index of the right bin
        ir = int(round(r / self.dr))
    
        # Makes certain the bin index isn't out of range
        if ir >= self.BINS:
            ir = self.BINS - 1
        
        # Puts the right weight in the right bin
        self.R[ir] += goneweight
        
    def RvsMuaReflect(self, r, goneweight):
        """ Saves reflected weight if it's at the right radial distance. 
        
        r: the radial distance of the reflected weight.
        goneweight: the weight that is reflected.
        """
        
        # If the photon is reflected at the right distance, the weight is saved
        if self.rmin <= r <= self.rmax:
        
            self.Rr += goneweight
            
    def savePhotonsReflect(self, r, goneweight, photon, s1):
        """ Saves a reflected photon. The list of reflected photons is written
        to a csv file.
        """
        
        # radial distance (cm), weight (starts at 1), path travelled (cm)
        self.photonstates.append([r,  goneweight, photon.path - s1])
        
    def RvsMua(self, mualist, Rlist, analist):
        """ Generates a plot of R vs mua. """
        
        # The reflectances are normalized
        AREA = math.pi * (self.rmax ** 2 - self.rmin ** 2)
        
        for R in Rlist:
            
            R = R / (AREA * self.N)
    
        # Plot combining R vs mua of analytical solution and simulation.
        plt.figure()
        plt.plot(mualist, Rlist, 'go')
        plt.plot(mualist, analist)
        plt.title("Reflectance as a function of absorption coefficient")
        plt.xlabel("mu_a (cm^-1)")
        plt.ylabel("photons / mm^2")
        plt.show()
        
    def RvsrOutput(self, mua):
        """
        Generates the output of both the simulation and the analytical solution.
        Generates three R vs r graphs, one for the analytical solution, one for the
        simulation and one with both.
        """ 
        
        # Normalizes the data
        for ir in range(self.BINS):
            
            # Bin volume and bin area are calculated
            V = 2 * math.pi * (ir - 0.5) * self.dr ** 2 * self.dz
            
            AREA = 2 * math.pi * (ir - 0.5) * self.dr ** 2
            
            # Reflection bins are normalized
            self.R[ir] = self.R[ir] / (AREA * self.N)
            
            # In tissue bins are normalized
            for iz in range(self.BINS):
                
                self.A[ir, iz] = self.A[ir, iz] / (V * self.N)
        
        
        # Lists for x and y axes are generated
        ir_list = [i for i in np.arange(self.dr, self.rlim - self.dr - 0.5 * self.dr, self.dr)]
        iz_list = [i for i in np.arange(self.dz, self.zlim - self.dz - 0.5 * self.dz, self.dz)]
        
        # First and last value are not accurate, so they are removed
        # Removal for the in tissue matrix
        # Lists B, ir_list and iz_list were used for a 3D-plot of the location
        # of absorption in tissue. But for this project the plot wasn't 
        # necessary and was removed. The lists are still there so they may
        # be used later
        B = np.zeros([self.BINS - 2, self.BINS - 2])
        
        for ir in range(self.BINS - 2 - len(ir_list), self.BINS - 2):
        
            for iz in range(self.BINS - 2):
                
                j = ir + 1
                k = iz + 1
                
                B[ir, iz] = self.A[j, k]
        
        # Removal for the reflection
        T = []
        
        for ir in range(self.BINS - 2 - len(ir_list), self.BINS - 2):
            
            T.append(self.R[ir + 1])
        
        ir_matrix, iz_matrix = np.meshgrid(ir_list, iz_list)
        
        # Plot of R vs r
        plt.figure()
        plt.plot(ir_list, T, 'p-')
        plt.plot(ir_list, T, 'go')
        plt.yscale("log")
        plt.title("reflectance of photons")
        plt.xlabel("r(cm)")
        plt.ylabel("R(cm^-2)")
        plt.show()
        
        # Analytical solution is generated and R vs r plotted
        analyticalprops = analytical.main(mua)
        
        # Plot combining R vs r of analytical solution and simulation
        plt.figure()
        plt.plot(ir_list, T, 'ro')
        plt.plot(analyticalprops.rlist, analyticalprops.Rlist, 'b-')
        plt.yscale("log")
        plt.xlim(0.01, 0.35)
        plt.ylim(10**-2, 10**2)
        plt.title(r"Reflectance as a function of radius at $\mu_a=5cm^{-1}$")
        plt.xlabel(r"$r (cm)$")
        plt.ylabel(r"$R (cm^{-2})$")
        plt.legend(("simulation", "analytical"))
        plt.show()
        
        return ir_list, T
        
    def savePhotons(self):
        """ Saves all saved reflections to a csv file. """
        
        filename = 'generateddata/photonsformua' + str(self.mu_a) + '.csv'
        
        with open(filename, 'a', newline = '') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        
            for row in self.photonstates:
                writer.writerow(row)
               
        # List is reset for next set of reflections
        self.photonstates = []