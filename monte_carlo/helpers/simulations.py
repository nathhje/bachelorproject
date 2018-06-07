# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:44:48 2018

@author: Gebruiker
"""

import helpers.runsimulation as run
import numpy as np
import matplotlib.pyplot as plt

def Rvsr():
    
    mua = 0.1
    prop = run.runSimulation(mua, 0.0, "Rvsr")
    
    prop.RvsrOutput(mua)
    
def RvsMua():
    
    r = 0.3
    mualist = []
    Rlist = []
    
    for mua in np.arange(0.1, 1.5, 0.2):
        
        mua = round(mua,1)
        print(mua)
        
        mualist.append(mua)
    
        prop = run.runSimulation(mua, r, "RvsMua")
        
        Rlist.append(prop.Rr)
        
    prop.RvsMua(mualist, Rlist)
    
def savePhotons():
    
    r = 0.3
    mualist = []
    Rlist = []
    
    for mua in np.arange(20, 21, 0.2):
        
        mua = round(mua,1)
        print(mua)
        
        mualist.append(mua)
    
        prop = run.runSimulation(mua, r, "savePhotons")
        
        Rlist.append(prop.R)
        
def RvsrThree():
    
    r = 0.
    
    prop = run.runSimulation(0.1, r, "Rvsr")
    ir_list1, T1 = prop.RvsrOutput(0.1)
    prop = run.runSimulation(1., r, "Rvsr")
    ir_list2, T2 = prop.RvsrOutput(1.)
    prop = run.runSimulation(2., r, "Rvsr")
    ir_list3, T3 = prop.RvsrOutput(2.)
    
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