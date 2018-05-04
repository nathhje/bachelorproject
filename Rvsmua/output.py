"""
12 April 2018 by Nathalie van Sterkenburg.
Outputs the results of both a simulation of photons in tissue, as an analytical
solution. Currently outputs a figure for R vs r for the analytical solution and 
one where the two are compared.
"""

import analytical
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def output(prop):
    """
    Generates the output of both the simulation and the analytical solution.
    Generates two R vs r graphs, one for the analytical solution and one with 
    both. And some print statements.
    """ 
        
    AREA = 2 * math.pi * (prop.rmax ** 2 - prop.rmin ** 2)
    print(prop.R)
    # Reflection is normalized.
    prop.R = prop.R / (AREA * prop.N)
    print(prop.R)
    # Analytical solution is generated and R vs r plotted.
    analyticalprops = analytical.main()
    
    # Plot combining R vs r of analytical solution and simulation.
    plt.figure()
    plt.plot(prop.r, prop.R, 'go')
    plt.plot(analyticalprops.rlist, analyticalprops.Rlist)
    plt.yscale("log")
    plt.axis([0, 0.35, 10**-2, 10**2])
    #plt.xlim(0.01, 0.35)
    #plt.ylim(10**-2, 10**2)
    plt.show()