# -*- coding: utf-8 -*-
"""
Created on Mon May  7 11:22:02 2018

@author: navansterkenburg

Runs simulation for multiple mua and makes R vs mua plots.

Current number of photons saved: 1150000 vanaf 2.5
1550000 tot en met 2.3
Currently working on: 400000

Current saved without absorption: 500000
Currently working on: 000000
"""
import matplotlib.pyplot as plt

import runsimulation as rs
import numpy as np
import csv 

def main(r):
    
    mualist = [2.5000000000000004, 2.7000000000000006, 2.900000000000001, 3.1000000000000005, 3.3000000000000007, 3.500000000000001, 3.7000000000000006, 3.900000000000001, 4.1000000000000005, 4.300000000000001, 4.500000000000001, 4.7, 4.9]
    Rlist = []
    
    for mua in mualist:
        print(mua)
    
        prop = rs.runSimulation(mua, r)
        
        Rlist.append(prop.R)
        
    # Plot of pathlength distribution.
    plt.figure()
    plt.hist(prop.pathlengths, bins = 100, weights = prop.weights)
    plt.title("Pathlength distribution for mu_a = {}".format(mua))
    plt.xlabel("pathlength (cm or mm ?)")
    plt.ylabel("amount of photons")
        
    prop.RvsMua(mualist, Rlist)   

    
    
    return mualist, Rlist
    
if __name__ == "__main__":
    
    main(0.2)