# -*- coding: utf-8 -*-
"""
Numerically performs a Laplace transform on a path length distribution constructed
from a data set to get reflectance as a function of absorption coefficient.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    
    # Lists for the data points of the path length distribution
    theweights = []
    pathlengths = []
    
    # The radial distance where the reflectance is determined
    r = 0.3
    
    # The range in which radial distances are close enough to r to be counted
    delta = 0.001
    
    # The list of mua for which reflectances are determined, is created
    mua = [i for i in np.arange(0.0, 12., 1)]
    
    # Placeholders for all reflectance points are created
    reflectance = [0 for i in np.arange(0.0, 12., 1)]
    
    # The path length distribution is taken from the file
    with open("data/photonsformua0.0.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if r - delta < float(row[1]) <= r + delta:
                theweights.append(float(row[2]))
                pathlengths.append(float(row[3]))
            
    # The path length distribution is plotted
    plt.figure()
    plt.hist(pathlengths, bins=100, weights=theweights)
    plt.show()
    
    # For each path length, all reflections with this path length are searched
    # for and added to the reflectance
    for rho in np.arange(0., 40., delta):
        
        reflection = 0
        
        gem = (2 * rho + delta) / 2
        
        # Determines for each reflection if it has the right path length
        for i in range(len(pathlengths)):
            
            if rho < pathlengths[i] < rho + delta:
                
                # If so, its weight is added to the reflection
                reflection += theweights[i]
        
        # This reflection is used to update the reflectance of each entry, using
        # the formula for a Laplace transform
        for i in range(len(mua)):
            
            R = delta * reflection * math.e ** (- mua[i] * gem)
            
            reflectance[i] += R
    
    # Reflectance as a function of absorption coefficient is plotted
    plt.figure()
    plt.plot(mua, reflectance)     
    plt.plot(mua, reflectance, 'bo')       
    
if __name__ == "__main__":
    main()