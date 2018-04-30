"""
12 April 2018 by Nathalie van Sterkenburg.
Outputs the results of both a simulation of photons in tissue, as an analytical
solution. Currently outputs a figure for R vs r for the analytical solution,
one for the simulation and one where the two are compared.
"""

import analytical
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def output(prop):
    """
    Generates the output of both the simulation and the analytical solution.
    Generates three R vs r graphs, one for the analytical solution, one for the
    simulation and one with both. And some print statements.
    """ 
    
    # Prints the number of weight that was reflected.
    print("output")
    print(prop.totalR)
    
    # Normalizes the data.
    for ir in range(prop.BINS):
        
        # Bin volume and bin area are calculated.
        V = 2 * math.pi * (ir - 0.5) * prop.dr ** 2 * prop.dz
        
        AREA = 2 * math.pi * (ir - 0.5) * prop.dr ** 2
        
        # Reflection bins are normalized.
        prop.R[ir] = prop.R[ir] / (AREA * prop.N)
        
        # In tissue bins are normalized.
        for iz in range(prop.BINS):
            
            prop.A[ir, iz] = prop.A[ir, iz] / (V * prop.N)
    
    
    # Lists for x and y axes are generated.
    ir_list = [i for i in np.arange(0.01, prop.rmax - prop.dr - 0.5 * prop.dr, prop.dr)]
    iz_list = [i for i in np.arange(prop.dz, prop.zmax - prop.dz - 0.5 * prop.dz, prop.dz)]
    
    # First and last value are not accurate, so they are removed
    # Removal for the in tissue matrix.
    B = np.zeros([prop.BINS - 2, prop.BINS - 2])
    
    for ir in range(prop.BINS - 2 - len(ir_list), prop.BINS - 2):
    
        for iz in range(prop.BINS - 2):
            
            j = ir + 1
            k = iz + 1
            
            B[ir, iz] = prop.A[j, k]
    
    # Removal for the reflection.
    T = []
    
    for ir in range(prop.BINS - 2 - len(ir_list), prop.BINS - 2):
        
        T.append(prop.R[ir + 1])
    
    ir_matrix, iz_matrix = np.meshgrid(ir_list, iz_list)
    
    # Some print statements to check accuracy.
    print("last stuff")
    print(len(prop.pathlengths))
    print(T[0])
    print(T[1])
    
    # Plot of pahtlength distribution.

    plt.figure()
    plt.hist(prop.pathlengths)
    plt.show()
    
    # Plot of R vs r.
    plt.figure()
    plt.plot(ir_list, T, 'p-')
    plt.plot(ir_list, T, 'go')
    plt.title("500 bins")
    plt.xlabel("r(cm)")
    plt.ylabel("R(cm^-2)")
    plt.show()
    
    # 3D plot of A vs r vs z.
    """
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    surf = ax.plot_surface(ir_matrix, iz_matrix, B, cmap=plt.cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_xlabel("r (cm)")
    ax.set_ylabel("z (cm)")
    ax.set_zlabel("A")
    fig.colorbar(surf, shrink=0.5, aspect=5, label = "Value of A")
    plt.show()
    """
    
    # Analytical solution is generated and R vs r plotted.
    analyticalprops = analytical.main()
    
    # Plot combining R vs r of analytical solution and simulation.
    plt.figure()
    plt.plot(ir_list, T, 'p-')
    plt.plot(ir_list, T, 'go')
    plt.plot(analyticalprops.rlist, analyticalprops.Rlist)
    plt.xlim(0.01, 0.15)
    plt.show()