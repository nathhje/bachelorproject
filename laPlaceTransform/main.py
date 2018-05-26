# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:42:00 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def main(r):
    
    theweights = []
    pathlengths = []
    r = 1.
    delta = 0.001
    
    mua = [i for i in np.arange(0.1, 3., 0.2)]
    reflectance = [0 for i in np.arange(0.1, 3., 0.2)]
    
    with open("reflectedPhotons.csv", 'r') as csvfile:
    
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        for row in reader:
            
            if r - delta < float(row[1]) <= r + delta:
                theweights.append(float(row[2]))
                pathlengths.append(float(row[3]))
            
    plt.figure()
    plt.hist(pathlengths, bins=100, weights=theweights)
    plt.show()
    
    for rho in np.arange(0., 40., delta):
        
        reflection = 0
        
        gem = (2 * rho + delta) / 2
        
        for i in range(len(pathlengths)):
            
            if rho < pathlengths[i] < rho + delta:
                
                reflection += theweights[i]
        
        for i in range(len(mua)):
            
            R = delta * reflection * math.e ** (- mua[i] * gem)
            
            reflectance[i] += R
            
    plt.figure()
    plt.plot(mua, reflectance)            
    
if __name__ == "__main__":
    main(0)