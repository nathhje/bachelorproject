# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:22:02 2018

@author: navansterkenburg

Runs simulation for multiple mua and makes R vs mua plots.

New batch saved: 1700000
Working on: 000000

Current number of photons saved: 2000000
Currently working on: 000000

Current saved without absorption: 2000000
Currently working on: 0000000
"""
import matplotlib.pyplot as plt

import runsimulation as rs
import numpy as np
import csv 

def main(r):
    
    mualist = []
    Rlist = []
    
    for mua in np.arange(1.0, 1.05, 0.2):
        
        mua = round(mua,1)
        print(mua)
        
        mualist.append(mua)
    
        prop = rs.runSimulation(mua, r)
        
        Rlist.append(prop.R)
        
    # Plot of pathlength distribution.
    plt.figure()
    plt.hist(prop.pathlengths, bins = 100, weights = prop.weights)
    plt.title("Pathlength distribution for mu_a = {}".format(mua))
    plt.xlabel("pathlength (cm or mm ?)")
    plt.ylabel("amount of photons")
        
    prop.RvsMua(mualist, Rlist) 
    prop.oneOutput()

    
    
    return mualist, Rlist
    
if __name__ == "__main__":
    
    main(0.2)