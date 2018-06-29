# -*- coding: utf-8 -*-
"""
Runs the simulation with the right variables and handles output.
"""

import helpers.runsimulation as run
import numpy as np
import matplotlib.pyplot as plt
import helpers.muaanalytical as muaAna

def Rvsr():
    """ Runs the simulation once for a given mua. """
    
    mua = 10.
    prop = run.runSimulation(mua, 0.0, "Rvsr")
    
    prop.RvsrOutput(mua)
    
def RvsMua():
    """ Runs the simulation for a range of mua and keeps track of reflectance
    at a certain r. 
    """ 
    
    r = 0.3
    mualist = []
    Rlist = []
    analist = []
    
    for mua in np.arange(0.1, 7, 0.4):
        
        mua = round(mua,1)
        print(mua)
    
        # Running simulation
        prop = run.runSimulation(mua, r, "RvsMua")
        
        # Analytical solution for comparison
        anaMua = muaAna.reflectance(mua, r)
        
        mualist.append(mua)
        analist.append(anaMua)
        Rlist.append(prop.Rr)
        
    prop.RvsMua(mualist, Rlist, analist)
    
def savePhotons():
    """ Runs the simulation and saves reflections to a csv file. """
    
    r = 0.3
    
    for mua in np.arange(6.55, 10.01, 0.05):
        
        mua = round(mua,2)
        print(mua)
    
        run.runSimulation(mua, r, "savePhotons")
        
def RvsrThree():
    """ Runs the simulation for three different mua and plots all R vs r
    together. """
    
    r = 0.
    
    # The simulations are run and right outputs generated
    prop = run.runSimulation(0.1, r, "Rvsr")
    ir_list1, T1 = prop.RvsrOutput(0.1)
    prop = run.runSimulation(1., r, "Rvsr")
    ir_list2, T2 = prop.RvsrOutput(1.)
    prop = run.runSimulation(2., r, "Rvsr")
    ir_list3, T3 = prop.RvsrOutput(2.)
    
    # The plot of all three is made
    plt.figure()
    plt.plot(ir_list1, T1, 'bo')
    plt.plot(ir_list2, T2, 'go')
    plt.plot(ir_list3, T3, 'ro')
    plt.yscale("log")
    plt.xlim(0.01, 0.35)
    plt.ylim(10**-2, 10**2)
    plt.title("Reflectance as a function of radius")
    plt.xlabel("r (cm)")
    plt.ylabel("R (cm^-2)")
    plt.show()