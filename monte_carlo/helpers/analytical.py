"""
Analytical solution for reflectance as a function of radial distance from 
photons moving through tissue.
"""

import matplotlib.pyplot as plt
import numpy as np
import helpers.muaanalytical as reflectance

def main(mua):
    """
    mua: the absorption coefficient for which the solution is determined.
    """

    # Contains list with solution
    props = Properties(mua)
    
    # Finding R for each r.
    for r in np.arange(0, 1., 0.002):
        
        props.rlist.append(r)
        
        R = reflectance.reflectance(mua, r)
            
        props.Rlist.append(R)
        
    # The result is plotted.
    plt.figure()
    plt.plot(props.rlist, props.Rlist)
    plt.title("Analytical")
    plt.xlabel("r(cm)?")
    plt.ylabel("R(photons/cm)?")
    plt.yscale("log")
    plt.axis([0, 0.35, 10**-2, 10**2])
    plt.show()
    
    return props
    
class Properties:
    """ Contains the solution. """
    
    def __init__(self, mua):
        
        self.rlist = []
        self.Rlist = []
        
if __name__ == "__main__":
    mua = 1.
    main(mua)