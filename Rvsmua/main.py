# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:22:02 2018

@author: navansterkenburg

Runs simulation for multiple mua and makes R vs mua plots.
"""
import matplotlib.pyplot as plt

import runsimulation as rs
import numpy as np

def main():
    
    mualist = []
    Rlist = []
    
    for mua in np.arange(0.1, 4., 0.1):
        
        mualist.append(mua)
    
        prop = rs.runSimulation(mua)
        
        Rlist.append(prop.R)
        
        # Plot of pathlength distribution.
        plt.figure()
        plt.hist(prop.pathlengths, bins = 100, weights = prop.weights)
        plt.title("Pathlength distribution for mu_a = {}".format(mua))
        plt.xlabel("pathlength (cm or mm ?)")
        plt.ylabel("amount of photons")
        
    prop.RvsMua(mualist, Rlist)
    
if __name__ == "__main__":
    
    main()