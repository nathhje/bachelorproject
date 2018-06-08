# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:42:00 2018

@author: Gebruiker
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    
    theweights = []
    pathlengths = []
    r = 0.3
    delta = 0.001
    
    mua = [i for i in np.arange(0.0, 12., 1)]
    reflectance = [0 for i in np.arange(0.0, 12., 1)]
    
    with open("data/photonsformua0.0.csv", 'r') as csvfile:
    
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
    plt.plot(mua, reflectance, 'bo')       
    
if __name__ == "__main__":
    main()